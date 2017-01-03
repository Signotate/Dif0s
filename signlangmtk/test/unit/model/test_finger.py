from signlangmtk.model import Finger
from signlangmtk.model import FingerProperty
from signlangmtk.model import FingerIndex


def test_finger_init():
    f = Finger()
    assert f.index is None
    assert f.properties == {FingerProperty.FOLDED}
    assert not f.is_valid()

    f = Finger(index=FingerIndex.INDEX)
    assert f.index == FingerIndex.INDEX
    assert f.properties == {FingerProperty.FOLDED}
    assert f.is_valid()

    f = Finger(index=FingerIndex.MIDDLE,
               properties=[FingerProperty.STRAIGHT,
                           FingerProperty.SPREAD])
    assert f.index == FingerIndex.MIDDLE
    assert f.properties == {FingerProperty.STRAIGHT, FingerProperty.SPREAD}
    assert f.is_valid()

    f = Finger(index=FingerIndex.THUMB,
               properties=[FingerProperty.X,
                           FingerProperty.TOGETHER])
    assert f.index == FingerIndex.THUMB
    assert f.properties == {FingerProperty.X}
    assert f.is_valid()

    f = Finger(index=FingerIndex.THUMB,
               properties=[FingerProperty.X])
    assert f.index == FingerIndex.THUMB
    assert f.properties == {FingerProperty.X}
    assert f.is_valid()

    f = Finger(index=FingerIndex.PINKY,
               properties=[FingerProperty.SPREAD])
    assert f.index == FingerIndex.PINKY
    assert f.properties == {FingerProperty.SPREAD, FingerProperty.STRAIGHT}
    assert f.is_valid()

    f = Finger(index=FingerIndex.PINKY,
               properties=[FingerProperty.BENT])
    assert f.index == FingerIndex.PINKY
    assert f.properties == {FingerProperty.BENT, FingerProperty.TOGETHER}
    assert f.is_valid()


def test_is_valid():
    f = Finger(index=FingerIndex.RING,
               properties=[FingerProperty.X,
                           FingerProperty.CONTACT,
                           FingerProperty.ROUND])
    assert f.index == FingerIndex.RING
    assert f.properties == {FingerProperty.X,
                            FingerProperty.CONTACT,
                            FingerProperty.ROUND}
    assert not f.is_valid()

    f = Finger(index=FingerIndex.RING,
               properties=[FingerProperty.CONTACT,
                           FingerProperty.BENT])
    assert f.index == FingerIndex.RING
    assert f.properties == {FingerProperty.CONTACT,
                            FingerProperty.BENT}
    assert not f.is_valid()


def test_eq():
    f1 = Finger(FingerIndex.INDEX)
    f2 = Finger(FingerIndex.PINKY)

    assert f1 != f2
    assert f2 != f1

    f2 = Finger(FingerIndex.INDEX)
    assert f1 == f2
    assert f2 == f1

    f2 = Finger(FingerIndex.INDEX, properties=[FingerProperty.STRAIGHT])
    assert f1 != f2
    assert f2 != f1
