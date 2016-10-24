import math
import numpy as np
import logging
from .palm_config import palm_cfg
from .palm_config import finger_shapes
from .common import Line


logger = logging.getLogger(__name__)


def draw_palm(palm, ctx):
    for s in palm_cfg.shapes_for(palm):
        s.draw(ctx)


def draw_orient_vectors(palm, ctx):
    cfg = palm_cfg(palm.palm_dir, palm.finger_dir)
    if not palm.dominant:
        cfg = palm_cfg.mirror_palm_config(cfg)
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
    cfg = palm_cfg(palm.palm_dir, palm.finger_dir)
    if not palm.dominant:
        cfg = palm_cfg.mirror_palm_config(cfg)
    v_finger, v_thumb, fill, v_fill_arc, transforms = cfg

    for f in fingers:
        shape = finger_shapes.shapes_for(f, cfg)
        shape.draw(ctx)


def draw_hand(hand, ctx):
    draw_palm(hand.palm, ctx)
    draw_fingers(hand.palm, hand.fingers, ctx)
