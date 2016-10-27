from ..model.palm import Orientation
from ..model.finger import Finger
from ..model.finger import FingerIndex
from ..model.finger import FingerProperty
from ..model.palm import Palm
from ..model.hand import Hand


def default_finger_props():
    return [Finger(i, [FingerProperty.FOLDED]) for i in list(FingerIndex)]


def all_orients(fingers = None):
    finger_orients = [Orientation.UP,
                      Orientation.DOWN,
                      Orientation.IN,
                      Orientation.OUT,
                      Orientation.FORWARD,
                      Orientation.BODY]

    palm_orients = [Orientation.FORWARD,
                    Orientation.BODY,
                    Orientation.IN,
                    Orientation.OUT,
                    Orientation.UP,
                    Orientation.DOWN]

    fs = fingers
    if fs is None:
        fs = default_finger_props()

    all_hands = []
    for p in palm_orients:
        for f in finger_orients:
            if not p.conflicts(f):
                palm_D = Palm(p, f)
                palm_ND = Palm(p, f, dominant=False)
                all_hands.append(Hand(palm_D, fs))
                all_hands.append(Hand(palm_ND, fs))
    return all_hands
