from ....draw import draw_hand
from ....draw import draw_palm
from ....draw import draw_fingers
from ....model.finger import Finger
from ....model.finger import FingerIndex
from ....model.finger import FingerProperty
from ....model.palm import Palm
from ....model.palm import Orientation
from ....model.hand import Hand
from ....draw.common import Line
from ....draw.common import Ellipse
from ....draw.common import FilledArc
from ....draw.palm_config import palm_cfg
from ....draw.palm_config import finger_shapes
import numpy as np


def test_shapes_for_palm():
    h = Hand(palm=Palm(palm_dir=Orientation.OUT, finger_dir=Orientation.BODY,
                       dominant=False, start_pos=True),
             fingers=[Finger(index=FingerIndex.THUMB,
                             properties=[FingerProperty.STRAIGHT,
                                         FingerProperty.SPREAD]),
                      Finger(index=FingerIndex.INDEX,
                             properties=[FingerProperty.STRAIGHT,
                                         FingerProperty.TOGETHER]),
                      Finger(index=FingerIndex.MIDDLE,
                             properties=[FingerProperty.STRAIGHT,
                                         FingerProperty.SPREAD]),
                      Finger(index=FingerIndex.RING,
                             properties=[FingerProperty.STRAIGHT,
                                         FingerProperty.SPREAD]),
                      Finger(index=FingerIndex.PINKY,
                             properties=[FingerProperty.STRAIGHT,
                                         FingerProperty.TOGETHER])])

    expected_shapes = [Ellipse(cx=0.000000, cy=0.000000, rx=-0.250000,
                               ry=0.500000, fill=True, line_width=0.059016)]
    palm_shapes = palm_cfg.shapes_for(h.palm)
    for expected, actual in zip(expected_shapes, palm_shapes):
        assert expected, actual

    h = Hand(palm=Palm(palm_dir=Orientation.IN, finger_dir=Orientation.UP,
                       dominant=False, start_pos=True),
             fingers=[Finger(index=FingerIndex.THUMB,
                             properties=[FingerProperty.STRAIGHT,
                                         FingerProperty.SPREAD]),
                      Finger(index=FingerIndex.INDEX,
                             properties=[FingerProperty.STRAIGHT,
                                         FingerProperty.TOGETHER]),
                      Finger(index=FingerIndex.MIDDLE,
                             properties=[FingerProperty.STRAIGHT,
                                         FingerProperty.SPREAD]),
                      Finger(index=FingerIndex.RING,
                             properties=[FingerProperty.STRAIGHT,
                                         FingerProperty.SPREAD]),
                      Finger(index=FingerIndex.PINKY,
                             properties=[FingerProperty.STRAIGHT,
                                         FingerProperty.TOGETHER])])

    expected_shapes = [Ellipse(cx=0.000000, cy=0.000000, rx=0.250000,
                               ry=0.500000, line_width=0.059016),
                       FilledArc(cx=0.000000, cy=0.000000, rx=0.250000,
                                 ry=0.500000, line_width=0.026230,
                                 start_radians=4.712389, end_radians=7.853982)]

    palm_shapes = palm_cfg.shapes_for(h.palm)
    for expected, actual in zip(expected_shapes, palm_shapes):
        assert expected, actual

def test_shapes_for_finger():
    p1 = Palm(palm_dir=Orientation.IN, finger_dir=Orientation.UP,
              dominant=True, start_pos=True)

    p2 = Palm(palm_dir=Orientation.BODY, finger_dir=Orientation.DOWN,
              dominant=False, start_pos=True)

    p3 = Palm(palm_dir=Orientation.IN, finger_dir=Orientation.BODY,
              dominant=False, start_pos=True)

    f1 = Finger(index=FingerIndex.INDEX,
                properties=[FingerProperty.STRAIGHT,
                            FingerProperty.TOGETHER])

    e = Line(x1=-0.179836, y1=-0.347327, x2=-0.179836, y2=-0.850000,
             width=0.026230, color='black')
    assert lines_similar(e, finger_shapes.shapes_for(f1, palm_cfg(p1))[0])

    e = Line(x1=-0.254326, y1=0.245598, x2=-0.254326, y2=0.601041,
             width=0.026230, color='black')
    assert lines_similar(e, finger_shapes.shapes_for(f1, palm_cfg(p2))[0])

    e = Line(x1=-0.173664, y1=0.359672, x2=-0.425000, y2=0.359672,
             width=0.026230, color='black')
    assert lines_similar(e, finger_shapes.shapes_for(f1, palm_cfg(p3))[0])


    f2 = Finger(index=FingerIndex.THUMB,
                properties=[FingerProperty.STRAIGHT,
                            FingerProperty.SPREAD])
    
    e = Line(x1=-0.157331, y1=0.388572, x2=-0.495722, y2=0.130532,
             width=0.026230, color='black')
    assert lines_similar(e, finger_shapes.shapes_for(f2, palm_cfg(p1))[0])

    e = Line(x1=-0.222499, y1=-0.274762, x2=-0.701057, y2=-0.092300,
             width=0.026230, color='black')
    assert lines_similar(e, finger_shapes.shapes_for(f2, palm_cfg(p2))[0])

    e = Line(x1=0.194286, y1=0.314661, x2=0.065266, y2=0.991444,
             width=0.026230, color='black')
    assert lines_similar(e, finger_shapes.shapes_for(f2, palm_cfg(p3))[0])
    
    f3 = Finger(index=FingerIndex.MIDDLE,
                properties=[FingerProperty.FOLDED])

    e = Line(x1=-0.044991, y1=-0.389748, x2=-0.067486, y2=-0.584622,
             width=0.026230, color='black')
    assert lines_similar(e, finger_shapes.shapes_for(f3, palm_cfg(p1))[0])

    e = Line(x1=-0.063627, y1=0.275593, x2=-0.095440, y2=0.413390,
             width=0.026230, color='black')
    assert lines_similar(e, finger_shapes.shapes_for(f3, palm_cfg(p2))[0])

    e = Line(x1=-0.194874, y1=0.089982, x2=-0.292311, y2=0.134973,
             width=0.026230, color='black')
    assert lines_similar(e, finger_shapes.shapes_for(f3, palm_cfg(p3))[0])

    p2 = Palm(palm_dir=Orientation.FORWARD, finger_dir=Orientation.DOWN,
              dominant=False, start_pos=True)

    f4 = Finger(index=FingerIndex.THUMB,
                properties=[FingerProperty.FOLDED])

    e = Line(x1=-0.157331, y1=0.388572, x2=-0.035355, y2=0.070711,
             width=0.026230, color='white')
    assert lines_similar(e, finger_shapes.shapes_for(f4, palm_cfg(p1))[0])

    e = Line(x1=0.222499, y1=-0.274762, x2=0.050000, y2=-0.050000,
             width=0.026230, color='black')
    assert lines_similar(e, finger_shapes.shapes_for(f4, palm_cfg(p2))[0])
    
    e = Line(x1=0.194286, y1=0.314661, x2=0.035355, y2=0.070711, width=0.026230,
             color='white')
    assert lines_similar(e, finger_shapes.shapes_for(f4, palm_cfg(p3))[0])


def lines_similar(line1, line2):
    l1 = np.array([line1.x1, line1.y1, line1.x2, line1.y2])
    l2 = np.array([line2.x1, line2.y1, line2.x2, line2.y2])
    print(l1, l2)

    if not np.all(np.isclose(l1, l2)):
        return False
    if not np.isclose(line1.width, line2.width):
        return False
    if not line1.color == line2.color:
        return False
    return True
