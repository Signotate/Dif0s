from .finger import Finger
from .finger import FingerIndex
from .finger import FingerProperty


"""The model of the hand part of a sign language sign"""


class Hand(object):
    '''The universal hand'''

    _default_fingers = {i: Finger(i) for i in list(FingerIndex)}

    def __init__(self, palm, fingers):
        self._palm = palm
        self._fingers = self._determine_fingers(fingers)

    @property
    def palm(self):
        return self._palm

    @property
    def fingers(self):
        return self._fingers

    def _determine_fingers(self, lst):
        fingers = {}
        finger_lst = []
        for f in lst:
            if f.index not in fingers:
                fingers[f.index] = f
                finger_lst.append(f)
        for i, f in ((finger.index, finger) for finger in finger_lst):
            if (FingerProperty.CONTACT in f.properties
                and i != FingerIndex.THUMB):

                if FingerIndex.THUMB in fingers:
                    thumb = fingers[FingerIndex.THUMB]
                    if FingerProperty.CONTACT not in thumb.properties:
                        thumb = Finger(FingerIndex.THUMB, f.properties)
                        fingers[FingerIndex.THUMB] = thumb
                    elif set([FingerProperty.CONTACT]) == thumb.properties:
                        thumb = Finger(FingerIndex.THUMB, f.properties)
                        fingers[FingerIndex.THUMB] = thumb
                else:
                    thumb = Finger(FingerIndex.THUMB, f.properties)
                    fingers[FingerIndex.THUMB] = thumb

                # only apply for first contact finger
                break

        # fill in missing fingers with defaults
        for i, f in self._default_fingers.items():
            if i not in fingers:
                fingers[i] = f

        return list(fingers.values())


    def __str__(self):
        return str(self.palm)

    def __repr__(self):
        s = 'Hand(palm='
        s += repr(self.palm)
        s += ', fingers='
        s += repr(self.fingers)
        s += ')'
        return s

    def __eq__(self, other):
        if self.palm != other.palm:
            return False
        elif (sorted(self.fingers, key=lambda f: f.index) != 
              sorted(other.fingers, key=lambda f: f.index)):
            return False
        return True
