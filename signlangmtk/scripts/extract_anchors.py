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

import sys
import xml.etree.ElementTree as etree
from pprint import pprint

filename = sys.argv[1]
sortVar = sys.argv[2]
reverse = False

if len(sys.argv) == 4 and sys.argv[3] == 'r':
    reverse = True

sortIndex = 0
if sortVar == 'y':
    sortIndex = 1

tree = etree.parse(filename)
root = tree.getroot()

anchors = {}
for child in root.iter('{http://www.w3.org/2000/svg}g'):
    color = child.attrib['{http://www.inkscape.org/namespaces/inkscape}label']
    if color == 'Palm':
        for ellipse in child.iter('{http://www.w3.org/2000/svg}circle'):
            cx = float(ellipse.attrib['cx'])
            cy = float(ellipse.attrib['cy'])
            r = float(ellipse.attrib['r'])
            anchors[color] = [cx, cy, r, r]
        for ellipse in child.iter('{http://www.w3.org/2000/svg}ellipse'):
            cx = float(ellipse.attrib['cx'])
            cy = float(ellipse.attrib['cy'])
            rx = float(ellipse.attrib['rx'])
            ry = float(ellipse.attrib['ry'])
            anchors[color] = [cx, cy, rx, ry]
    else:
        anchors[color] = []
        circles = []
        for circle in child.iter('{http://www.w3.org/2000/svg}circle'):
            #pprint(circle.attrib)
            #print("Label:", color, "; cx:", circle.attrib['cx'])
            cx = float(circle.attrib['cx'])
            cy = float(circle.attrib['cy'])
            r = float(circle.attrib['r'])
            circles.append([cx, cy, r])
        circles = sorted(circles, key=lambda t: t[sortIndex], reverse=reverse)
        if len(circles) == 4:
            for i, c in enumerate(circles):
                circles[i].insert(0, i + 1)
        elif len(circles) == 5:
            for i, c in enumerate(circles):
                circles[i].insert(0, i)
        elif len(circles) == 1:
            for i, c in enumerate(circles):
                circles[i].insert(0, -1)

        anchors[color] = circles

pprint(anchors)
