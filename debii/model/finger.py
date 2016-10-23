'''A simple model of a finger'''
from enum import Enum
from collections import namedtuple


class FingerProperty(Enum):
    '''
    A property defining of a finger position or shape.
    '''

    STRAIGHT = '+'
    FOLDED = '-'
    SPREAD = 's'
    BENT = 'b'
    ROUND = 'r'
    TAPER = 't'
    CONTACT = 'c'
    X = 'x'
    TOGETHER = ''


class FingerIndex(Enum):
    '''The index identifying a specific finger'''

    THUMB = 0
    INDEX = 1
    MIDDLE = 2
    RING = 3
    PINKY = 4


class Finger(object):
    '''A finger with properties'''

    def __init__(self, index=None, properties=[]):
        self._index = index
        self._properties = set(properties)

    @property
    def index(self):
        return self._index

    @property
    def properties(self):
        return self._properties

    def __eq__(self):
        if self.index != other.index:
            return false
        if self.properties != other.properties:
            return false

        return true
