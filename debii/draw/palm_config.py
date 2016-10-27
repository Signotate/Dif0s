from ..model.palm import Orientation
from .common import directed_angle
from .common import scale_matrix
from .common import rotation_matrix
from .common import is_counter_clockwise
from .common import car2pol
from .common import norm_angle
from .common import Ellipse
from .common import FilledArc
from .hand_config import *
import numpy as np
from collections import namedtuple
import logging


logger = logging.getLogger(__name__)


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

    def __call__(self, palm):
        cfg = self.palm_configs[(palm.palm_dir, palm.finger_dir)]
        if not palm.dominant:
            cfg = self.mirror_palm_config(cfg)
        return cfg

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

    def shapes_for(self, palm):
        cfg = self(palm)
        logger.debug('Getting shapes for: ' + str(cfg))
        v_finger, v_thumb, fill, v_fill_arc, _ = cfg

        rx = v_finger[0] + v_thumb[0]
        ry = v_finger[1] + v_thumb[1]

        palm_shapes = []
        palm_shapes.append(Ellipse(0.0, 0.0, float(rx), float(ry), fill))

        if v_fill_arc is not None:
            rho, phi = car2pol(np.array([v_fill_arc[0], v_fill_arc[1]]))
            phi = norm_angle(phi)
            logger.debug('Getting half filled arc with phi: ' + str(phi))
            if np.isclose(phi, 0.0):
                phi += 2 * np.pi
            start_angle = phi - np.pi / 2.0
            end_angle = phi + np.pi / 2.0

            if start_angle == np.pi or start_angle == 2 * np.pi:
                start_angle, end_angle = end_angle, start_angle
            if v_fill_arc[0] == 0.0 and v_fill_arc[1] > 0.0:
                start_angle, end_angle = -np.pi, 0.0

            logger.debug("Filled arc angles:" +
                         str(start_angle / np.pi) + ', ' +
                         str(end_angle / np.pi))

            palm_shapes.append(
                FilledArc(0.0,
                          0.0,
                          float(abs(rx)),
                          float(abs(ry)),
                          start_angle,
                          end_angle))

        return palm_shapes
