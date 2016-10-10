from ..model.palm import Orientation
from .common import angle_between
from .common import directed_angle
from .common import scale_matrix
from .common import rotation_matrix
from .common import directed_angle
from .common import is_counter_clockwise
import numpy as np
import math
from collections import namedtuple


FORWARD = Orientation.FORWARD
BODY = Orientation.BODY
UP = Orientation.UP
DOWN = Orientation.DOWN
IN = Orientation.IN
OUT = Orientation.OUT


HAND_MAJOR_RADIUS = 1.0
HAND_MINOR_RADIUS = 0.5
HAND_CIRCLE_RADIUS = 0.7071067811865476


# size of palm relative to size of whole hand
PALM_SIZE_RATIO = 0.5


PALM_MAJOR_RADIUS = HAND_MAJOR_RADIUS * PALM_SIZE_RATIO
PALM_MINOR_RADIUS = HAND_MINOR_RADIUS * PALM_SIZE_RATIO
PALM_CIRCLE_RADIUS = HAND_CIRCLE_RADIUS * PALM_SIZE_RATIO


'''Orientation vectors'''
NORTH = np.array([0.0, 1.0])
SOUTH = np.array([0.0, -1.0])
EAST = np.array([1.0, 0.0])
WEST = np.array([-1.0, 0.0])


'''
Map of palm configs (dominant only)
(palm_direction, finger_direction) -> (finger_direction, 
                                       thumb_direction,
                                       filled,
                                       half_filled_direction,
                                       finger_radius)
'''
PALM_CONFIGS = {}
PALM_CONFIGS[(FORWARD, UP)] = (NORTH, EAST, False, None, PALM_CIRCLE_RADIUS)
PALM_CONFIGS[(FORWARD, DOWN)] = (SOUTH, WEST, False, None, PALM_CIRCLE_RADIUS)
PALM_CONFIGS[(FORWARD, IN)] = (EAST, SOUTH, False, None, PALM_CIRCLE_RADIUS)
PALM_CONFIGS[(FORWARD, OUT)] = (WEST, NORTH, False, None, PALM_CIRCLE_RADIUS)


PALM_CONFIGS[(BODY, UP)] = (NORTH, WEST, True, None, PALM_CIRCLE_RADIUS)
PALM_CONFIGS[(BODY, DOWN)] = (SOUTH, EAST, True, None, PALM_CIRCLE_RADIUS)
PALM_CONFIGS[(BODY, IN)] = (EAST, NORTH, True, None, PALM_CIRCLE_RADIUS)
PALM_CONFIGS[(BODY, OUT)] = (WEST, SOUTH, True, None, PALM_CIRCLE_RADIUS)


PALM_CONFIGS[(IN, UP)] = (NORTH, WEST, False, WEST, PALM_MAJOR_RADIUS)
PALM_CONFIGS[(IN, DOWN)] = (SOUTH, WEST, False, WEST, PALM_MAJOR_RADIUS)
PALM_CONFIGS[(IN, FORWARD)] = (EAST, NORTH, False, WEST, PALM_MINOR_RADIUS)
PALM_CONFIGS[(IN, BODY)] = (EAST, SOUTH, False, WEST, PALM_MINOR_RADIUS)


PALM_CONFIGS[(OUT, UP)] = (NORTH, EAST, True, None, PALM_MAJOR_RADIUS)
PALM_CONFIGS[(OUT, DOWN)] = (SOUTH, EAST, True, None, PALM_MAJOR_RADIUS)
PALM_CONFIGS[(OUT, FORWARD)] = (WEST, SOUTH, True, None, PALM_MINOR_RADIUS)
PALM_CONFIGS[(OUT, BODY)] = (EAST, NORTH, True, None, PALM_MINOR_RADIUS)


PALM_CONFIGS[(UP, IN)] = (EAST, SOUTH, False, SOUTH, PALM_MAJOR_RADIUS)
PALM_CONFIGS[(UP, OUT)] = (WEST, NORTH, False, SOUTH, PALM_MAJOR_RADIUS)
PALM_CONFIGS[(UP, FORWARD)] = (SOUTH, WEST, False, None, PALM_MINOR_RADIUS)
PALM_CONFIGS[(UP, BODY)] = (NORTH, EAST, False, None, PALM_MINOR_RADIUS)


PALM_CONFIGS[(DOWN, IN)] = (EAST, NORTH, False, NORTH, PALM_MAJOR_RADIUS)
PALM_CONFIGS[(DOWN, OUT)] = (WEST, SOUTH, False, NORTH, PALM_MAJOR_RADIUS)
PALM_CONFIGS[(DOWN, FORWARD)] = (SOUTH, EAST, True, None, PALM_MINOR_RADIUS)
PALM_CONFIGS[(DOWN, BODY)] = (NORTH, WEST, True, None, PALM_MINOR_RADIUS)


'''Generate palm configs'''
_PalmConfig = namedtuple('_PalmConfig', ['v_finger',
                                         'v_thumb',
                                         'fill',
                                         'v_filled_arc',
                                         'transforms'])


#ROTATIONS = {(NORTH, EAST) : 0.0,
             #(NORTH, WEST) : 0.0,
             #(SOUTH, EAST) : math.pi,
             #(SOUTH, WEST) : math.pi,
             #(EAST, NORTH) : -math.pi / 2.0,
             #(EAST, SOUTH) : -math.pi / 2.0,
             #(WEST, NORTH) : math.pi / 2.0,
             #(WEST, SOUTH) : math.pi / 2.0
            #}
#
#
#MIRROR = {(NORTH, EAST) : False,
          #(NORTH, WEST) : True,
          #(SOUTH, EAST) : True,
          #(SOUTH, WEST) : False,
          #(EAST, NORTH) : True,
          #(EAST, SOUTH) : False,
          #(WEST, NORTH) : False,
          #(WEST, SOUTH) : True
         #}


def should_mirror(v_finger, v_thumb):
    return not is_counter_clockwise(v_finger, v_thumb)


def finger_rotation(vf1, vf2):
    return directed_angle(vf1, vf2)


def gen_palm_config(p_config):
    v_finger, v_thumb, fill, v_arc, r_finger = p_config

    r_thumb = PALM_CIRCLE_RADIUS
    if r_finger == PALM_MINOR_RADIUS:
        r_thumb = PALM_MAJOR_RADIUS
    elif r_finger == PALM_MAJOR_RADIUS:
        r_thumb = PALM_MINOR_RADIUS

    v_f = v_finger * r_finger
    v_t = v_thumb * r_thumb
    v_a = None
    if v_arc is not None:
        v_a = v_arc * r_thumb

    transforms = []

    if should_mirror(v_finger, v_thumb):
        #transforms.append(scale_matrix(-1.0, 1.0))
        transforms.append(True)
    else:
        transforms.append(False)

    #transforms.append(rotation_matrix(finger_rotation(v_finger, v_thumb)))
    transforms.append(finger_rotation(v_finger, NORTH))
    #transforms.append(get_palm_scale_matrix(v_finger, v_thumb))

    return _PalmConfig(v_f, v_t, fill, v_a, transforms)


def get_palm_scale_matrix(v_f, v_t):
    rx = abs(v_f[0] + v_t[0])
    ry = abs(v_f[1] + v_t[1])

    return np.array([[rx / PALM_CIRCLE_RADIUS, 0.0,],
                     [0.0, ry / PALM_CIRCLE_RADIUS]])


def gen_palm_configs():
    configs = {}
    for o, raw_config in PALM_CONFIGS.items():
        configs[o] = gen_palm_config(raw_config)

    return configs


def mirror_palm_config(cfg):
    mirror = np.array([[-1.0, 0.0],
                       [0.0, 1.0]])

    v_arc = None
    if cfg.v_filled_arc is not None:
        v_arc = mirror.dot(cfg.v_filled_arc)

    return _PalmConfig(mirror.dot(cfg.v_finger),
                       mirror.dot(cfg.v_thumb),
                       cfg.fill,
                       v_arc,
                       [mirror] + cfg.transforms)


_palm_configs = gen_palm_configs()


def cfg(o_finger, o_thumb):
    return _palm_configs[(o_finger, o_thumb)]


if __name__ == '__main__':
    for k, c in _palm_configs.items():
        print(k, '=>', c)
