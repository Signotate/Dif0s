'''Configuration for a hand'''

from ..model.palm import Orientation
from collections import namedtuple
import numpy as np


''' basic configuration constants'''
major_radius = 1
minor_radius = 0.5


# sqrt(1/2)
circle_radius = 0.7071067811865476


palm_size_ratio = 0.5


# convenience constants
__FORWARD = Orientation.FORWARD
__BODY = Orientation.BODY
__UP = Orientation.UP
__DOWN = Orientation.DOWN
__IN = Orientation.IN
__OUT = Orientation.OUT


_PalmConfig = namedtuple('_PalmConfig', ['finger_vector', 'thumb_vector',
                                         'fill', 'filled_arc_vector'])


'''dictionary of palms and there basic configuration'''
palm_configs = {(__FORWARD, __UP): _PalmConfig((0.0, circle_radius),
                                               (circle_radius, 0.0),
                                               False,
                                               None),
                (__FORWARD, __DOWN): _PalmConfig((0.0, -circle_radius),
                                                 (-circle_radius, 0.0),
                                                 False,
                                                 None),
                (__FORWARD, __IN): _PalmConfig((circle_radius, 0.0),
                                               (0.0, -circle_radius),
                                               False,
                                               None),
                (__FORWARD, __OUT): _PalmConfig((-circle_radius, 0.0),
                                                (0.0, circle_radius),
                                                False,
                                                None),

                (__BODY, __UP): _PalmConfig((0.0, circle_radius),
                                            (-circle_radius, 0.0),
                                            True,
                                            None),
                (__BODY, __DOWN): _PalmConfig((0.0, -circle_radius),
                                              (circle_radius, 0.0),
                                              True,
                                              None),
                (__BODY, __IN): _PalmConfig((circle_radius, 0.0),
                                            (0.0, circle_radius),
                                            True,
                                            None),
                (__BODY, __OUT): _PalmConfig((-circle_radius, 0.0),
                                             (0.0, -circle_radius),
                                             True,
                                             None),

                (__IN, __UP): _PalmConfig((0.0, major_radius),
                                          (-minor_radius, 0.0),
                                          False,
                                          (-minor_radius, 0.0)),
                (__IN, __DOWN): _PalmConfig((0.0, -major_radius),
                                            (-minor_radius, 0.0),
                                            False,
                                            (-minor_radius, 0.0)),
                (__IN, __FORWARD): _PalmConfig((minor_radius, 0.0),
                                               (0.0, major_radius),
                                               False,
                                               (-minor_radius, 0.0)),
                (__IN, __BODY): _PalmConfig((minor_radius, 0.0),
                                            (0.0, -major_radius),
                                            False,
                                            (-minor_radius, 0.0)),

                (__OUT, __UP): _PalmConfig((0.0, major_radius),
                                           (minor_radius, 0.0),
                                           True,
                                           None),
                (__OUT, __DOWN): _PalmConfig((0.0, -major_radius),
                                             (minor_radius, 0.0),
                                             True,
                                             None),
                (__OUT, __FORWARD): _PalmConfig((-minor_radius, 0.0),
                                                (0.0, -major_radius),
                                                True,
                                                None),
                (__OUT, __BODY): _PalmConfig((minor_radius, 0.0),
                                             (0.0, major_radius),
                                             True,
                                             None),

                (__UP, __IN): _PalmConfig((major_radius, 0.0),
                                          (0.0, -minor_radius),
                                          False,
                                          (0.0, -minor_radius)),
                (__UP, __OUT): _PalmConfig((-major_radius, 0.0),
                                           (0.0, minor_radius),
                                           False,
                                           (0.0, -minor_radius)),
                (__UP, __FORWARD): _PalmConfig((0.0, -minor_radius),
                                               (-major_radius, 0.0),
                                               False,
                                               None),
                (__UP, __BODY): _PalmConfig((0.0, minor_radius),
                                            (major_radius, 0.0),
                                            False,
                                            None),

                (__DOWN, __IN): _PalmConfig((major_radius, 0.0),
                                            (0.0, minor_radius),
                                            False,
                                            (0.0, minor_radius)),
                (__DOWN, __OUT): _PalmConfig((-major_radius, 0.0),
                                             (0.0, -minor_radius),
                                             False,
                                             (0.0, minor_radius)),
                (__DOWN, __FORWARD): _PalmConfig((0.0, -minor_radius),
                                                 (minor_radius, 0.0),
                                                 True,
                                                 None),
                (__DOWN, __BODY):  _PalmConfig((0.0, minor_radius),
                                               (-major_radius, 0.0),
                                               True,
                                               None)}


def palm_config(palm_dir, finger_dir):
    '''Get the palm config for an orientation pair'''
    return palm_configs.get((palm_dir, finger_dir), None)


def mirror_palm_config(palm_cfg):
    v_mirror = np.array((-1, 1))
    v_finger = tuple(np.array(palm_cfg.finger_vector) * v_mirror)
    v_thumb = tuple(np.array(palm_cfg.thumb_vector) * v_mirror)

    v_arc = None
    if palm_cfg.filled_arc_vector is not None:
        v_arc = tuple(np.array(palm_cfg.filled_arc_vector) * v_mirror)

    return _PalmConfig(v_finger, v_thumb, palm_cfg.fill, v_arc)
