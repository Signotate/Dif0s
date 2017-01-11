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

import sys
import signal
import logging
import gi
from signlangmtk.util import setup_logging

logger = logging.getLogger(__name__)


def main(log_level=logging.INFO):
    setup_logging(log_level)
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    gi.require_version('Gtk', '3.0')

    logger.info('Starting Difos')

    from signlangmtk.difos.gui.difos_app import DifosApp
    difos = DifosApp()
    return difos.run(sys.argv)


if __name__ == '__main__':
    sys.exit(main(log_level=logging.DEBUG))
