from io import BytesIO
from pkgutil import get_data
from gi.repository import GdkPixbuf
from signlangmtk.util import resource_location
import signlangmtk.difos.gui


APP_ID = 'com.eigendomain.signlangmtk.difos'
APP_TITLE = 'Dif0s'

ABOUT_TITLE = 'About Dif0s Sign Language Markup Tool'
DIFOS_VERSION = '0.1.a0dev'
ABOUT_COMMENTS = 'Dif0s models and creates sign language transcripts by ' \
                 'drawing representative diagrams '

AUTHORS = ['Brenda Clark <brendarc@hawaii.edu>',
           'Greg Clark <greg@eigendomain.com>']


def gui_resource(name):
    return resource_location(signlangmtk.difos.gui, name)


DIFOS_STYLE = gui_resource('style.css')
ICON_FILE = gui_resource('icon.png')
ICON = GdkPixbuf.Pixbuf.new_from_file_at_size(ICON_FILE, 64, 64)

MAIN_WIN_UI = gui_resource('difos_main_window.ui')
MENU_UI = gui_resource('difos_menu.ui')

DEFAULT_WIN_SIZE_X = 300
DEFAULT_WIN_SIZE_Y = 300

EXPORT_SIZE_X = 300
EXPORT_SIZE_Y = 300
