# Sign Language Markup Tool Kit
# Tools to model, search and create scalable graphic representations of sign
# language transcripts
#
# Copyright (C) 2016, 2017 Greg Clark
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

from gi.repository import GdkPixbuf
from signlangmtk.util import resource_location
import signlangmtk.difos.gui
from signlangmtk.__about__ import *


APP_ID = 'com.eigendomain.signlangmtk.difos'
APP_TITLE = 'Dif0s'

ABOUT_TITLE = 'Dif0s Sign Language Markup Tool'
DIFOS_VERSION = __version__
ABOUT_COMMENTS = ('This tool kit provides a set of applications to model, ' +
                  'create, and search sign language transcripts as ' +
                  'described in the SiLOrB writing system developed by ' +
                  'Brenda Clark.')

CREDITS_SOFTWARE = ['Greg Clark <greg@eigendomain.com>']
CREDITS_CONCEPT = ['Brenda Clark <brendarc@hawaii.edu>']


def gui_resource(name):
    return resource_location(signlangmtk.difos.gui, name)


DIFOS_STYLE = gui_resource('dif0s_style.css')
ICON_FILE = gui_resource('dif0s.png')
ICON = GdkPixbuf.Pixbuf.new_from_file_at_size(ICON_FILE, 64, 64)

MAIN_WIN_UI = gui_resource('difos_main_window.ui')
MENU_UI = gui_resource('difos_menu.ui')

DEFAULT_WIN_SIZE_X = 300
DEFAULT_WIN_SIZE_Y = 300

EXPORT_SIZE_X = 300
EXPORT_SIZE_Y = 300
