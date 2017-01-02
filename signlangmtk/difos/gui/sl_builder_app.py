from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import Gio
from gi.repository import GObject
from gi.repository import GdkPixbuf
import cairo
import numpy as np
import sys
import os
import logging
from signlangmtk.util import setup_logging
from signlangmtk.model.palm import InvalidPalmException
from signlangmtk.model.finger import InvalidFingerException
from signlangmtk.draw import draw_hand
from signlangmtk.parser import parse_hand
from signlangmtk.parser import is_hand_string
from signlangmtk.parser import ParseException


logger = logging.getLogger(__name__)


class SignLanguageBuilderApp(Gtk.Application):
    __module_dir = os.path.dirname(__file__)
    menu_ui_file = os.path.join(__module_dir, 'sl_builder_menu.ui')
    sl_builder_window_file = os.path.join(__module_dir, 'main_window.ui')
    icon_file = os.path.join(__module_dir, 'icon.png')

    def __init__(self):
        Gtk.Application.__init__(self,
                                 application_id='com.eigendomain.debiy')

    def do_activate(self):
        screen = Gdk.Screen.get_default()
        gtk_provider = Gtk.CssProvider()
        gtk_context = Gtk.StyleContext()
        gtk_context.add_provider_for_screen(
            screen,
            gtk_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

        css_file = os.path.join(os.path.dirname(__file__), 'style.css')
        gtk_provider.load_from_path(css_file)

        self.main_window = SlBuilderMainWindow(self)
        self.main_window.show_all()

    def do_startup(self):
        Gtk.Application.do_startup(self)

        # app action quit, connected to the callback function
        quit_action = Gio.SimpleAction.new("quit", None)
        quit_action.connect("activate", self.on_quit)
        self.add_action(quit_action)
        self.set_accels_for_action('app.quit', ['<Control>q'])

        about_action = Gio.SimpleAction.new("about", None)
        about_action.connect("activate", self.on_about)
        self.add_action(about_action)

        builder = Gtk.Builder()
        try:
            builder.add_from_file(self.menu_ui_file)
        except Exception as e:
            logger.exception(e)
            logger.error('menu file not found')
            sys.exit()
        menu = builder.get_object("appmenu")
        self.set_app_menu(menu)

    def on_quit(self, action, parameter):
        self.quit()

    def on_about(self, action, parameter):
        about = Dif0sAboutDialog()
        about.run()


class SlBuilderMainWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.ApplicationWindow.__init__(self,
                                       title='DebiY',
                                       application=app)
        self.set_default_size(300, 300)
        self.set_icon_from_file(app.icon_file)

        export_action = Gio.SimpleAction.new('export', None)
        export_action.connect('activate', self.on_export)
        app.add_action(export_action)
        app.set_accels_for_action('app.export', ['<Control>e'])

        builder = Gtk.Builder()
        try:
            builder.add_from_file(app.sl_builder_window_file)
        except Exception as e:
            logger.exception(e)
            sys.exit()

        self.hand_entry = builder.get_object('hand_entry_text_box')
        self.main_box_layout = builder.get_object('main_box_layout')
        self.hand_widget = HandWidget(text_box=self.hand_entry,
                                      config_id='hand')
        self.main_box_layout.pack_start(self.hand_widget, True, True, 0)

        self.add(self.main_box_layout)
        builder.connect_signals(self)

    def on_export(self, action, parameter):
        save_dialog = Gtk.FileChooserDialog("Pick a file",
                                            self,
                                            Gtk.FileChooserAction.SAVE,
                                            (Gtk.STOCK_CANCEL,
                                             Gtk.ResponseType.CANCEL,
                                             Gtk.STOCK_SAVE,
                                             Gtk.ResponseType.ACCEPT))
        filter_svg = Gtk.FileFilter()
        filter_svg.set_name('SVG Files')
        filter_svg.add_pattern('*.svg')
        save_dialog.add_filter(filter_svg)
        filter_png = Gtk.FileFilter()
        filter_png.set_name('PNG Files')
        filter_png.add_pattern('*.png')
        save_dialog.add_filter(filter_png)

        save_dialog.set_local_only(False)
        save_dialog.set_modal(True)
        save_dialog.set_do_overwrite_confirmation(True)
        save_dialog.connect('response', self.on_export_response)
        save_dialog.show()

    def on_export_response(self, dialog, response_id):
        if response_id == Gtk.ResponseType.ACCEPT:
            try:
                self.hand_to_file(dialog.get_filename(), dialog.get_filter())
            except Exception as e:
                display_error(self, 'Could not export hand')
                logger.exception(e)
        dialog.destroy()

    def on_update_hand(self, entry):
        valid = self.hand_widget.update_hand()
        entry_style = entry.get_style_context()
        if valid:
            entry_style.remove_class('hand_entry_error')
        else:
            entry_style.add_class('hand_entry_error')


    def hand_to_file(self, filename, file_filter):
        file_type = None
        if file_filter is None:
            if filename.lower().endswith('.svg'):
                file_type = 'svg'
            elif filename.lower().endswith('.png'):
                file_type = 'png'
        if file_filter.get_name() == 'SVG Files':
            file_type = 'svg'
        elif file_filter.get_name() == 'PNG Files':
            file_type = 'png'

        if file_type is None:
            display_error(self, ('Could not export hand to %s, '
                                 + 'unsupported file type' % filename))

        if not filename.lower().endswith('.' + file_type):
            filename += '.' + file_type

        if self.hand_widget is None:
            return
        w, h = 300, 300
        try:
            surface = None
            if file_type == 'svg':
                surface = cairo.SVGSurface(filename, w, h)
            else:
                surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, w, h)
            ctx = cairo.Context(surface)
            ctx.save()
            ctx.translate(w / 2.0, h / 2.0)
            s = np.min([w, h]) / 2.0
            ctx.scale(s, s)
            draw_hand(self.hand_widget.hand, ctx)
            ctx.show_page()
            if file_type == 'png':
                surface.write_to_png(filename)
        except Exception as e:
            display_error(self, 'Could not save file')
            logger.exception(e)


class HandWidget(Gtk.DrawingArea):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.text_box = kwargs['text_box']
        self.config_id = kwargs.get('config_id', None)
        self.hand = None
        self.hand_text = None
        self.height = self.get_allocated_height()
        self.width = self.get_allocated_width()

    def do_draw(self, cr):
        if self.hand is not None:
            h = self.get_allocated_height()
            w = self.get_allocated_width()

            cr.save()
            cr.translate(w / 2.0, h / 2.0)
            s = np.min([w, h])
            cr.scale(s / 2.0, s / 2.0)
            draw_hand(self.hand, cr)
            cr.restore()

            cr.show_page()

    def update_hand(self):
        text = self.text_box.get_text().strip()
        if text != self.hand_text:
            self.hand_text = text
            self.hand = None
            try:
                self.hand = parse_hand(text)
                logger.debug(('Parsed Hand (field: %s): ' % self.config_id)
                             + repr(self.hand))
            except (InvalidPalmException, InvalidFingerException,
                    ParseException) as e:
                logger.debug(('(field %s)' % self.config_id) + str(e))
            self.queue_draw()
        return (self.hand is not None
                and self.hand.is_valid()
                and is_hand_string(text))


def display_error(window, message, secondary_text=''):
        dialog = Gtk.MessageDialog(window,
                                   0,
                                   Gtk.MessageType.ERROR,
                                   Gtk.ButtonsType.OK,
                                   message)
        dialog.format_secondary_text(secondary_text)
        dialog.run()
        dialog.destroy()


class Dif0sAboutDialog(Gtk.AboutDialog):
    def __init__(self):
        icon_file = os.path.join(os.path.dirname(__file__), 'icon.png')
        icon = GdkPixbuf.Pixbuf.new_from_file_at_size(icon_file, 64, 64)
        Gtk.AboutDialog.__init__(self)
        self.set_title('About Dif0s Sign Language Builder')
        self.set_name('Dif0s')
        self.set_version('0.1a0dev')
        self.set_comments('Dif0s models and creates diagrams of sign '
                          + 'language transcripts')
        self.set_authors(['Brenda Clark (concept)', 'Greg Clark (software)'])
        self.set_logo(icon)

        self.connect('response', self.on_response)

    def on_response(self, dialog, response):
        self.destroy()
