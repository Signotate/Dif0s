from ....model.finger import Finger
from ....model.finger import FingerIndex
from ....model.finger import FingerProperty
from ....model.palm import Palm
from ....model.palm import Orientation
from ....model.hand import Hand
from ....draw.common import Ellipse
from ....draw.common import FilledArc
from ....draw import palm_cfg


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
