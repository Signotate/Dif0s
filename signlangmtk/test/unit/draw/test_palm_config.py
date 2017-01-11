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

from signlangmtk.model.finger import Finger
from signlangmtk.model.finger import FingerIndex
from signlangmtk.model.finger import FingerProperty
from signlangmtk.model.palm import Palm
from signlangmtk.model.palm import Orientation
from signlangmtk.model.hand import Hand
from signlangmtk.draw.common import Ellipse
from signlangmtk.draw.common import FilledArc
from signlangmtk.draw.draw_hand import palm_cfg


def test_shapes_for_palm():
    h = Hand(palm=Palm(palm_dir=Orientation.OUT, finger_dir=Orientation.BODY,
                       dominant=False, start_pos=True),
             fingers=[Finger(index=FingerIndex.THUMB,
                             properties=[FingerProperty.STRAIGHT,
                                         FingerProperty.SPREAD]),
                      Finger(index=FingerIndex.INDEX,
                             properties=[FingerProperty.STRAIGHT,
                                         FingerProperty.TOGETHER]),
                      Finger(index=FingerIndex.MIDDLE,
                             properties=[FingerProperty.STRAIGHT,
                                         FingerProperty.SPREAD]),
                      Finger(index=FingerIndex.RING,
                             properties=[FingerProperty.STRAIGHT,
                                         FingerProperty.SPREAD]),
                      Finger(index=FingerIndex.PINKY,
                             properties=[FingerProperty.STRAIGHT,
                                         FingerProperty.TOGETHER])])

    expected_shapes = [Ellipse(cx=0.000000, cy=0.000000, rx=-0.250000,
                               ry=0.500000, fill=True, line_width=0.059016)]
    palm_shapes = palm_cfg.shapes_for(h.palm)
    for expected, actual in zip(expected_shapes, palm_shapes):
        assert expected, actual

    h = Hand(palm=Palm(palm_dir=Orientation.IN, finger_dir=Orientation.UP,
                       dominant=False, start_pos=True),
             fingers=[Finger(index=FingerIndex.THUMB,
                             properties=[FingerProperty.STRAIGHT,
                                         FingerProperty.SPREAD]),
                      Finger(index=FingerIndex.INDEX,
                             properties=[FingerProperty.STRAIGHT,
                                         FingerProperty.TOGETHER]),
                      Finger(index=FingerIndex.MIDDLE,
                             properties=[FingerProperty.STRAIGHT,
                                         FingerProperty.SPREAD]),
                      Finger(index=FingerIndex.RING,
                             properties=[FingerProperty.STRAIGHT,
                                         FingerProperty.SPREAD]),
                      Finger(index=FingerIndex.PINKY,
                             properties=[FingerProperty.STRAIGHT,
                                         FingerProperty.TOGETHER])])

    expected_shapes = [Ellipse(cx=0.000000, cy=0.000000, rx=0.250000,
                               ry=0.500000, line_width=0.059016),
                       FilledArc(cx=0.000000, cy=0.000000, rx=0.250000,
                                 ry=0.500000, line_width=0.026230,
                                 start_radians=4.712389, end_radians=7.853982)]

    palm_shapes = palm_cfg.shapes_for(h.palm)
    for expected, actual in zip(expected_shapes, palm_shapes):
        assert expected, actual
