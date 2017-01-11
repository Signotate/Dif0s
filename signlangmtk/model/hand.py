# Sign Language Markup Tool Kit
# Tools to model, search and create scalable graphic representations of sign
# language transcripts
#
# Copyright (C) 2016, 2017 Greg Clark
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

"""The model of the hand part of a sign language sign"""


from signlangmtk.model.finger import Finger
from signlangmtk.model.finger import FingerIndex
from signlangmtk.model.finger import FingerProperty


class InvalidHandException(Exception):
    pass


class Hand(object):
    """The universal hand"""

    _default_fingers = {i: Finger(i) for i in list(FingerIndex)}

    def __init__(self, palm, fingers):
        self._palm = palm
        self._fingers = self._determine_fingers(fingers)

    @property
    def palm(self):
        return self._palm

    @property
    def fingers(self):
        return self._fingers

    def _determine_fingers(self, lst):
        fingers = {}
        finger_lst = []
        for f in lst:
            if f.index not in fingers:
                fingers[f.index] = f
                finger_lst.append(f)
        for i, f in ((finger.index, finger) for finger in finger_lst):
            if (FingerProperty.CONTACT in f.properties
                    and i != FingerIndex.THUMB):

                if FingerIndex.THUMB in fingers:
                    thumb = fingers[FingerIndex.THUMB]
                    if (FingerProperty.CONTACT not in thumb.properties
                            and len(thumb.properties) == 0):
                        thumb = Finger(FingerIndex.THUMB, f.properties)
                        fingers[FingerIndex.THUMB] = thumb
                    elif {FingerProperty.CONTACT} == thumb.properties:
                        thumb = Finger(FingerIndex.THUMB, f.properties)
                        fingers[FingerIndex.THUMB] = thumb
                else:
                    thumb = Finger(FingerIndex.THUMB, f.properties)
                    fingers[FingerIndex.THUMB] = thumb

                # only apply for first contact finger
                break

        # fill in missing fingers with defaults
        for i, f in self._default_fingers.items():
            if i not in fingers:
                fingers[i] = f

        return list(fingers.values())

    def __str__(self):
        return str(self.palm)

    def __repr__(self):
        s = 'Hand(palm='
        s += repr(self.palm)
        s += ', fingers='
        s += repr(self.fingers)
        s += ')'
        return s

    def __eq__(self, other):
        if self.palm != other.palm:
            return False
        elif (sorted(self.fingers, key=lambda f: f.index) != 
              sorted(other.fingers, key=lambda f: f.index)):
            return False
        return True

    def is_valid(self):
        return (self.palm.is_valid()
                and all([f.is_valid() for f in self.fingers])
                and self._check_fingers())

    def _check_fingers(self):
        fingers = {f.index: f for f in self.fingers}
        for index in list(FingerIndex):
            if index not in fingers:
                return False

        thumb = fingers[FingerIndex.THUMB]
        contact_props = []
        for index, finger in fingers.items():
            if index != FingerIndex.THUMB:
                if FingerProperty.CONTACT in finger.properties:
                    props = set(finger.properties)
                    props.remove(FingerProperty.CONTACT)
                    contact_props.append(list(props)[0])
                    if FingerProperty.CONTACT not in thumb.properties:
                        return False

        if len(contact_props) > 0:
            thumb_has_contact_prop = False
            for p in contact_props:
                if p in thumb.properties:
                    thumb_has_contact_prop = True

            if not thumb_has_contact_prop:
                return False

        return True
