from ..model.palm import Orientation
from ..model.finger import FingerProperty
from ..model.finger import FingerIndex
from .common import angle_between
from .common import directed_angle
from .common import scale_matrix
from .common import rotation_matrix
from .common import is_counter_clockwise
from .common import pol2car
from .common import Line
from .common import Ellipse
import numpy as np
import math
from collections import namedtuple


HAND_MAJOR_RADIUS = 1.0
HAND_MINOR_RADIUS = 0.5
HAND_CIRCLE_RADIUS = 0.7071067811865476

# size of palm relative to size of whole hand
PALM_SIZE_RATIO = 0.5

PALM_MAJOR_RADIUS = HAND_MAJOR_RADIUS * PALM_SIZE_RATIO
PALM_MINOR_RADIUS = HAND_MINOR_RADIUS * PALM_SIZE_RATIO
PALM_CIRCLE_RADIUS = HAND_CIRCLE_RADIUS * PALM_SIZE_RATIO


class PalmConfigs:
    
    FORWARD = Orientation.FORWARD
    BODY = Orientation.BODY
    UP = Orientation.UP
    DOWN = Orientation.DOWN
    IN = Orientation.IN
    OUT = Orientation.OUT

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


    '''A Palm Configuration'''
    _PalmConfig = namedtuple('_PalmConfig', ['v_finger',
                                             'v_thumb',
                                             'fill',
                                             'v_filled_arc',
                                             'transforms'])
    def __init__(self):
        super().__init__()
        self._palm_configs = None

    def __call__(self, o_finger, o_thumb):
        return self.palm_configs[(o_finger, o_thumb)]

    @property
    def palm_configs(self):
        if self._palm_configs is None:
            self._palm_configs = self.gen_palm_configs()
        return self._palm_configs

    def should_mirror(self, v_finger, v_thumb):
        return not is_counter_clockwise(v_finger, v_thumb)

    def finger_rotation(self, vf1, vf2):
        return directed_angle(vf1, vf2)

    def gen_palm_config(self, p_config):
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

        if self.should_mirror(v_finger, v_thumb):
            transforms.append(scale_matrix(-1.0, 1.0))
        else:
            transforms.append(scale_matrix(1.0, 1.0))

        transforms.append(self.get_palm_scale_matrix(v_f, v_t))
        transforms.append(rotation_matrix(self.finger_rotation(self.NORTH,
                                                               v_finger)))

        return self._PalmConfig(v_f, v_t, fill, v_a, transforms)

    def get_palm_scale_matrix(self, v_f, v_t):
        rx = abs(v_f[0] + v_t[0])
        ry = abs(v_f[1] + v_t[1])

        return np.array([[rx / PALM_CIRCLE_RADIUS, 0.0,],
                         [0.0, ry / PALM_CIRCLE_RADIUS]])

    def gen_palm_configs(self):
        configs = {}
        for o, raw_config in self.PALM_CONFIGS.items():
            configs[o] = self.gen_palm_config(raw_config)

        return configs

    def mirror_palm_config(self, cfg):
        mirror = np.array([[-1.0, 0.0],
                           [0.0, 1.0]])

        v_arc = None
        if cfg.v_filled_arc is not None:
            v_arc = mirror.dot(cfg.v_filled_arc)

        transforms = list(cfg.transforms)
        transforms[0] = mirror.dot(transforms[0])
        transforms[2] = transforms[2].T

        return self._PalmConfig(mirror.dot(cfg.v_finger),
                                mirror.dot(cfg.v_thumb),
                                cfg.fill,
                                v_arc,
                                transforms)


'''
Access shapes for a single finger, based on a palm_config

Configuration is bases on a set of vectors (anchors) with define finger shapes
for the Dfu palm config.  The vectors can be transformed to be used every
palm configuration.
'''
class FingerShapes(object):
    P_STRA = FingerProperty.STRAIGHT
    P_SPRE = FingerProperty.SPREAD
    P_ROUN = FingerProperty.ROUND
    P_BEND = FingerProperty.BENT
    P_FOLD = FingerProperty.FOLDED
    P_CONT = FingerProperty.CONTACT
    P_TAPE = FingerProperty.TAPER
    P_X    = FingerProperty.X
    P_TOGE = FingerProperty.TOGETHER
    
    FOLDED_START_RADIUS = PALM_CIRCLE_RADIUS * 0.9
    FOLDED_END_RADIUS = PALM_CIRCLE_RADIUS * 1.1
    FINGER_SCALES = [1.0, 0.85, 1.0, 0.85, 0.7]
    FINGER_START_PHIS = [5.39307, 0.76794, 1.34390, 1.90241, 2.44346]
    SPLAY_END_PHIS = [6.15228, 0.87266, 1.32645, 1.88495, 2.43473]
    FINGER_LENGTHS = [HAND_CIRCLE_RADIUS * a for a in FINGER_SCALES]

    FINGER_STARTS = [np.array(pol2car(PALM_CIRCLE_RADIUS, t))
                     for t in FINGER_START_PHIS]
    SPLAY_ENDS = [np.array(pol2car(r, t))
                  for r, t in zip(FINGER_LENGTHS, SPLAY_END_PHIS)]
    STRAIGHT_ENDS = []
    for s, l in zip(FINGER_STARTS, FINGER_LENGTHS):
        STRAIGHT_ENDS.append(np.array([s[0], l]))

    STRAIGHT_ENDS[0] = np.array([PALM_CIRCLE_RADIUS + 0.08, 0.3])
    STRAIGHT_THUMB_START = np.array(pol2car(PALM_CIRCLE_RADIUS, 2 * math.pi))

    def __init__(self):
        super().__init__()

    def shapes_for(self, finger, palm_cfg):
        index, features = finger.index, finger.properties
        if set([self.P_STRA, self.P_TOGE]) == finger.properties:
            start = self.FINGER_STARTS[index.value]
            if index == FingerIndex.THUMB:
                start = self.STRAIGHT_THUMB_START
            end = self.STRAIGHT_ENDS[index.value]
            start, end = self.transform_anchors([start, end], palm_cfg)
            return Line(start[0], start[1], end[0], end[1])

        elif set([self.P_STRA, self.P_SPRE]) == finger.properties:
            start = self.FINGER_STARTS[index.value]
            end = self.SPLAY_ENDS[index.value]
            start, end = self.transform_anchors([start, end], palm_cfg)
            return Line(start[0], start[1], end[0], end[1])

    def transform_anchors(self, anchors, palm_config):
        anchors_prime = []
        for a in anchors:
            a_p = np.array([a[0], a[1]])
            mirror = palm_config.transforms[0]
            scale  = palm_config.transforms[1]
            rotate = palm_config.transforms[2]
            a_p = mirror.dot(a_p)
            a_p = rotate.dot(a_p)
            a_p = scale.dot(a_p)
            a_p = np.array([[1.0, 0.0],
                            [0.0, -1.0]]).dot(a_p)
            anchors_prime.append(a_p)
        return anchors_prime


palm_cfg = PalmConfigs()
finger_shapes = FingerShapes()
