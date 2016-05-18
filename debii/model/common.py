"""Functions to draw common shapes and do common transformations"""
import math
from enum import Enum
import numpy as np


class CommonStrEnum(Enum):
    def __str__(self):
        return self.value


class Ellipse(object):
    def __init__(self, cx, cy, rx, ry, fill=False, line_width=0.059016):
        super(Ellipse, self).__init__()

        self.cx = cx
        self.cy = cy
        self.rx = rx
        self.ry = ry
        self.fill = fill
        self.line_width = line_width

    def draw(self, ctx):
        ctx.save()
        ctx.set_source_rgb(0, 0, 0)
        ctx.set_line_width(self.line_width)
        ctx.save()

        ctx.translate(self.cx, self.cy)
        ctx.scale(self.rx, self.ry)
        ctx.arc(0.0, 0.0, 1.0, 0.0, 2 * math.pi)
        ctx.restore()

        if not self.fill:
            ctx.stroke()
        else:
            ctx.fill()
        ctx.restore()

    def cointains_point(self, x, y):
        radiasX = self.rx + self.line_width
        radiasY = self.ry + self.line_width
        a = ((x - self.cx) * (x - self.cx)) / (radiasX * radiasX)
        b = ((y - self.cy) * (y - self.cy)) / (radiasY * radiasY)

        return a + b <= 1

    def filled(self):
        return Ellipse(self.cx, self.cy, self.rx, self.ry, True,
                       self.line_width)


class Line(object):
    def __init__(self, x1, y1, x2, y2, width=0.02623):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.width = width

    def norm_vector(self):
        v = np.array([self.x2, self.y2]) - np.array([self.x1, self.y1])
        return v / np.linalg.norm(v)

    def around_start(self, r, width=0.02623):
        u = self.norm_vector()
        v1 = np.array([self.x1, self.y1]) - r * u
        v2 = np.array([self.x1, self.y1]) + r * u

        return Line(v1[0], v1[1], v2[0], v2[1], width=self.width)

    def draw(self, ctx):
        ctx.save()
        ctx.set_source_rgb(0, 0, 0)
        ctx.set_line_width(self.width)
        ctx.move_to(self.x1, self.y1)
        ctx.line_to(self.x2, self.y2)
        ctx.stroke()
        ctx.restore()


class FilledArc(Ellipse):
    def __init__(self, cx, cy, rx, ry, start_radians, end_radians,
                 line_width=0.02623):
        super(FilledArc, self).__init__(cx, cy, rx, ry, fill=False,
                                        line_width=line_width)
        self.start_radians = start_radians
        self.end_radians = end_radians

    def cointains_point(self, x, y):
        inEllipse = super(FilledArc, self).cointains_point(x, y)
        if not inEllipse:
            return False

    def draw(self, ctx):
        ctx.save()
        ctx.set_source_rgb(0, 0, 0)
        ctx.set_line_width(self.line_width)
        ctx.save()

        ctx.translate(self.cx, self.cy)
        ctx.scale(self.rx, self.ry)
        ctx.arc(0.0, 0.0, 1.0, self.start_radians, self.end_radians)
        ctx.restore()
        ctx.fill()
        ctx.restore()


def rotate(ctx, w, h, radias):
    ctx.translate(w / 2.0, h / 2.0)
    ctx.rotate(radias)
    ctx.translate(-w / 2.0, -h / 2.0)

    return ctx


def flip_over_y(ctx, w, h):
    ctx.translate(0, h)
    ctx.scale(1, -1)
    return ctx


def flip_over_x(ctx, w, h):
    ctx.translate(w, 0)
    ctx.scale(-1, 1)
    return ctx
