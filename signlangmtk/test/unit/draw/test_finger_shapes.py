from signlangmtk.model.palm import Orientation
from signlangmtk.model.palm import Palm
from signlangmtk.model.finger import Finger
from signlangmtk.model.finger import FingerIndex
from signlangmtk.model.finger import FingerProperty
from signlangmtk.draw.common import Line
from signlangmtk.draw import finger_shapes
from signlangmtk.draw import palm_cfg
from signlangmtk.test.unit.draw.utils import lines_similar


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
    assert lines_similar(e, finger_shapes.shapes_for(f1, p1, palm_cfg(p1))[0])

    e = Line(x1=-0.254326, y1=0.245598, x2=-0.254326, y2=0.601041,
             width=0.026230, color='black')
    assert lines_similar(e, finger_shapes.shapes_for(f1, p2, palm_cfg(p2))[0])

    e = Line(x1=-0.173664, y1=0.359672, x2=-0.425000, y2=0.359672,
             width=0.026230, color='black')
    assert lines_similar(e, finger_shapes.shapes_for(f1, p3, palm_cfg(p3))[0])

    f2 = Finger(index=FingerIndex.THUMB,
                properties=[FingerProperty.STRAIGHT,
                            FingerProperty.SPREAD])
    
    e = Line(x1=-0.157331, y1=0.388572, x2=-0.495722, y2=0.130532,
             width=0.026230, color='black')
    assert lines_similar(e, finger_shapes.shapes_for(f2, p1, palm_cfg(p1))[0])

    e = Line(x1=-0.222499, y1=-0.274762, x2=-0.701057, y2=-0.092300,
             width=0.026230, color='black')
    assert lines_similar(e, finger_shapes.shapes_for(f2, p2, palm_cfg(p2))[0])

    e = Line(x1=0.194286, y1=0.314661, x2=0.065266, y2=0.991444,
             width=0.026230, color='black')
    assert lines_similar(e, finger_shapes.shapes_for(f2, p3, palm_cfg(p3))[0])
    
    f3 = Finger(index=FingerIndex.MIDDLE,
                properties=[FingerProperty.FOLDED])

    e = Line(x1=-0.044991, y1=-0.389748, x2=-0.067486, y2=-0.584622,
             width=0.026230, color='black')
    assert lines_similar(e, finger_shapes.shapes_for(f3, p1, palm_cfg(p1))[0])

    e = Line(x1=-0.063627, y1=0.275593, x2=-0.095440, y2=0.413390,
             width=0.026230, color='black')
    assert lines_similar(e, finger_shapes.shapes_for(f3, p2, palm_cfg(p2))[0])

    e = Line(x1=-0.194874, y1=0.089982, x2=-0.292311, y2=0.134973,
             width=0.026230, color='black')
    assert lines_similar(e, finger_shapes.shapes_for(f3, p3, palm_cfg(p3))[0])

    p2 = Palm(palm_dir=Orientation.FORWARD, finger_dir=Orientation.DOWN,
              dominant=False, start_pos=True)

    f4 = Finger(index=FingerIndex.THUMB,
                properties=[FingerProperty.FOLDED])

    e = Line(x1=-0.157331, y1=0.388572, x2=-0.035355, y2=0.070711,
             width=0.026230, color='white')
    assert lines_similar(e, finger_shapes.shapes_for(f4, p2, palm_cfg(p1))[0])

    e = Line(x1=0.222499, y1=-0.274762, x2=0.050000, y2=-0.050000,
             width=0.026230, color='black')
    assert lines_similar(e, finger_shapes.shapes_for(f4, p2, palm_cfg(p2))[0])
    
    e = Line(x1=0.194286, y1=0.314661, x2=0.035355, y2=0.070711, width=0.026230,
             color='white')
    assert lines_similar(e, finger_shapes.shapes_for(f4, p3, palm_cfg(p3))[0])
