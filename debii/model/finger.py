'''A simple model of a finger'''
from enum import Enum
from collections import namedtuple


class FingerProperty(Enum):
    '''A finger property'''

    STRAIGHT = 0
    FOLDED = 1
    SPREAD = 2
    BENT = 3
    ROUND = 4
    TAPER = 5
    CONTACT = 6
    X = 7


class FingerIndex(Enum):
    '''The index identifying a specific finger'''

    THUMB = 0
    INDEX = 1
    MIDDLE = 2
    RING = 3
    PINKY = 4


Finger = namedtuple('Finger', ['index', 'property_list'])
