from signlangmtk.model import *
from signlangmtk.parser import parse_hand


def test_parse_hand_simple():
    hand_Dfu = Hand(Palm(palm_dir=Orientation.FORWARD,
                         finger_dir=Orientation.UP,
                         dominant=True,
                         start_pos=True),
                    [Finger(index=FingerIndex.THUMB,
                            properties=[FingerProperty.FOLDED]),
                     Finger(index=FingerIndex.INDEX,
                            properties=[FingerProperty.FOLDED]),
                     Finger(index=FingerIndex.MIDDLE,
                            properties=[FingerProperty.FOLDED]),
                     Finger(index=FingerIndex.RING,
                            properties=[FingerProperty.FOLDED]),
                     Finger(index=FingerIndex.PINKY,
                            properties=[FingerProperty.FOLDED])])

    hand_NDefu = Hand(Palm(palm_dir=Orientation.FORWARD,
                           finger_dir=Orientation.UP,
                           dominant=False,
                           start_pos=False),
                      [Finger(index=FingerIndex.THUMB,
                              properties=[FingerProperty.FOLDED]),
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

    hand_Dfu_rc = Hand(Palm(palm_dir=Orientation.FORWARD,
                            finger_dir=Orientation.UP,
                            dominant=True,
                            start_pos=True),
                       [Finger(index=FingerIndex.THUMB,
                               properties=[FingerProperty.CONTACT,
                                           FingerProperty.ROUND]),
                        Finger(index=FingerIndex.INDEX,
                               properties=[FingerProperty.CONTACT,
                                           FingerProperty.ROUND]),
                        Finger(index=FingerIndex.MIDDLE,
                               properties=[FingerProperty.CONTACT,
                                           FingerProperty.ROUND]),
                        Finger(index=FingerIndex.RING,
                               properties=[FingerProperty.CONTACT,
                                           FingerProperty.ROUND]),
                        Finger(index=FingerIndex.PINKY,
                               properties=[FingerProperty.CONTACT,
                                           FingerProperty.ROUND])])

    assert hand_Dfu == parse_hand('Dfu', parseAll=True)
    assert hand_Dfu == parse_hand('Dsfu', parseAll=True)
    assert hand_Dfu == parse_hand('Dfu 01234-', parseAll=True)
    assert hand_Dfu == parse_hand('Dfu 0- 1-2-3-4-', parseAll=True)
    assert hand_Dfu == parse_hand('Dfu 1-', parseAll=True)
    assert hand_Dfu_rc == parse_hand('Dfu 123rc 4rc', parseAll=True)
    assert hand_NDefu == parse_hand('NDefu 1+ 23s+ 4+', parseAll=True)


def test_parse_hand_contact():
    hand_Dui_1tc = Hand(Palm(palm_dir=Orientation.UP,
                             finger_dir=Orientation.IN,
                             dominant=True,
                             start_pos=True),
                        [Finger(index=FingerIndex.THUMB,
                                properties=[FingerProperty.TAPER,
                                            FingerProperty.CONTACT]),
                         Finger(index=FingerIndex.INDEX,
                                properties=[FingerProperty.TAPER,
                                            FingerProperty.CONTACT]),
                         Finger(index=FingerIndex.MIDDLE,
                                properties=[FingerProperty.FOLDED]),
                         Finger(index=FingerIndex.RING,
                                properties=[FingerProperty.FOLDED]),
                         Finger(index=FingerIndex.PINKY,
                                properties=[FingerProperty.FOLDED])])

    hand_Dui_1tc_234b = Hand(Palm(palm_dir=Orientation.UP,
                                  finger_dir=Orientation.IN,
                                  dominant=True,
                                  start_pos=True),
                             [Finger(index=FingerIndex.THUMB,
                                     properties=[FingerProperty.TAPER,
                                                 FingerProperty.CONTACT]),
                              Finger(index=FingerIndex.INDEX,
                                     properties=[FingerProperty.TAPER,
                                                 FingerProperty.CONTACT]),
                              Finger(index=FingerIndex.MIDDLE,
                                     properties=[FingerProperty.TOGETHER,
                                                 FingerProperty.BENT]),
                              Finger(index=FingerIndex.RING,
                                     properties=[FingerProperty.TOGETHER,
                                                 FingerProperty.BENT]),
                              Finger(index=FingerIndex.PINKY,
                                     properties=[FingerProperty.TOGETHER,
                                                 FingerProperty.BENT])])

    hand_Dui_1tc_234bc = Hand(Palm(palm_dir=Orientation.UP,
                                   finger_dir=Orientation.IN,
                                   dominant=True,
                                   start_pos=True),
                              [Finger(index=FingerIndex.THUMB,
                                      properties=[FingerProperty.TAPER,
                                                  FingerProperty.CONTACT]),
                               Finger(index=FingerIndex.INDEX,
                                      properties=[FingerProperty.TAPER,
                                                  FingerProperty.CONTACT]),
                               Finger(index=FingerIndex.MIDDLE,
                                      properties=[FingerProperty.CONTACT,
                                                  FingerProperty.BENT]),
                               Finger(index=FingerIndex.RING,
                                      properties=[FingerProperty.CONTACT,
                                                  FingerProperty.BENT]),
                               Finger(index=FingerIndex.PINKY,
                                      properties=[FingerProperty.CONTACT,
                                                  FingerProperty.BENT])])

    hand_Dui_234bc_1tc_0c = Hand(Palm(palm_dir=Orientation.UP,
                                      finger_dir=Orientation.IN,
                                      dominant=True,
                                      start_pos=True),
                                 [Finger(index=FingerIndex.THUMB,
                                         properties=[FingerProperty.BENT,
                                                     FingerProperty.CONTACT]),
                                  Finger(index=FingerIndex.INDEX,
                                         properties=[FingerProperty.TAPER,
                                                     FingerProperty.CONTACT]),
                                  Finger(index=FingerIndex.MIDDLE,
                                         properties=[FingerProperty.CONTACT,
                                                     FingerProperty.BENT]),
                                  Finger(index=FingerIndex.RING,
                                         properties=[FingerProperty.CONTACT,
                                                     FingerProperty.BENT]),
                                  Finger(index=FingerIndex.PINKY,
                                         properties=[FingerProperty.CONTACT,
                                                     FingerProperty.BENT])])

    hand_Dui_0123s_4rc = Hand(Palm(palm_dir=Orientation.UP,
                                   finger_dir=Orientation.IN,
                                   dominant=True,
                                   start_pos=True),
                              [Finger(index=FingerIndex.THUMB,
                                      properties=[FingerProperty.STRAIGHT,
                                                  FingerProperty.SPREAD]),
                               Finger(index=FingerIndex.INDEX,
                                      properties=[FingerProperty.STRAIGHT,
                                                  FingerProperty.SPREAD]),
                               Finger(index=FingerIndex.MIDDLE,
                                      properties=[FingerProperty.STRAIGHT,
                                                  FingerProperty.SPREAD]),
                               Finger(index=FingerIndex.RING,
                                      properties=[FingerProperty.STRAIGHT,
                                                  FingerProperty.SPREAD]),
                               Finger(index=FingerIndex.PINKY,
                                      properties=[FingerProperty.CONTACT,
                                                  FingerProperty.ROUND])])

    hand_Dui_0tc_123s_4rc = Hand(Palm(palm_dir=Orientation.UP,
                                      finger_dir=Orientation.IN,
                                      dominant=True,
                                      start_pos=True),
                                 [Finger(index=FingerIndex.THUMB,
                                         properties=[FingerProperty.TAPER,
                                                     FingerProperty.CONTACT]),
                                  Finger(index=FingerIndex.INDEX,
                                         properties=[FingerProperty.STRAIGHT,
                                                     FingerProperty.SPREAD]),
                                  Finger(index=FingerIndex.MIDDLE,
                                         properties=[FingerProperty.STRAIGHT,
                                                     FingerProperty.SPREAD]),
                                  Finger(index=FingerIndex.RING,
                                         properties=[FingerProperty.STRAIGHT,
                                                     FingerProperty.SPREAD]),
                                  Finger(index=FingerIndex.PINKY,
                                         properties=[FingerProperty.CONTACT,
                                                     FingerProperty.ROUND])])

    assert hand_Dui_1tc == parse_hand('Dsui 1tc', parseAll=True)
    assert hand_Dui_1tc_234b == parse_hand('Dsui 1tc 234b', parseAll=True)
    assert hand_Dui_1tc_234bc == parse_hand('Dsui 1tc 234bc', parseAll=True)
    assert hand_Dui_234bc_1tc_0c == parse_hand('Dsui 234bc 1tc 0c',
                                               parseAll=True)
    assert hand_Dui_0123s_4rc == parse_hand('Dui 0123s 4rc', parseAll=True)
    assert hand_Dui_0tc_123s_4rc == parse_hand('Dui 0tc 123s 4rc', parseAll=True)


def test_parse_hand_extra_fingers():
    hand_NDeob = Hand(Palm(palm_dir=Orientation.OUT,
                           finger_dir=Orientation.BODY,
                           dominant=False,
                           start_pos=False),
                      [Finger(index=FingerIndex.THUMB,
                              properties=[FingerProperty.FOLDED]),
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

    assert hand_NDeob == parse_hand('NDeob 0- 1+ 23+s 4+ 13r', parseAll=True)
