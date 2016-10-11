import math
import numpy as np
from .palm_config import palm_cfg
from .palm_config import anchors
from .common import Ellipse
from .common import FilledArc
from .common import Line
from .common import car2pol
from .common import pol2car
from .common import norm_angle
from .common import equal_with_tol


def draw_palm(palm, ctx):
    cfg = palm_cfg(palm.palm_dir, palm.finger_dir)
    if not palm.dominant:
        cfg = palm_cfg.mirror_palm_config(cfg)
    print(cfg)
    v_finger, v_thumb, fill, v_fill_arc, _ = cfg

    rx = v_finger[0] + v_thumb[0]
    ry = v_finger[1] + v_thumb[1]

    Ellipse(0.0, 0.0, float(rx), float(ry), fill).draw(ctx)

    if v_fill_arc is not None:
        rho, phi = car2pol(np.array([v_fill_arc[0], v_fill_arc[1]]))
        phi = norm_angle(phi)
        print("norm arc phi:", phi)
        if equal_with_tol(phi, 0.0):
            phi += 2 * math.pi
        start_angle = phi - math.pi / 2.0
        end_angle = phi + math.pi / 2.0
        #if equal_with_tol(end_angle, 0.0):
            #end_angle += 2 * math.pi
        #print("arc:", start_angle / math.pi, end_angle / math.pi)
        #if ((start_angle < 0 or end_angle < 0) and
                #(start_angle >= 0 or end_angle >= 0)):

        if start_angle == math.pi or start_angle == 2 * math.pi:
            start_angle, end_angle = end_angle, start_angle
        if v_fill_arc[0] == 0.0 and v_fill_arc[1] > 0.0:
            start_angle, end_angle = -math.pi, 0.0

        print("arc angles:", start_angle / math.pi, end_angle / math.pi)

        FilledArc(0.0, 0.0, float(abs(rx)), float(abs(ry)), start_angle,
                  end_angle).draw(ctx)


def draw_orient_vectors(palm, ctx):
    cfg = palm_cfg(palm.palm_dir, palm.finger_dir)
    if not palm.dominant:
        cfg = palm_cfg.mirror_palm_config(cfg)
    v_finger, v_thumb, fill, v_fill_arc, _ = cfg
    Line(0.0, 0.0, float(v_finger[0]), float(-v_finger[1]), color='green').draw(ctx)
    Line(0.0, 0.0, float(v_thumb[0]), float(-v_thumb[1]), color='red').draw(ctx)


def draw_test_fingers(palm, ctx):
    cfg = palm_cfg(palm.palm_dir, palm.finger_dir)
    if not palm.dominant:
        cfg = palm_cfg.mirror_palm_config(cfg)
    v_finger, v_thumb, fill, v_fill_arc, transforms = cfg

    v_starts = []
    for v in anchors.BASE_ANCHORS[anchors.FINGER_STARTS]:
        for trans in transforms:
            v = trans.dot(v)

        v = np.array([[1.0, 0.0],
                      [0.0, -1.0]]).dot(v)

        v_starts.append(v)
    v_starts[0] = anchors.BASE_ANCHORS[anchors.STRAIGHT_THUMB_START]

    v_ends = []
    for v in anchors.BASE_ANCHORS[anchors.STRAIGHT_ENDS]:
        for trans in transforms:
            v = trans.dot(v)

        v = np.array([[1.0, 0.0],
                      [0.0, -1.0]]).dot(v)

        v_ends.append(v)

    for v, u in zip(v_starts, v_ends):
        Line(v[0], v[1], u[0], u[1]).draw(ctx)
