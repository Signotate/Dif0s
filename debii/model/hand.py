"""The model of the hand part of a sign language sign"""


class Hand(object):
    '''The universal hand'''

    def __init__(self, palm, fingers):
        self._palm = palm
        self._fingers = fingers

    @property
    def palm(self):
        return self._palm

    @property
    def fingers(self):
        return self._fingers

    def __str__(self):
        return str(self.palm)

    def __repr__(self):
        s = 'Hand(palm='
        s += repr(self.palm)
        s += ', fingers='
        s += repr(self.fingers)
        s += ')'
        return s
