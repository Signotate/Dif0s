import math
import numpy as np
import logging
from .palm_config import palm_cfg
from .palm_config import finger_shapes
from .common import Line


logger = logging.getLogger(__name__)


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
        for s in finger_shapes.shapes_for(f, cfg):
            s.draw(ctx)


def draw_hand(hand, ctx):
    logger.debug('Drawing Hand: ' + repr(hand))
    draw_palm(hand.palm, ctx)
    draw_fingers(hand.palm, hand.fingers, ctx)
