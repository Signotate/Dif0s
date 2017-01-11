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

HAND_MAJOR_RADIUS = 1.0
HAND_MINOR_RADIUS = 0.5
HAND_CIRCLE_RADIUS = 0.7071067811865476

# size of palm relative to size of whole hand
PALM_SIZE_RATIO = 0.5

PALM_MAJOR_RADIUS = HAND_MAJOR_RADIUS * PALM_SIZE_RATIO
PALM_MINOR_RADIUS = HAND_MINOR_RADIUS * PALM_SIZE_RATIO
PALM_CIRCLE_RADIUS = HAND_CIRCLE_RADIUS * PALM_SIZE_RATIO
