'''A simple model of a palm position'''


from enum import Enum
import re


__PALM_PATTERN = re.compile(r'^(?P<d_nd>N?D)(?P<start_end>[se])?' +
                            r'(?P<palm_orient>[udfbio])' +
                            r'(?P<finger_orient>[udfbio])$')


def parse_palm(s):
    '''Create a palm from its string representation'''
    match = re.match(__PALM_PATTERN, s.strip())

    invalid_palm = InvalidPalmException('The string \'' + str(s) + '\' is' +
                                        ' not a valid palm')

    if match is None:
        raise invalid_palm
    palm_parts = match.groupdict()

    dominant = True
    if palm_parts['d_nd'] == 'ND':
        dominant = False

    start_pos = True
    if palm_parts.get('start_end', None) is None:
        start_pos = None
    elif palm_parts.get('start_end', None) == 'e':
        start_pos = False

    palm_orient = Orientation.parse(palm_parts['palm_orient'])
    finger_orient = Orientation.parse(palm_parts['finger_orient'])

    if palm_orient.conflicts(finger_orient):
        raise invalid_palm

    return Palm(palm_orient, finger_orient, dominant, start_pos)


class InvalidPalmException(Exception):
    pass


class Orientation(Enum):
    """Palm and finger orientations"""

    UP = 'u'
    DOWN = 'd'
    FORWARD = 'f'
    BODY = 'b'
    IN = 'i'
    OUT = 'o'

    def __str__(self):
        return str(self.value)

    @classmethod
    def parse(cls, s):
        '''Get the orientation associated with s'''
        if s not in [o.value for o in list(cls)]:
            return None
        else:
            for o in list(cls):
                if o.value == s:
                    return o

    def __repr__(self):
        return "%s.%s" % (self.__class__.__name__, self._name_)

    def conflicts(self, other_orient):
        '''Return true of orientation conflict'''
        oposites = [(Orientation.UP, Orientation.DOWN),
                    (Orientation.IN, Orientation.OUT),
                    (Orientation.FORWARD, Orientation.BODY)]

        for oposite in oposites:
            if self in oposite and other_orient in oposite:
                return True

        return False


class Palm(object):
    '''A palm'''

    def __init__(self, palm_dir=None, finger_dir=None, dominant=True,
                 start_pos=True):
        self._palm_dir = palm_dir
        self._finger_dir = finger_dir
        self._dominant = dominant
        self._start_pos = start_pos

    @property
    def palm_dir(self):
        return self._palm_dir

    @property
    def finger_dir(self):
        return self._finger_dir

    @property
    def dominant(self):
        return self._dominant

    @property
    def start_pos(self):
        return self._start_pos

    def __str__(self):
        s = 'D'
        if not self.dominant:
            s = 'ND'
        if self.start_pos is True:
            s += 's'
        elif self.start_pos is False:
            s += 'e'

        s += str(self.palm_dir) + str(self.finger_dir)
        return s

    def __repr__(self):
        s = 'Palm('
        s += 'palm_dir=' + repr(self.palm_dir)
        s += ', finger_dir=' + repr(self.finger_dir)
        s += ', dominant=' + repr(self.dominant)
        s += ', start_pos=' + repr(self.start_pos)
        s += ')'

        return s

    def __eq__(self, other):
        return ((self.palm_dir,
                 self.finger_dir,
                 self.dominant,
                 self.start_pos) ==
                (other.palm_dir,
                 other.finger_dir,
                 other.dominant,
                 other.start_pos))


if __name__ == "__main__":
    import sys
