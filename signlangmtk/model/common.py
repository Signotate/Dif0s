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

"""A simple model of a palm position"""

from uuid import uuid4 as uuid
from collections import namedtuple

# Uniquely identifies a sign
# One sign will have several Segments
SegmentIndex = namedtuple('SegmentIndex', ['transcript_id',
                                           'paragraph_n',
                                           'sentence_n',
                                           'clause_n',
                                           'sign_n'])


class SignSegment(object):
    def __init__(self, **kwargs):
        super().__init__()
        self.id = kwargs.pop('id', uuid())
        self.index = kwargs.pop('index', None)
        # list of SignSegment ids
        self.compounds = kwargs.pop('compounds', [])

        self.raw_config = kwargs.pop('raw_config', None)
        self.common_name = kwargs.pop('common_name', None)
        self.body_part = kwargs.pop('body_part', None)

        self.time = kwargs.pop('time', None)
        self.body_side = kwargs.pop('body_size', None)
        self.features = kwargs.pop('features', [])


FeatureValue = namedtuple('FeatureValue', 'key value')


class SegmentFeature(object):
    def __init__(self, **kwargs):
        self.id = kwargs.pop('id', uuid())
        self.name = kwargs.pop('name', None)
        self.values = [FeatureValue(k, v) for k, v in kwargs]
        self._values_index = {v.key: v.value for v in self.values}

    def __getattr__(self, item):
        if hasattr(self, item):
            super().__getattr__(item)
        elif item in self._values_index:
            return self._values_index[item]
        else:
            raise AttributeError('SegmentFeature has not attribute \'{}\''
                                 .format(str(item)))


class SegmentMeta(object):
    def __init__(self, **kwargs):
        super().__init__()
        self.id = kwargs.pop('id', uuid())
        self.index = kwargs.pop('index', None)