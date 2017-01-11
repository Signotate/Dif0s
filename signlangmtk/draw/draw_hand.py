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

import logging
from signlangmtk.draw.palm_config import PalmConfigs
from signlangmtk.draw.finger_config import FingerShapes
from signlangmtk.model.finger import InvalidFingerException
from signlangmtk.draw.common import Line


logger = logging.getLogger(__name__)


palm_cfg = PalmConfigs()
finger_shapes = FingerShapes()


def draw_palm(palm, ctx):
    logger.debug('Drawing Palm: ' + repr(palm))
    for s in palm_cfg.shapes_for(palm):
        s.draw(ctx)


def draw_orient_vectors(palm, ctx):
    cfg = palm_cfg(palm)
    v_finger, v_thumb, fill, v_fill_arc, _ = cfg
    Line(0.0,
         0.0,
         float(v_finger[0]),
         float(-v_finger[1]),
         color='green').draw(ctx)
    Line(0.0,
         0.0,
         float(v_thumb[0]),
         float(-v_thumb[1]),
         color='red').draw(ctx)


def draw_fingers(palm, fingers, ctx):
    cfg = palm_cfg(palm)
    for f in fingers:
        logger.debug('Drawing Finger: ' + repr(f))
        try:
            for s in finger_shapes.shapes_for(f, palm, cfg):
                s.draw(ctx)
        except InvalidFingerException as e:
            logger.debug(str(e))


def draw_hand(hand, ctx):
    logger.debug('Drawing Hand: ' + repr(hand))
    draw_palm(hand.palm, ctx)
    draw_fingers(hand.palm, hand.fingers, ctx)
