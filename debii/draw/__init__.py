import math
import numpy as np
from . import hand_config
from .common import Ellipse
from .common import FilledArc
from .common import Line
from .common import car2pol


def draw_hand(hand, ctx):
    pass


def draw_palm(palm, ctx):
    palm_cfg = hand_config.palm_config(palm.palm_dir, palm.finger_dir)
    if not palm.dominant:
        palm_cfg = hand_config.mirror_palm_config(palm_cfg)
    print(palm_cfg)
    v_finger, v_thumb, fill, v_fill_arc = palm_cfg

    rx = (v_finger[0] + v_thumb[0]) * hand_config.palm_size_ratio
    ry = (v_finger[1] + v_thumb[1]) * hand_config.palm_size_ratio

    Ellipse(0.0, 0.0, float(rx), float(ry), fill).draw(ctx)

    if v_fill_arc is not None:
        rho, phi = car2pol(np.array(v_fill_arc))
        start_angle = -phi + math.pi / 2.0
        end_angle = -phi - math.pi / 2.0
        print(start_angle / math.pi, end_angle / math.pi)
        if ((start_angle < 0 or end_angle < 0) and
                (start_angle >= 0 or end_angle >= 0)):

            if start_angle > end_angle:
                start_angle, end_angle = end_angle, start_angle

        print(start_angle / math.pi, end_angle / math.pi)

        FilledArc(0.0, 0.0, float(rx), float(ry), start_angle,
                  end_angle).draw(ctx)


def draw_orient_vectors(palm, ctx):
    palm_cfg = hand_config.palm_config(palm.palm_dir, palm.finger_dir)
    if not palm.dominant:
        palm_cfg = hand_config.mirror_palm_config(palm_cfg)
    v_finger, v_thumb, fill, v_fill_arc = palm_cfg
    Line(0.0, 0.0, float(v_finger[0]), float(-v_finger[1])).draw(ctx)
    Line(0.0, 0.0, float(v_thumb[0]), float(-v_thumb[1]), color='red').draw(ctx)
