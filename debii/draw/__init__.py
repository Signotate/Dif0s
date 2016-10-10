import math
import numpy as np
from . import hand_config
from . import palm_config
from .common import Ellipse
from .common import FilledArc
from .common import Line
from .common import car2pol
from .common import pol2car
from .common import norm_angle
from .common import equal_with_tol
from .hand_config import finger_phi


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
        rho, phi = car2pol(np.array([v_fill_arc[0], v_fill_arc[1]]))
        phi = norm_angle(phi)
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

        print("arc angles:", start_angle / math.pi, end_angle / math.pi)

        FilledArc(0.0, 0.0, float(abs(rx)), float(abs(ry)), start_angle,
                  end_angle).draw(ctx)


def draw_palm2(palm, ctx):
    palm_cfg = palm_config.cfg(palm.palm_dir, palm.finger_dir)
    if not palm.dominant:
        palm_cfg = palm_config.mirror_palm_config(palm_cfg)
    print(palm_cfg)
    v_finger, v_thumb, fill, v_fill_arc, _ = palm_cfg

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


def draw_orient_vectors2(palm, ctx):
    palm_cfg = palm_config.cfg(palm.palm_dir, palm.finger_dir)
    if not palm.dominant:
        palm_cfg = palm_config.mirror_palm_config(palm_cfg)
    v_finger, v_thumb, fill, v_fill_arc, _ = palm_cfg
    Line(0.0, 0.0, float(v_finger[0]), float(-v_finger[1]), color='green').draw(ctx)
    Line(0.0, 0.0, float(v_thumb[0]), float(-v_thumb[1]), color='red').draw(ctx)


def draw_orient_vectors(palm, ctx):
    palm_cfg = hand_config.palm_config(palm.palm_dir, palm.finger_dir)
    if not palm.dominant:
        palm_cfg = hand_config.mirror_palm_config(palm_cfg)
    v_finger, v_thumb, fill, v_fill_arc = palm_cfg
    Line(0.0, 0.0, float(v_finger[0]), float(-v_finger[1])).draw(ctx)
    Line(0.0, 0.0, float(v_thumb[0]), float(-v_thumb[1]), color='red').draw(ctx)


def draw_orient_thumb(palm, ctx):
    palm_cfg = hand_config.palm_config(palm.palm_dir, palm.finger_dir)
    if not palm.dominant:
        palm_cfg = hand_config.mirror_palm_config(palm_cfg)
    v_finger, v_thumb, fill, v_fill_arc = palm_cfg
    Line(0.0, 0.0, float(v_finger[0]), float(-v_finger[1])).draw(ctx)
    Line(0.0, 0.0, float(v_thumb[0]), float(-v_thumb[1]), color='red').draw(ctx)


def draw_test_fingers(palm, ctx):
    palm_cfg = hand_config.palm_config(palm.palm_dir, palm.finger_dir)
    if not palm.dominant:
        palm_cfg = hand_config.mirror_palm_config(palm_cfg)
    v_finger, v_thumb, fill, v_fill_arc = palm_cfg

    rx_palm = (v_finger[0] + v_thumb[0]) * hand_config.palm_size_ratio
    ry_palm = (v_finger[1] + v_thumb[1]) * hand_config.palm_size_ratio

    rx_fingers = (v_finger[0] + v_thumb[0])
    ry_fingers = (v_finger[1] + v_thumb[1])

    base_scales = [0.85, 1.0, 0.85, 0.7]

    for theta, alpha in zip(get_finger_phis(palm_cfg), base_scales):
        finger = Line(abs(rx_palm) * math.cos(theta),
                      -1 * abs(ry_palm) * math.sin(theta),
                      abs(rx_fingers) * math.cos(theta),
                      -1 * abs(ry_fingers) * math.sin(theta)).scale(alpha)

        finger.draw(ctx)

    r_finger, p_finger = car2pol(np.array([v_finger[0], v_finger[1]]))
    r_thumb, p_thumb = car2pol(np.array([v_thumb[0], v_thumb[1]]))

    p_finger = norm_angle(p_finger)
    p_thumb = norm_angle(p_thumb)

    # draw thumb
    tp_start, tp_stop = get_thumb_phis(v_finger, v_thumb)
    thumb = Line(abs(rx_palm) * math.cos(tp_start),
                 -1 * abs(ry_palm) * math.sin(tp_start),
                 abs(rx_fingers) * 0.8 * math.cos(tp_stop),
                 -1 * abs(ry_fingers) * 0.8 * math.sin(tp_stop))
    
    thumb.draw(ctx)

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




def get_finger_phis(palm_config):
    return [finger_phi(palm_config, i) for i in range(1, 5)]


def get_thumb_phis(v_finger, v_thumb):
    p_finger, p_thumb = get_orient_phis(v_finger, v_thumb)

    delta_thumb = math.pi / 6.0

    d_a = abs(norm_angle(p_thumb - delta_thumb) - p_finger)
    d_b = abs(norm_angle(p_thumb + delta_thumb) - p_finger)

    #if d_a < d_b:
        #return norm_angle(p_thumb + 1.9 * delta_thumb), norm_angle(p_thumb - delta_thumb)
    #return norm_angle(p_thumb - 1.9 * delta_thumb), norm_angle(p_thumb + delta_thumb)

    if d_a < d_b:
        return norm_angle(p_thumb + 1.9 * delta_thumb), p_thumb
    return norm_angle(p_thumb - 1.9 * delta_thumb), p_thumb


def get_orient_phis(v_finger, v_thumb):
    r_finger, p_finger = car2pol(np.array([v_finger[0], v_finger[1]]))
    r_thumb, p_thumb = car2pol(np.array([v_thumb[0], v_thumb[1]]))

    p_finger = norm_angle(p_finger)
    p_thumb = norm_angle(p_thumb)

    if equal_with_tol(p_finger, 0.0):
        p_finger += 2 * math.pi
    if equal_with_tol(p_thumb, 0.0):
        p_thumb += 2 * math.pi

    while p_thumb > p_finger and abs(p_thumb - p_finger) > math.pi / 2.0:
        p_thumb -= 2 * math.pi
    while p_thumb < p_finger and abs(p_thumb - p_finger) > math.pi / 2.0:
        p_finger -= 2 * math.pi

    return p_finger, p_thumb
