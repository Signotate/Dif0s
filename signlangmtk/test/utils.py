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

from signlangmtk.model.palm import Orientation
from signlangmtk.model.finger import Finger
from signlangmtk.model.finger import FingerIndex
from signlangmtk.model.finger import FingerProperty
from signlangmtk.model.palm import Palm
from signlangmtk.model.hand import Hand


def default_finger_props():
    return [Finger(i, [FingerProperty.FOLDED]) for i in list(FingerIndex)]


def all_orients(fingers = None):
    finger_orients = [Orientation.UP,
                      Orientation.DOWN,
                      Orientation.IN,
                      Orientation.OUT,
                      Orientation.FORWARD,
                      Orientation.BODY]

    palm_orients = [Orientation.FORWARD,
                    Orientation.BODY,
                    Orientation.IN,
                    Orientation.OUT,
                    Orientation.UP,
                    Orientation.DOWN]

    fs = fingers
    if fs is None:
        fs = default_finger_props()

    all_hands = []
    for p in palm_orients:
        for f in finger_orients:
            if not p.conflicts(f):
                palm_D = Palm(p, f)
                palm_ND = Palm(p, f, dominant=False)
                all_hands.append(Hand(palm_D, fs))
                all_hands.append(Hand(palm_ND, fs))
    return all_hands
