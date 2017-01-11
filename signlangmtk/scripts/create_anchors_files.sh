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

#!/bin/bash
python3 extract_anchors.py Duf.svg x > Duf_anchors.txt 
python3 extract_anchors.py Dub.svg x r > Dub_anchors.txt 
python3 extract_anchors.py Diu.svg x r > Diu_anchors.txt 
python3 extract_anchors.py Dif.svg y r > Dif_anchors.txt 
python3 extract_anchors.py Dfu.svg x r > Dfu_anchors.txt 
python3 extract_anchors.py Ddi.svg y r > Ddi_anchors.txt
