from signlangmtk.model import *


def test_hand_init():
    h = Hand(Palm(palm_dir=Orientation.FORWARD,
                  finger_dir=Orientation.UP,
                  dominant=True,
                  start_pos=True), [])

    assert h.palm == Palm(Orientation.FORWARD, Orientation.UP)
    assert len(h.fingers) == 5
    for f in h.fingers:
        assert {FingerProperty.FOLDED} == f.properties

    assert h.is_valid()

    # simple contact case
    expected_hand = Hand(Palm(palm_dir=Orientation.UP,
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

    actual_hand = Hand(Palm(palm_dir=Orientation.UP,
                            finger_dir=Orientation.IN,
                            dominant=True,
                            start_pos=True),
                       [Finger(index=FingerIndex.INDEX,
                               properties=[FingerProperty.TAPER,
                                           FingerProperty.CONTACT])])

    assert expected_hand == actual_hand
    assert expected_hand.is_valid()

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

    actual_hand = Hand(Palm(palm_dir=Orientation.UP,
                            finger_dir=Orientation.IN,
                            dominant=True,
                            start_pos=True),
                       [Finger(index=FingerIndex.INDEX,
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

    assert hand_Dui_1tc_234bc == actual_hand
    assert not actual_hand.is_valid()

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

    actual_hand = Hand(Palm(palm_dir=Orientation.UP,
                            finger_dir=Orientation.IN,
                            dominant=True,
                            start_pos=True),
                       [Finger(index=FingerIndex.THUMB,
                               properties=[FingerProperty.SPREAD]),
                        Finger(index=FingerIndex.INDEX,
                               properties=[FingerProperty.SPREAD]),
                        Finger(index=FingerIndex.MIDDLE,
                               properties=[FingerProperty.SPREAD]),
                        Finger(index=FingerIndex.RING,
                               properties=[FingerProperty.SPREAD]),
                        Finger(index=FingerIndex.PINKY,
                               properties=[FingerProperty.CONTACT,
                                           FingerProperty.ROUND])])

    assert hand_Dui_0123s_4rc == actual_hand
    assert not actual_hand.is_valid()

    expected_hand = Hand(Palm(palm_dir=Orientation.UP,
                              finger_dir=Orientation.IN,
                              dominant=True,
                              start_pos=True),
                         [Finger(index=FingerIndex.THUMB,
                                 properties=[FingerProperty.ROUND,
                                             FingerProperty.CONTACT]),
                          Finger(index=FingerIndex.INDEX,
                                 properties=[FingerProperty.ROUND,
                                             FingerProperty.CONTACT]),
                          Finger(index=FingerIndex.MIDDLE,
                                 properties=[FingerProperty.FOLDED]),
                          Finger(index=FingerIndex.RING,
                                 properties=[FingerProperty.FOLDED]),
                          Finger(index=FingerIndex.PINKY,
                                 properties=[FingerProperty.FOLDED])])

    actual_hand = Hand(Palm(palm_dir=Orientation.UP,
                            finger_dir=Orientation.IN,
                            dominant=True,
                            start_pos=True),
                       [Finger(index=FingerIndex.INDEX,
                               properties=[FingerProperty.ROUND,
                                           FingerProperty.CONTACT])])

    assert expected_hand == actual_hand
    assert actual_hand.is_valid()

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

    actual_hand = Hand(Palm(palm_dir=Orientation.UP,
                                      finger_dir=Orientation.IN,
                                      dominant=True,
                                      start_pos=True),
                                 [Finger(index=FingerIndex.THUMB,
                                         properties=[FingerProperty.TAPER,
                                                     FingerProperty.CONTACT]),
                                  Finger(index=FingerIndex.INDEX,
                                         properties=[FingerProperty.SPREAD]),
                                  Finger(index=FingerIndex.MIDDLE,
                                         properties=[FingerProperty.SPREAD]),
                                  Finger(index=FingerIndex.RING,
                                         properties=[FingerProperty.SPREAD]),
                                  Finger(index=FingerIndex.PINKY,
                                         properties=[FingerProperty.CONTACT,
                                                     FingerProperty.ROUND])])

    assert hand_Dui_0tc_123s_4rc == actual_hand
    assert not actual_hand.is_valid()


def test_init_edge_cases():
    expected_hand = Hand(Palm(palm_dir=Orientation.UP,
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

    thumb = Finger(index=FingerIndex.THUMB)
    thumb._properties = set([])
    actual_hand = Hand(Palm(palm_dir=Orientation.UP,
                            finger_dir=Orientation.IN,
                            dominant=True,
                            start_pos=True),
                       [Finger(index=FingerIndex.INDEX,
                               properties=[FingerProperty.TAPER,
                                           FingerProperty.CONTACT]),
                        thumb])

    assert expected_hand == actual_hand
    assert actual_hand.is_valid()

    actual_hand = Hand(Palm(palm_dir=Orientation.UP,
                           finger_dir=Orientation.IN,
                           dominant=True,
                           start_pos=True),
                      [Finger(index=FingerIndex.INDEX,
                              properties=[FingerProperty.TAPER,
                                          FingerProperty.CONTACT]),
                       thumb])
    fingers = list(actual_hand.fingers)
    actual_hand._fingers = fingers[1:]
    assert not actual_hand.is_valid()

def test_eq():
    p1 = Palm(Orientation.UP, Orientation.IN)
    p2 = Palm(Orientation.DOWN, Orientation.IN)

    fingers1 = [Finger(FingerIndex.INDEX, properties=[FingerProperty.BENT,
                                                      FingerProperty.TOGETHER]),
                Finger(FingerIndex.PINKY, properties=[FingerProperty.FOLDED])]

    fingers2 = [Finger(FingerIndex.INDEX, properties=[FingerProperty.ROUND,
                                                      FingerProperty.TOGETHER]),
                Finger(FingerIndex.THUMB, properties=[FingerProperty.FOLDED])]

    h1 = Hand(p1, [])
    h2 = Hand(p1, [])
    assert h1 == h2
    assert h2 == h1

    h2 = Hand(p2, fingers1)
    assert h1 != h2
    assert h2 != h1

    h1 = Hand(p1, fingers1)
    h2 = Hand(p1, fingers1)

    assert h1 == h2
    assert h2 == h1

    h2 = Hand(p1, fingers2)

    assert h1 != h2
    assert h2 != h1