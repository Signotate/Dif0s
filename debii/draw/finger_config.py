from ..model.finger import FingerProperty
from ..model.finger import FingerIndex
from .common import pol2car
from .common import Line
from .common import Ellipse
from .hand_config import *
import numpy as np
import logging


logger = logging.getLogger(__name__)


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
    

    def __init__(self):
        super().__init__()

        self.FOLDED_START_RADIUS = PALM_CIRCLE_RADIUS * 0.8
        self.FOLDED_END_RADIUS = PALM_CIRCLE_RADIUS * 1.2

        self.FOLDED_THUMB_END = np.array([0.05, -0.05])
        self.FINGER_SCALES = [1.0, 0.85, 1.0, 0.85, 0.7]
        self.FINGER_START_PHIS = [5.39307, 0.76794, 1.34390, 1.90241, 2.44346]
        self.SPLAY_END_PHIS = [6.15228, 0.87266, 1.32645, 1.88495, 2.43473]
        self.FINGER_LENGTHS = [HAND_CIRCLE_RADIUS * a 
                               for a in self.FINGER_SCALES]

        self.FINGER_STARTS = [np.array(pol2car(PALM_CIRCLE_RADIUS, t))
                              for t in self.FINGER_START_PHIS]
        
        self.SPLAY_ENDS = []
        for r, t, in zip(self.FINGER_LENGTHS, self.SPLAY_END_PHIS):
            self.SPLAY_ENDS.append(np.array(pol2car(r, t)))

        self.STRAIGHT_ENDS = []
        for s, l in zip(self.FINGER_STARTS, self.FINGER_LENGTHS):
            self.STRAIGHT_ENDS.append(np.array([s[0], l]))
        self.STRAIGHT_ENDS[0] = np.array([PALM_CIRCLE_RADIUS + 0.08, 0.3])
        self.STRAIGHT_THUMB_START = np.array(pol2car(PALM_CIRCLE_RADIUS, 2 * np.pi))

        self.FOLDED_STARTS = [np.array(pol2car(self.FOLDED_START_RADIUS, phi)) 
                              for phi in self.FINGER_START_PHIS]
        self.FOLDED_ENDS = [np.array(pol2car(self.FOLDED_END_RADIUS, phi))
                            for phi in self.FINGER_START_PHIS]

        self.ROUND_END_R = 0.49
        self.ROUND_SP_END_R = 0.6
        self.ROUND_STRA_R = 0.12
        self.ROUND_SPRE_R = 0.09
        self.ROUND_T_PHI = 5.48731
        self.ROUND_T_LEN = 0.5
        self.ROUND_SCALES = [1.0, 0.92, 0.93, 0.92, 0.87]
        self.ROUND_LENS = [self.ROUND_END_R * s for s in self.ROUND_SCALES]
        self.ROUND_TOGETHER_POS = []
        for s, l in zip(self.FINGER_STARTS, self.ROUND_LENS):
            self.ROUND_TOGETHER_POS.append(np.array([s[0], l]))
        self.ROUND_TOGETHER_POS[0] = np.array(pol2car(self.ROUND_T_LEN,
                                                      self.ROUND_T_PHI))
        self.ROUND_SPREAD_POS = []
        for t, s in zip(self.FINGER_START_PHIS, self.ROUND_SCALES):
            self.ROUND_SPREAD_POS.append(pol2car(self.ROUND_SP_END_R * s, t))
        self.ROUND_SPREAD_POS[0] = np.array(pol2car(self.ROUND_T_LEN,
                                                    self.ROUND_T_PHI))

    def shapes_for(self, finger, palm_cfg):
        index, features = finger.index, finger.properties
        if set([self.P_STRA, self.P_TOGE]) == finger.properties:
            start = self.FINGER_STARTS[index.value]
            if index == FingerIndex.THUMB:
                start = self.STRAIGHT_THUMB_START
            end = self.STRAIGHT_ENDS[index.value]
            start, end = self.transform_anchors([start, end], palm_cfg)
            return [Line(start[0], start[1], end[0], end[1])]

        elif set([self.P_STRA, self.P_SPRE]) == finger.properties:
            start = self.FINGER_STARTS[index.value]
            end = self.SPLAY_ENDS[index.value]
            start, end = self.transform_anchors([start, end], palm_cfg)
            return [Line(start[0], start[1], end[0], end[1])]
        elif set([self.P_FOLD]) == finger.properties:
            start = self.FOLDED_STARTS[index.value]
            end = self.FOLDED_ENDS[index.value]
            color = 'black'
            if index == FingerIndex.THUMB:
                start = self.FINGER_STARTS[0]
                end = self.FOLDED_THUMB_END
                if self.is_finger_white(finger, palm_cfg):
                    logger.debug('Drawing folded Thumb: Thumb is white')
                    color = 'white'

            start, end = self.transform_anchors([start, end], palm_cfg)

            return [Line(start[0], start[1], end[0], end[1], color=color)]
        elif set([self.P_ROUN, self.P_TOGE]) == finger.properties:
            pos = self.ROUND_TOGETHER_POS[index.value]
            pos = self.transform_anchors([pos], palm_cfg)[0]
            r_scale = 1.0
            if (abs(palm_cfg.v_finger[0] + palm_cfg.v_finger[1]) ==
                PALM_MAJOR_RADIUS):
                r_scale = 0.6
            elif (abs(palm_cfg.v_finger[0] + palm_cfg.v_finger[1]) ==
                  PALM_MINOR_RADIUS):
                r_scale = 1.3
            return [Ellipse(pos[0],
                            pos[1],
                            self.ROUND_SPRE_R * r_scale,
                            self.ROUND_SPRE_R * r_scale)]
        elif set([self.P_ROUN, self.P_SPRE]) == finger.properties:
            pos = self.ROUND_SPREAD_POS[index.value]
            pos = self.transform_anchors([pos], palm_cfg)[0]
            r_scale = 1.0
            if (abs(palm_cfg.v_finger[0] + palm_cfg.v_finger[1]) ==
                PALM_MAJOR_RADIUS):
                r_scale = 0.6
            elif (abs(palm_cfg.v_finger[0] + palm_cfg.v_finger[1]) ==
                  PALM_MINOR_RADIUS):
                r_scale = 1.3
            return [Ellipse(pos[0],
                            pos[1],
                            self.ROUND_SPRE_R * r_scale,
                            self.ROUND_SPRE_R * r_scale)]

    def is_finger_white(self, finger, palm_cfg):
        if palm_cfg.fill:
            return True

        if (palm_cfg.v_filled_arc is not None and
            np.all(np.cross(palm_cfg.v_finger, palm_cfg.v_filled_arc) ==
                   np.zeros(2))):
            return finger.index == FingerIndex.THUMB

        thumb_side_fingers = [FingerIndex.THUMB,
                              FingerIndex.INDEX,
                              FingerIndex.MIDDLE]
        if finger.index in thumb_side_fingers:
            if np.all(np.equal(palm_cfg.v_thumb, palm_cfg.v_filled_arc)):
                return True
        elif (palm_cfg.v_filled_arc is not None and 
              np.any(np.not_equal(palm_cfg.v_thumb, palm_cfg.v_filled_arc))):
            return True

        return False

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
