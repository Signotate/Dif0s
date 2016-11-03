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


roundc_fingers = [Finger(FingerIndex.THUMB,
                        [FingerProperty.ROUND,
                         FingerProperty.CONTACT]),
                 Finger(FingerIndex.INDEX,
                        [FingerProperty.ROUND,
                         FingerProperty.CONTACT]),
                 Finger(FingerIndex.MIDDLE,
                        [FingerProperty.ROUND,
                         FingerProperty.CONTACT]),
                 Finger(FingerIndex.RING,
                        [FingerProperty.ROUND,
                         FingerProperty.CONTACT]),
                 Finger(FingerIndex.PINKY,
                        [FingerProperty.ROUND,
                         FingerProperty.CONTACT])]


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


bentt_fingers = [Finger(FingerIndex.THUMB,
                        [FingerProperty.BENT,
                         FingerProperty.TOGETHER]),
                 Finger(FingerIndex.INDEX,
                        [FingerProperty.BENT,
                         FingerProperty.TOGETHER]),
                 Finger(FingerIndex.MIDDLE,
                        [FingerProperty.BENT,
                         FingerProperty.TOGETHER]),
                 Finger(FingerIndex.RING,
                        [FingerProperty.BENT,
                         FingerProperty.TOGETHER]),
                 Finger(FingerIndex.PINKY,
                        [FingerProperty.BENT,
                         FingerProperty.TOGETHER])]


bents_fingers = [Finger(FingerIndex.THUMB,
                        [FingerProperty.BENT,
                         FingerProperty.SPREAD]),
                 Finger(FingerIndex.INDEX,
                        [FingerProperty.BENT,
                         FingerProperty.SPREAD]),
                 Finger(FingerIndex.MIDDLE,
                        [FingerProperty.BENT,
                         FingerProperty.SPREAD]),
                 Finger(FingerIndex.RING,
                        [FingerProperty.BENT,
                         FingerProperty.SPREAD]),
                 Finger(FingerIndex.PINKY,
                        [FingerProperty.BENT,
                         FingerProperty.SPREAD])]


tappers_fingers = [Finger(FingerIndex.THUMB,
                        [FingerProperty.TAPER,
                         FingerProperty.SPREAD]),
                 Finger(FingerIndex.INDEX,
                        [FingerProperty.TAPER,
                         FingerProperty.SPREAD]),
                 Finger(FingerIndex.MIDDLE,
                        [FingerProperty.TAPER,
                         FingerProperty.SPREAD]),
                 Finger(FingerIndex.RING,
                        [FingerProperty.TAPER,
                         FingerProperty.SPREAD]),
                 Finger(FingerIndex.PINKY,
                        [FingerProperty.TAPER,
                         FingerProperty.SPREAD])]


tappert_fingers = [Finger(FingerIndex.THUMB,
                        [FingerProperty.TAPER,
                         FingerProperty.TOGETHER]),
                 Finger(FingerIndex.INDEX,
                        [FingerProperty.TAPER,
                         FingerProperty.TOGETHER]),
                 Finger(FingerIndex.MIDDLE,
                        [FingerProperty.TAPER,
                         FingerProperty.TOGETHER]),
                 Finger(FingerIndex.RING,
                        [FingerProperty.TAPER,
                         FingerProperty.TOGETHER]),
                 Finger(FingerIndex.PINKY,
                        [FingerProperty.TAPER,
                         FingerProperty.TOGETHER])]


tapperc_fingers = [Finger(FingerIndex.THUMB,
                        [FingerProperty.TAPER,
                         FingerProperty.CONTACT]),
                 Finger(FingerIndex.INDEX,
                        [FingerProperty.TAPER,
                         FingerProperty.CONTACT]),
                 Finger(FingerIndex.MIDDLE,
                        [FingerProperty.TAPER,
                         FingerProperty.CONTACT]),
                 Finger(FingerIndex.RING,
                        [FingerProperty.TAPER,
                         FingerProperty.CONTACT]),
                 Finger(FingerIndex.PINKY,
                        [FingerProperty.TAPER,
                         FingerProperty.CONTACT])]


round_bent_fingers = [Finger(FingerIndex.THUMB,
                        [FingerProperty.FOLDED]),
                 Finger(FingerIndex.INDEX,
                        [FingerProperty.STRAIGHT,
                         FingerProperty.SPREAD]),
                 Finger(FingerIndex.MIDDLE,
                        [FingerProperty.ROUND,
                         FingerProperty.SPREAD]),
                 Finger(FingerIndex.RING,
                        [FingerProperty.BENT,
                         FingerProperty.TOGETHER]),
                 Finger(FingerIndex.PINKY,
                        [FingerProperty.BENT,
                         FingerProperty.TOGETHER])]


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
               ('folded', folded),
               ('together', together),
               ('spread', spread),
               ('round', round_fingers),
               ('round_spread', rspread_fingers),
               ('round_contact', roundc_fingers),
               ('bent_together', bentt_fingers),
               ('bent_spread', bents_fingers),
               ('bent_round', round_bent_fingers),
               ('taper_spread', tappers_fingers),
               ('taper_together', tappert_fingers),
               ('taper_contact', tapperc_fingers),
               ('12+', s1),
               ('0+s1+s4s+', s2),
               ('0+s1+2+s3s+4+', s3)
]
