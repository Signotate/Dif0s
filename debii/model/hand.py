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
        return self.fingers
