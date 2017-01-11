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

from signlangmtk.model import Palm
from signlangmtk.model import Orientation


def test_palm_init():
    p = Palm(finger_dir=Orientation.UP, palm_dir=Orientation.FORWARD)
    assert Orientation.UP == p.finger_dir
    assert Orientation.FORWARD == p.palm_dir
    assert p.dominant
    assert p.start_pos
    assert p.is_valid()

    p = Palm(finger_dir=Orientation.DOWN,
             palm_dir=Orientation.IN,
             dominant=False,
             start_pos=False)
    assert Orientation.DOWN == p.finger_dir
    assert Orientation.IN == p.palm_dir
    assert not p.dominant
    assert not p.start_pos
    assert p.is_valid()


def test_palm_conflicting_orients():
    p = Palm(finger_dir=Orientation.UP, palm_dir=Orientation.DOWN)
    assert not p.is_valid()


def test_no_dir_palm():
    p = Palm()
    assert p.finger_dir is None
    assert p.palm_dir is None
    assert p.dominant
    assert p.start_pos
    assert not p.is_valid()
