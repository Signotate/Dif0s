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

from signlangmtk.draw.common import directed_angle
from signlangmtk.draw.common import is_counter_clockwise
from signlangmtk.draw.common import car2pol
import math
import numpy as np


def test_directed_angle():
    assert math.pi / 2.0 == directed_angle(np.array([1.0, 0.0]),
                                           np.array([0.0, 1.0]))
    assert math.pi / 2.0 == directed_angle(np.array([0.0, 1.0]),
                                           np.array([-1.0, 0.0]))
    assert -3 * math.pi / 2.0 == directed_angle(np.array([-1.0, 0.0]),
                                                np.array([0.0, -1.0]))
    assert math.pi / 2.0 == directed_angle(np.array([0.0, -1.0]),
                                           np.array([1.0, 0.0]))


def test_is_counter_clockwise():
    assert not is_counter_clockwise(np.array([1.0, 0.0]),
                                    np.array([0.0, 1.0]))
    assert not is_counter_clockwise(np.array([0.0, 1.0]),
                                    np.array([-1.0, 0.0]))
    assert not is_counter_clockwise(np.array([-1.0, 0.0]),
                                    np.array([0.0, -1.0]))
    assert not is_counter_clockwise(np.array([0.0, -1.0]),
                                    np.array([1.0, 0.0]))

    assert is_counter_clockwise(np.array([1.0, 0.0]),
                                np.array([0.0, -1.0]))
    assert is_counter_clockwise(np.array([0.0, -1.0]),
                                np.array([-1.0, 0.0]))
    assert is_counter_clockwise(np.array([-1.0, 0.0]),
                                np.array([0.0, 1.0]))
    assert is_counter_clockwise(np.array([0.0, 1.0]),
                                np.array([1.0, 0.0]))


def test_car2pol():
    rho, phi = car2pol((0.0, 1.0))
    assert rho == 1.0
    assert phi == math.pi / 2.0

    rho, phi = car2pol((1.0, 0.0))
    assert rho == 1.0
    assert phi == 0.0

    rho, phi = car2pol((-1.0, 0.0))
    assert rho == 1.0
    assert phi == math.pi

    rho, phi = car2pol((0.0, -1.0))
    print(rho, phi)
    assert rho == 1
    assert phi == -math.pi / 2.0
