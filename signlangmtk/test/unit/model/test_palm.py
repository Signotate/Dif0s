from signlangmtk.model import Palm
from signlangmtk.model import Orientation


def test_palm_init():
    p = Palm(finger_dir=Orientation.UP, palm_dir=Orientation.FORWARD)
    assert Orientation.UP == p.finger_dir
    assert Orientation.FORWARD == p.palm_dir
    assert p.dominant
    assert p.start_pos
    assert p.is_valid()

    p = Palm(finger_dir=Orientation.DOWN,
             palm_dir=Orientation.IN,
             dominant=False,
             start_pos=False)
    assert Orientation.DOWN == p.finger_dir
    assert Orientation.IN == p.palm_dir
    assert not p.dominant
    assert not p.start_pos
    assert p.is_valid()


def test_palm_conflicting_orients():
    p = Palm(finger_dir=Orientation.UP, palm_dir=Orientation.DOWN)
    assert not p.is_valid()


def test_no_dir_palm():
    p = Palm()
    assert p.finger_dir is None
    assert p.palm_dir is None
    assert p.dominant
    assert p.start_pos
    assert not p.is_valid()
