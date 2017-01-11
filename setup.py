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

import ez_setup
ez_setup.use_setuptools()


from setuptools import setup
from setuptools import find_packages
from signlangmtk.__about__ import *
import os


setup(
    name=__title__,
    description=__summary__,
    long_description=__long_summary__,
    version=__version__,
    packages=find_packages(),

    package_data={'signlangmtk.difos.gui':
                  ['*.ui', '*.css', '*.png', '*.ico']},
    include_package_data=True,

    author=__author__,
    author_email=__email__,
    license=__license__,

    entry_points={
        'gui_scripts': [
            'dif0s = signlangmtk.difos.__main__:main'
        ]
    },

    data_files=[
        ('share/applications', ['dif0s.desktop']),
        ('share/icons/hicolor/scalable/apps',
         ['signlangmtk/difos/gui/dif0s.svg'])
    ]
)
