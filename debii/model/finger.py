'''A simple model of a finger'''
from enum import Enum
from collections import namedtuple
from functools import total_ordering


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
    TOGETHER = 8


class FingerIndex(Enum):
    '''The index identifying a specific finger'''

    THUMB = 0
    INDEX = 1
    MIDDLE = 2
    RING = 3
    PINKY = 4


@total_ordering
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

    def __lt__(self, other):
        if self.index < other.index:
            return true
        return (''.join(sorted([str(p.value) for p in self.properties])) <
                   ''.join(sorted([str(p.value) for p in other.properties])))
