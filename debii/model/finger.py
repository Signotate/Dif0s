'''A simple model of a finger'''
from enum import Enum
from ..util import OrderedEnum
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

    @classmethod
    def parse(cls, s):
        '''Get the orientation associated with s'''
        if s not in [o.value for o in list(cls)]:
            return None
        else:
            for o in list(cls):
                if o.value == s:
                    return o


class FingerIndex(OrderedEnum):
    '''The index identifying a specific finger'''

    THUMB = 0
    INDEX = 1
    MIDDLE = 2
    RING = 3
    PINKY = 4

    @classmethod
    def parse(cls, s):
        '''Get the orientation associated with s'''
        if int(s) not in [o.value for o in list(cls)]:
            return None
        else:
            for o in list(cls):
                if o.value == int(s):
                    return o


class Finger(object):
    '''A finger with properties'''

    def __init__(self, index=None, properties=[]):
        self._index = index
        self._properties = self._determine_properties(properties)

    @property
    def index(self):
        return self._index

    @property
    def properties(self):
        return self._properties
    
    def __hash__(self):
        prime = 37
        result = prime * hash(self.index)
        result += prime * hash(self.properties)
        return result

    def __eq__(self, other):
        if self.index != other.index:
            return False
        if self.properties != other.properties:
            return False

        return True

    def _determine_properties(self, props):
        if props is None or len(props) == 0:
            return set([FingerProperty.FOLDED])
        elif (FingerProperty.FOLDED not in props and
              FingerProperty.SPREAD not in props and
              FingerProperty.CONTACT not in props and
              FingerProperty.TOGETHER not in props):
            properties = set(props)
            properties.add(FingerProperty.TOGETHER)
            return properties
        return set(props)

    def __repr__(self):
        return 'Finger(index=%s, properties=%s)' % (repr(self.index),
                                                    repr(self.properties))
