"""The model of the hand part of a sign language sign"""
from enum import Enum
from collections import namedtuple


PalmTransition = namedtuple('PalmTransition', 'base_palm flip rotation fill')


class FingerProperty(Enum):
    STRAIGHT = 0
    FOLDED = 1
    SPREAD = 2
    BENT = 3
    ROUND = 4
    TAPER = 5
    CONTACT = 6
    X = 7


class Finger(Enum):
    THUMB = 0
    INDEX = 1
    MIDDLE = 2
    RING = 3
    PINKY = 4


class Flip(Enum):
    TOP = 0
    BOTTOM = 0
    LEFT = 3
    RIGHT = 4


class HandPosition(object):
    def __init__(self, palm_pos, fingers={}):
        super(HandPosition, self).__init__()

        self._palm_pos = palm_pos
        self._fingers = fingers

    @property
    def palm_pos(self):
        return self._palm_pos

    @property
    def fingers(self):
        return self._fingers


class FingerPosition(object):
    def __init__(self, finger, properties=set([])):
        super(FingerPosition, self).__init__()

        self._finger = finger
        self._properties = properties

    @property
    def finger(self):
        return self._finger

    @property
    def properties(self):
        return self._properties

    def __eq__(self, other):
        return ((self.finger, self.properties) ==
                (other.finger, other.properties))

    def __hash__(self):
        return hash((self.finger, self.properties))

    def __repr__(self):
        s = 'FingerPosition('
        s += 'finger=' + self.finger
        s += ', properties=' + self.properties
        s += ')'
        return s

    def __str__(self):
        return repr(self)
