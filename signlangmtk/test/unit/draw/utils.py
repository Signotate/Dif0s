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

import cairo
import numpy as np


def cairo_surfaces_equal(expected, actual):
    assert isinstance(expected, cairo.ImageSurface)
    assert isinstance(actual, cairo.ImageSurface)

    assert expected.get_format() == actual.get_format()
    assert expected.get_data() == actual.get_data()


def cairo_surface(width, height):
    return cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)


def lines_similar(line1, line2):
    l1 = np.array([line1.x1, line1.y1, line1.x2, line1.y2])
    l2 = np.array([line2.x1, line2.y1, line2.x2, line2.y2])

    if not np.all(np.isclose(l1, l2)):
        return False
    if not np.isclose(line1.width, line2.width):
        return False
    if not line1.color == line2.color:
        return False
    return True
