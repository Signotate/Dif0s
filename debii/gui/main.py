import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import os
import numpy as np
from ..model.palm import parse_palm, InvalidPalmException
from ..draw import draw_palm
import cairo


class MainHandler(object):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.hand_widget = None
        self.hand_entry_text_box = args[0]
        self.main_box_layout = args[1]

    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)

    def onDisplayHand(self, *args):
        if self.hand_widget is None:
            box = self.main_box_layout
            self.hand_widget = HandWidget(text_box=self.hand_entry_text_box)
            box.pack_start(self.hand_widget, True, True, 0)
            box.show_all()
        else:
            self.hand_widget.queue_draw()

    def update_hand(self, *args):
        self.onDisplayHand(*args)


class HandWidget(Gtk.DrawingArea):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.text_box = kwargs['text_box']
        self.hand = None
        self.hand_text = None
        self.height = self.get_allocated_height()
        self.width = self.get_allocated_width()

        self.surface = None

        self.surface_width = 5000
        self.surface_height = 5000
        self.default_surface = cairo.SVGSurface(None, self.surface_width, self.surface_height)

    def do_configure_event(self, event):
        self.width = self.get_allocated_width()
        self.height = self.get_allocated_height()
        # print('In configure', self.width, self.height)
        if self.surface is None:
            self.surface = self.default_surface

        return True

    def do_draw(self, cr):
        # print('In draw:', self.width, self.height)
        self.hand_brush()
        w = self.width
        h = self.height
        cr.save()
        s = np.min([self.width / self.surface_width, self.height / self.surface_height])
        cr.translate(self.width / 2.0 - s * self.surface_width / 2.0,
                     self.height / 2.0 - s * self.surface_height / 2.0)
        cr.scale(s, s)
        cr.set_source_surface(self.surface, 0, 0)
        # cr.set_operator(cairo.OPERATOR_SOURCE)
        # cr.get_source().set_extend(cairo.EXTEND_REFLECT)
        cr.paint()
        return False

    def hand_brush(self):
        text = self.text_box.get_text()
        if text != self.hand_text:
            self.hand_text = text
            try:
                palm = parse_palm(text)
            except InvalidPalmException:
                self.surface = self.default_surface
                return

            if palm != self.hand:
                self.hand = palm

                # print("Redraw Hand")
                w = self.surface_width
                h = self.surface_height
                self.surface = cairo.SVGSurface(None, w, h)
                cr = cairo.Context(self.surface)
                cr.save()
                cr.translate(w / 2.0, h / 2.0)
                s = np.min([w, h])
                cr.scale(s / 2.0, s / 2.0)
                draw_palm(palm, cr)
                cr.restore()


if __name__ == "__main__":
    glade_file = os.path.join(os.path.dirname(__file__), 'main.glade')

    builder = Gtk.Builder()
    builder.add_from_file(glade_file)
    builder.connect_signals(
        MainHandler(
            builder.get_object('hand_entry_text_box'),
            builder.get_object('main_box_layout')))

    window = builder.get_object("main_window")
    window.set_default_size(300, 300)
    window.show_all()

    Gtk.main()
