from ..model.finger import FingerProperty
from ..model.finger import FingerIndex
from ..model.finger import InvalidFingerException
from ..model.palm import Orientation
from .common import pol2car
from .common import Line
from .common import Ellipse
from .common import Triangle
from .common import Diamond
from .hand_config import PALM_CIRCLE_RADIUS
from .hand_config import HAND_CIRCLE_RADIUS
from .hand_config import PALM_MINOR_RADIUS
from .hand_config import PALM_MAJOR_RADIUS
import numpy as np
import logging


logger = logging.getLogger(__name__)


class FingerShapes(object):
    '''
    Access shapes for a single finger, based on a palm_config

    Configuration is bases on a set of vectors (anchors) with define finger
    shapes for the Dfu palm config.  The vectors can be transformed to be used
    every palm configuration.
    '''

    P_STRA = FingerProperty.STRAIGHT
    P_SPRE = FingerProperty.SPREAD
    P_ROUN = FingerProperty.ROUND
    P_BEND = FingerProperty.BENT
    P_FOLD = FingerProperty.FOLDED
    P_CONT = FingerProperty.CONTACT
    P_TAPE = FingerProperty.TAPER
    P_TOGE = FingerProperty.TOGETHER
    P_X = FingerProperty.X

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
        self.STRAIGHT_THUMB_START = np.array(pol2car(PALM_CIRCLE_RADIUS,
                                                     2 * np.pi))

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
        self.RC_LONG_PHIS = [5.8, 0.22689, 0.84634, 2.29542, 2.91470]
        self.RC_PHIS = [5.8, 0.22689, 1.07634, 2.06542, 2.91470]
        self.RC_LEN_SCALES = [0.4, 0.65, 0.55, 0.55, 0.65]
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

        self.RC_POS = []
        for t, s in zip(self.RC_PHIS, self.RC_LEN_SCALES):
            self.RC_POS.append(pol2car(s * PALM_CIRCLE_RADIUS, t))
        self.RC_POS[0] = np.array([0.15, -0.2])

        self.RC_LONG_POS = []
        for t, s in zip(self.RC_LONG_PHIS, self.RC_LEN_SCALES):
            self.RC_LONG_POS.append(pol2car(s * PALM_CIRCLE_RADIUS, t))

        self.BENT_T_PHI = 0.0
        self.BENT_TRI_SIZE = 0.12
        self.BENT_TOGETHER_POS = []
        for s, l in zip(self.FINGER_STARTS, self.ROUND_LENS):
            self.BENT_TOGETHER_POS.append(np.array([s[0], l]))
        self.BENT_TOGETHER_POS[0] = np.array(pol2car(self.ROUND_T_LEN,
                                                     self.BENT_T_PHI))

        self.BENT_SPREAD_POS = []
        for t, s in zip(self.FINGER_START_PHIS, self.ROUND_SCALES):
            self.BENT_SPREAD_POS.append(pol2car(self.ROUND_SP_END_R * s, t))
        self.BENT_SPREAD_POS[0] = np.array(pol2car(self.ROUND_T_LEN,
                                                   self.BENT_T_PHI))

        self.TAPER_SCALES = [1.0, 0.98, 0.99, 0.98, 0.93]
        self.TAPER_LENS = [self.ROUND_END_R * s for s in self.TAPER_SCALES]
        self.TAPER_T_PHI = 0.0
        self.TAPER_DIMOND_SIZE = 0.12
        self.TAPER_TOGETHER_POS = []
        for s, l in zip(self.FINGER_STARTS, self.TAPER_LENS):
            self.TAPER_TOGETHER_POS.append(np.array([s[0], l]))
        self.TAPER_TOGETHER_POS[0] = np.array(pol2car(self.ROUND_T_LEN,
                                                      self.TAPER_T_PHI))

        self.TAPER_SPREAD_POS = []
        for t, s in zip(self.FINGER_START_PHIS, self.TAPER_SCALES):
            self.TAPER_SPREAD_POS.append(pol2car(self.ROUND_SP_END_R * s, t))
        self.TAPER_SPREAD_POS[0] = np.array(pol2car(self.ROUND_T_LEN,
                                                    self.TAPER_T_PHI))

        self.TC_POS = []
        for t, s in zip(self.RC_PHIS, self.RC_LEN_SCALES):
            self.TC_POS.append(pol2car(s * PALM_CIRCLE_RADIUS, t))
        self.TC_POS[0] = np.array([0.15, -0.2])

        self.TC_LONG_POS = []
        for t, s in zip(self.RC_LONG_PHIS, self.RC_LEN_SCALES):
            self.TC_LONG_POS.append(pol2car(s * PALM_CIRCLE_RADIUS, t))

        self.TC_IU_POS = []
        self.C_IU_PHIS = [0.6736970912698113,
                          1.3802063724771156,
                          1.0793116094332935,
                          0.40840704496667307,
                          5.677556056737554]
        self.C_IU_SCALES = [0.4, 0.33, 0.23, 0.17, 0.16]
        for t, s in zip(self.C_IU_PHIS, self.C_IU_SCALES):
            self.TC_IU_POS.append(pol2car(s, t))

        self.shape_sets = {frozenset([self.P_STRA,
                                      self.P_TOGE]): self._shapes_stra_toge,
                           frozenset([self.P_STRA,
                                      self.P_SPRE]): self._shapes_stra_spre,
                           frozenset([self.P_FOLD]): self._shapes_fold,
                           frozenset([self.P_ROUN,
                                      self.P_TOGE]): self._shapes_roun_toge,
                           frozenset([self.P_ROUN,
                                      self.P_SPRE]): self._shapes_roun_spre,
                           frozenset([self.P_ROUN,
                                      self.P_CONT]): self._shapes_roun_cont,
                           frozenset([self.P_BEND,
                                      self.P_TOGE]): self._shapes_bend_toge,
                           frozenset([self.P_BEND,
                                      self.P_SPRE]): self._shapes_bend_spre,
                           frozenset([self.P_TAPE,
                                      self.P_TOGE]): self._shapes_taper_toge,
                           frozenset([self.P_TAPE,
                                      self.P_SPRE]): self._shapes_taper_spre,
                           frozenset([self.P_TAPE,
                                      self.P_CONT]): self._shapes_taper_cont,
                           frozenset([self.P_X]): self._shapes_stra_toge}

    def _line_shapes(self, palm, palm_cfg, finger, start, end, color='black'):
        start, end = self.transform_anchors([start, end], palm_cfg)
        return [Line(start[0], start[1], end[0], end[1], color=color)]

    def _shapes_stra_toge(self, palm, palm_cfg, finger):
        start = self.FINGER_STARTS[finger.index.value]
        if finger.index == FingerIndex.THUMB:
            start = self.STRAIGHT_THUMB_START
        end = self.STRAIGHT_ENDS[finger.index.value]
        return self._line_shapes(palm, palm_cfg, finger, start, end)

    def _shapes_stra_spre(self, palm, palm_cfg, finger):
        start = self.FINGER_STARTS[finger.index.value]
        end = self.SPLAY_ENDS[finger.index.value]
        return self._line_shapes(palm, palm_cfg, finger, start, end)

    def _shapes_fold(self, palm, palm_cfg, finger):
        start = self.FOLDED_STARTS[finger.index.value]
        end = self.FOLDED_ENDS[finger.index.value]
        color = 'black'
        if finger.index == FingerIndex.THUMB:
            start = self.FINGER_STARTS[0]
            end = self.FOLDED_THUMB_END
            if self.is_finger_white(finger, palm_cfg):
                logger.debug('Drawing folded Thumb: Thumb is white')
                color = 'white'
        return self._line_shapes(palm, palm_cfg, finger, start, end,
                                 color=color)

    def _shapes_roun_toge(self, palm, palm_cfg, finger):
        pos = self.ROUND_TOGETHER_POS[finger.index.value]
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

    def _shapes_roun_spre(self, palm, palm_cfg, finger):
        pos = self.ROUND_SPREAD_POS[finger.index.value]
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

    def _shapes_bend_toge(self, palm, palm_cfg, finger):
        pos = self.BENT_TOGETHER_POS[finger.index.value]
        pos = self.transform_anchors([pos], palm_cfg)[0]
        l = self.BENT_TRI_SIZE
        if (abs(palm_cfg.v_finger[0] + palm_cfg.v_finger[1]) ==
                PALM_MINOR_RADIUS):
            l = l * 1.3
        v = np.nan_to_num(np.divide(palm_cfg.v_finger,
                                    np.abs(palm_cfg.v_finger)))
        v = v * l
        return [Triangle(pos[0], pos[1], v)]

    def _shapes_bend_spre(self, palm, palm_cfg, finger):
        pos = self.BENT_SPREAD_POS[finger.index.value]
        pos = self.transform_anchors([pos], palm_cfg)[0]
        l = self.BENT_TRI_SIZE
        if (abs(palm_cfg.v_finger[0] + palm_cfg.v_finger[1]) ==
                PALM_MINOR_RADIUS):
            l = l * 1.3
        v = np.nan_to_num(np.divide(palm_cfg.v_finger,
                                    np.abs(palm_cfg.v_finger)))
        v = v * l
        return [Triangle(pos[0], pos[1], v)]

    def _shapes_taper_toge(self, palm, palm_cfg, finger):
        pos = self.TAPER_TOGETHER_POS[finger.index.value]
        pos = self.transform_anchors([pos], palm_cfg)[0]
        l = self.TAPER_DIMOND_SIZE
        if (abs(palm_cfg.v_finger[0] + palm_cfg.v_finger[1]) ==
                PALM_MAJOR_RADIUS):
            l = l * 0.6
        elif (abs(palm_cfg.v_finger[0] + palm_cfg.v_finger[1]) ==
                PALM_MINOR_RADIUS):
            l = l * 1.3
        v = np.nan_to_num(np.divide(palm_cfg.v_finger,
                                    np.abs(palm_cfg.v_finger)))
        v = v * l
        return [Diamond(pos[0], pos[1], v)]

    def _shapes_taper_spre(self, palm, palm_cfg, finger):
        pos = self.TAPER_SPREAD_POS[finger.index.value]
        pos = self.transform_anchors([pos], palm_cfg)[0]
        l = self.TAPER_DIMOND_SIZE
        if (abs(palm_cfg.v_finger[0] + palm_cfg.v_finger[1]) ==
                PALM_MAJOR_RADIUS):
            l = l * 0.6
        elif (abs(palm_cfg.v_finger[0] + palm_cfg.v_finger[1]) ==
                PALM_MINOR_RADIUS):
            l = l * 1.3
        v = np.nan_to_num(np.divide(palm_cfg.v_finger,
                                    np.abs(palm_cfg.v_finger)))
        v = v * l
        return [Diamond(pos[0], pos[1], v)]

    def _shapes_roun_cont(self, palm, palm_cfg, finger):
        if self.is_in_up_palm(palm):
            pos = self.TC_IU_POS[finger.index.value]
            r = self.ROUND_SPRE_R
            r = r * 0.6
            pos = self.transform_c_iu_anchors([pos], palm_cfg)[0]
            color = 'black'
            if ((Orientation.OUT == palm.finger_dir or
                    Orientation.OUT == palm.palm_dir) and
                    finger.index != FingerIndex.THUMB):
                color = 'white'
            return [Ellipse(pos[0], pos[1], r, r, color=color)]
        else:
            pos = self.RC_POS[finger.index.value]
            r = self.ROUND_SPRE_R
            if (abs(palm_cfg.v_finger[0] + palm_cfg.v_finger[1]) ==
                    PALM_MAJOR_RADIUS):
                r = r * 0.6
                pos = self.RC_LONG_POS[finger.index.value]
            pos = self.transform_anchors([pos], palm_cfg)[0]
            color = 'black'
            if self.is_finger_white(finger, palm_cfg):
                color = 'white'
            return [Ellipse(pos[0], pos[1], r, r, color=color)]

    def _shapes_taper_cont(self, palm, palm_cfg, finger):
        if self.is_in_up_palm(palm):
            pos = self.TC_IU_POS[finger.index.value]
            pos = self.transform_c_iu_anchors([pos], palm_cfg)[0]
            l = self.TAPER_DIMOND_SIZE
            l = l * 0.6
            color = 'black'
            if ((Orientation.OUT == palm.finger_dir
                    or Orientation.OUT == palm.palm_dir)
                    and finger.index != FingerIndex.THUMB):
                color = 'white'
            v = np.nan_to_num(np.divide(palm_cfg.v_finger,
                                        np.abs(palm_cfg.v_finger)))
            v = v * l
            return [Diamond(pos[0], pos[1], v, color=color)]
        else:
            pos = self.TC_POS[finger.index.value]
            l = self.TAPER_DIMOND_SIZE
            if (abs(palm_cfg.v_finger[0] + palm_cfg.v_finger[1]) ==
                    PALM_MAJOR_RADIUS):
                l = l * 0.6
                pos = self.TC_LONG_POS[finger.index.value]
            pos = self.transform_anchors([pos], palm_cfg)[0]
            color = 'black'
            if self.is_finger_white(finger, palm_cfg):
                color = 'white'
            v = np.nan_to_num(np.divide(palm_cfg.v_finger,
                                        np.abs(palm_cfg.v_finger)))
            v = v * l
            return [Diamond(pos[0], pos[1], v, color=color)]

    def has_shapes_for(self, finger):
        return frozenset(finger.properties) in self.shape_sets

    def shapes_for(self, finger, palm, palm_cfg):
        if self.has_shapes_for(finger):
            return self.shape_sets[frozenset(finger.properties)](palm,
                                                                 palm_cfg,
                                                                 finger)
        raise InvalidFingerException('No Shapes for ' + str(finger.properties))

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
            scale = palm_config.transforms[1]
            rotate = palm_config.transforms[2]
            a_p = mirror.dot(a_p)
            a_p = rotate.dot(a_p)
            a_p = scale.dot(a_p)
            a_p = np.array([[1.0, 0.0],
                            [0.0, -1.0]]).dot(a_p)
            anchors_prime.append(a_p)
        return anchors_prime

    def transform_c_iu_anchors(self, anchors, palm_config):
        anchors_prime = []
        for a in anchors:
            a_p = np.array([a[0], a[1]])
            a_p = np.array([[-1.0, 0.0], [0.0, 1.0]]).dot(a)  # pre mirror
            mirror = palm_config.transforms[0]
            rotate = palm_config.transforms[2]
            a_p = mirror.dot(a_p)
            a_p = rotate.dot(a_p)
            a_p = np.array([[1.0, 0.0],
                            [0.0, -1.0]]).dot(a_p)
            anchors_prime.append(a_p)
        return anchors_prime

    def is_in_up_palm(self, palm):
        f_dir = palm.finger_dir
        p_dir = palm.palm_dir
        orients = [f_dir, p_dir]
        if Orientation.IN in orients or Orientation.OUT in orients:
            return Orientation.UP in orients or Orientation.DOWN in orients
        return False
