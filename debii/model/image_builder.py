"""Contains functions to build hand position images from HandPosition
objects"""

import cairo
from cairo import Matrix
import math
from palm import Duf, Dif, Dib
from common import Line


def read_anchors(filename):
    with open(filename, 'r') as infile:
        return eval(infile.read())


def build_hand_position_context(hand_pos):
    anchors = read_anchors('scripts/Ddi_anchors.txt')
    palm_cx, palm_cy, palm_rx, palm_ry = anchors['Palm']

    image_size = 305

    surface = cairo.SVGSurface('build_test.svg', 305, 305)
    ctx = cairo.Context(surface)

    ctx.set_source_rgb(0, 0, 0)
    ctx.set_line_width(18)
    ctx.save()

    # draw ellipse
    ctx.translate(palm_cx, palm_cy)
    ctx.scale(palm_rx, palm_ry)
    ctx.arc(0.0, 0.0, 1.0, 0.0, 2 * math.pi)
    ctx.restore()
    ctx.stroke()

    # ctx.save()

    # ctx.translate(118.94, 138.32)
    # ctx.scale(86.73, 46.07)
    # ctx.arc(0.0, 0.0, 1.0, math.pi, 2 * math.pi)
    # ctx.restore()
    # ctx.fill()

    ctx.set_line_width(12)
    ctx.move_to(182, 305 - 200)
    ctx.line_to(195, 305 - 227)
    ctx.stroke()

    ctx.show_page()


if __name__ == '__main__':
    surface = cairo.SVGSurface('build_test.svg', 1600, 1600)
    ctx = cairo.Context(surface)
    ctx.save()

    # ctx.scale(1.0 / 305, 1.0 / 305)
    ctx.scale(100, 100)
    Duf.dominant_palm_position().draw(ctx)

    ctx.set_matrix(Matrix())
    ctx.translate(100, 100)
    ctx.scale(100, 100)
    Dib.draw(ctx)

    ctx.set_matrix(Matrix())
    ctx.set_dash([20, 20])
    line = Line(0, 200, 200, 0, width=8)
    line.draw(ctx)

    ctx.show_page()
