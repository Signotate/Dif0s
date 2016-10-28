from ...model.finger import Finger
from ...model.finger import FingerIndex
from ...model.finger import FingerProperty


folded = [Finger(FingerIndex.THUMB,
             [FingerProperty.FOLDED]),
      Finger(FingerIndex.INDEX,
             [FingerProperty.FOLDED]),
      Finger(FingerIndex.MIDDLE,
             [FingerProperty.FOLDED]),
      Finger(FingerIndex.RING,
             [FingerProperty.FOLDED]),
      Finger(FingerIndex.PINKY,
             [FingerProperty.FOLDED])]


spread = [Finger(FingerIndex.THUMB,
             [FingerProperty.STRAIGHT,
             FingerProperty.SPREAD]),
      Finger(FingerIndex.INDEX,
             [FingerProperty.STRAIGHT,
             FingerProperty.SPREAD]),
      Finger(FingerIndex.MIDDLE,
             [FingerProperty.STRAIGHT,
             FingerProperty.SPREAD]),
      Finger(FingerIndex.RING,
             [FingerProperty.STRAIGHT,
             FingerProperty.SPREAD]),
      Finger(FingerIndex.PINKY,
             [FingerProperty.STRAIGHT,
             FingerProperty.SPREAD])]


together = [Finger(FingerIndex.THUMB,
             [FingerProperty.STRAIGHT,
             FingerProperty.TOGETHER]),
      Finger(FingerIndex.INDEX,
             [FingerProperty.STRAIGHT,
             FingerProperty.TOGETHER]),
      Finger(FingerIndex.MIDDLE,
             [FingerProperty.STRAIGHT,
             FingerProperty.TOGETHER]),
      Finger(FingerIndex.RING,
             [FingerProperty.STRAIGHT,
             FingerProperty.TOGETHER]),
      Finger(FingerIndex.PINKY,
             [FingerProperty.STRAIGHT,
             FingerProperty.TOGETHER])]


round_fingers = [Finger(FingerIndex.THUMB, 
                        [FingerProperty.ROUND,
                         FingerProperty.TOGETHER]),
                 Finger(FingerIndex.INDEX,
                        [FingerProperty.ROUND,
                         FingerProperty.SPREAD]),
                 Finger(FingerIndex.MIDDLE,
                        [FingerProperty.ROUND,
                         FingerProperty.SPREAD]),
                 Finger(FingerIndex.RING,
                        [FingerProperty.ROUND,
                         FingerProperty.TOGETHER]),
                 Finger(FingerIndex.PINKY,
                        [FingerProperty.ROUND,
                         FingerProperty.TOGETHER])]


rspread_fingers = [Finger(FingerIndex.THUMB, 
                        [FingerProperty.ROUND,
                         FingerProperty.SPREAD]),
                 Finger(FingerIndex.INDEX,
                        [FingerProperty.ROUND,
                         FingerProperty.SPREAD]),
                 Finger(FingerIndex.MIDDLE,
                        [FingerProperty.ROUND,
                         FingerProperty.SPREAD]),
                 Finger(FingerIndex.RING,
                        [FingerProperty.ROUND,
                         FingerProperty.SPREAD]),
                 Finger(FingerIndex.PINKY,
                        [FingerProperty.ROUND,
                         FingerProperty.SPREAD])]


s1 = [Finger(FingerIndex.THUMB,
             [FingerProperty.FOLDED]),
      Finger(FingerIndex.INDEX,
             [FingerProperty.STRAIGHT,
              FingerProperty.TOGETHER]),
      Finger(FingerIndex.MIDDLE,
             [FingerProperty.STRAIGHT,
              FingerProperty.TOGETHER]),
      Finger(FingerIndex.RING,
             [FingerProperty.FOLDED]),
      Finger(FingerIndex.PINKY,
             [FingerProperty.FOLDED])]


s2 = [Finger(FingerIndex.THUMB,
             [FingerProperty.STRAIGHT,
             FingerProperty.SPREAD]),
      Finger(FingerIndex.INDEX,
             [FingerProperty.STRAIGHT,
              FingerProperty.SPREAD]),
      Finger(FingerIndex.MIDDLE,
             [FingerProperty.FOLDED]),
      Finger(FingerIndex.RING,
             [FingerProperty.FOLDED]),
      Finger(FingerIndex.PINKY,
             [FingerProperty.STRAIGHT,
             FingerProperty.SPREAD])]


s3 = [Finger(FingerIndex.THUMB,
             [FingerProperty.STRAIGHT,
             FingerProperty.SPREAD]),
      Finger(FingerIndex.INDEX,
             [FingerProperty.STRAIGHT,
              FingerProperty.TOGETHER]),
      Finger(FingerIndex.MIDDLE,
             [FingerProperty.STRAIGHT,
              FingerProperty.SPREAD]),
      Finger(FingerIndex.RING,
             [FingerProperty.STRAIGHT,
              FingerProperty.SPREAD]),
      Finger(FingerIndex.PINKY,
             [FingerProperty.STRAIGHT,
             FingerProperty.TOGETHER])]


finger_sets = [
               #('folded', folded),
               #('together', together),
               #('spread', spread),
               ('round', round_fingers),
               ('round_spread', rspread_fingers)
               #('12+', s1),
               #('0+s1+s4s+', s2),
               #('0+s1+2+s3s+4+', s3)
]
