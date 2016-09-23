import math
import numpy as np
from . import hand_config
from .common import Ellipse
from .common import FilledArc
from .common import Line
from .common import car2pol
from .common import pol2car
from .common import norm_angle


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


def draw_demo_fingers(palm, ctx):
    palm_cfg = hand_config.palm_config(palm.palm_dir, palm.finger_dir)
    if not palm.dominant:
        palm_cfg = hand_config.mirror_palm_config(palm_cfg)
    v_finger, v_thumb, fill, v_fill_arc = palm_cfg

    diff_radians = find_diff_angle(v_thumb, v_finger)
    print("Diff: ", diff_radians)


def draw_orient_thumb(palm, ctx):
    palm_cfg = hand_config.palm_config(palm.palm_dir, palm.finger_dir)
    if not palm.dominant:
        palm_cfg = hand_config.mirror_palm_config(palm_cfg)
    v_finger, v_thumb, fill, v_fill_arc = palm_cfg
    #Line(0.0, 0.0, float(v_finger[0]), float(-v_finger[1])).draw(ctx)
    Line(0.0, 0.0, float(v_thumb[0]), float(-v_thumb[1]), color='red').draw(ctx)


def draw_test_fingers(palm, ctx):
    palm_cfg = hand_config.palm_config(palm.palm_dir, palm.finger_dir)
    if not palm.dominant:
        palm_cfg = hand_config.mirror_palm_config(palm_cfg)
    v_finger, v_thumb, fill, v_fill_arc = palm_cfg

    rx_palm = -1 * abs(v_finger[0] + v_thumb[0]) * hand_config.palm_size_ratio
    ry_palm = -1 * abs(v_finger[1] + v_thumb[1]) * hand_config.palm_size_ratio
    
    rx_fingers = -1 * abs(v_finger[0] + v_thumb[0])
    ry_fingers = -1 * abs(v_finger[1] + v_thumb[1])

    rho, phi = car2pol(np.array([v_finger[0], v_finger[1]]))
    phi = norm_angle(phi)

    finger_offsets = [-2 * math.pi / 11.0,
                      -math.pi / 11.0 / 2.0,
                      math.pi / 11.0 / 2.0,
                      2 * math.pi / 11.0]

    #finger_scales = [0.7, 0.8, 1.0, 0.9]
    finger_scales = [0.7, 0.85, 1.0, 0.85]
    if not is_offsets_reversed(v_finger, v_thumb):
        #finger_offsets = list(reversed(finger_offsets))
        finger_scales = list(reversed(finger_scales))

    finger_phis = [phi + theta for theta in finger_offsets]
    print(finger_phis)
    print(finger_scales)

    for theta, alpha in zip(finger_phis, finger_scales):
        print(theta, alpha)
        finger = Line(rx_palm * math.cos(theta),
                      ry_palm * math.sin(theta),
                      rx_fingers * math.cos(theta),
                      ry_fingers * math.sin(theta)).scale(alpha)

        print(str(finger))
        finger.draw(ctx)

    #thumb_phi = diff_radians / abs(diff_radians) * (math.pi * 110 / 180) + phi

    #thumb = Line(rx_palm * math.cos(thumb_phi),
                 #ry_palm * math.sin(thumb_phi),
                 #rx_fingers * math.cos(thumb_phi),
                 #ry_fingers * math.sin(thumb_phi)).scale(0.6)
    #thumb.draw(ctx)


def find_diff_angle(v1, v2):
    print (v1, v2)
    rho1, phi1 = car2pol(np.array([v1[0], v1[1]]))
    print(rho1, phi1)
    rho2, phi2 = car2pol(np.array([v2[0], v2[1]]))
    print(rho2, phi2)

    return phi2 - phi1


def is_offsets_reversed(v_finger, v_thumb):
    r_finger, p_finger = car2pol(np.array([v_finger[0], v_finger[1]]))
    r_thumb, p_thumb = car2pol(np.array([v_thumb[0], v_thumb[1]]))

    p_finger = norm_angle(p_finger)
    p_thumb = norm_angle(p_thumb)
    
    if equal_with_tol(p_finger, 0.0) and p_thumb < math.pi:
        return False
    if equal_with_tol(p_finger, 0.0) and p_thumb > math.pi:
        return True
    if equal_with_tol(p_thumb, 0.0) and p_finger > math.pi:
        return False
    delta_p = p_finger - p_thumb

    if delta_p < 0:
        return False
    return True


def equal_with_tol(a, b, tol=0.001):
    if abs(b - a) <= 0.001:
        return True
    return False
