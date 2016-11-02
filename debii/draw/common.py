"""Functions to draw common shapes and do common transformations"""
from enum import Enum
import numpy as np


class CommonStrEnum(Enum):
    pass


class Ellipse(object):
    def __init__(self, cx, cy, rx, ry, fill=False, line_width=0.059016,
                 color='black'):
        super(Ellipse, self).__init__()

        self.cx = cx
        self.cy = cy
        self.rx = rx
        self.ry = ry
        self.fill = fill
        self.line_width = line_width
        self.color = color

    def draw(self, ctx):
        ctx.save()
        if self.color == 'black':
            ctx.set_source_rgb(0, 0, 0)
        elif self.color == 'white':
            ctx.set_source_rgb(1.0, 1.0, 1.0)
        ctx.set_line_width(self.line_width)
        ctx.save()

        ctx.translate(self.cx, self.cy)
        ctx.scale(self.rx, self.ry)
        ctx.arc(0.0, 0.0, 1.0, 0.0, 2 * np.pi)
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
                       self.line_width, self.color)

    def __repr__(self):
        s = ('Ellipse(cx=%f, cy=%f, rx=%f, ry=%f, fill=%s, line_width=%f,' +
             ' color=%s')
        return s % (self.cx, self.cy, self.rx, self.ry, str(self.fill),
                    self.line_width, self.color)

    def __eq__(self, other):
        params = [self.cx, self.cy, self.rx, self.ry, self.fill,
                  self.line_width]
        other_params = [other.cx, other.cy, other.rx, other.ry, other.fill,
                        other.line_width]
        return np.isclose(params, other_params)


class Line(object):
    def __init__(self, x1, y1, x2, y2, width=0.02623, color='black'):
        self.x1 = float(x1)
        self.y1 = float(y1)
        self.x2 = float(x2)
        self.y2 = float(y2)
        self.width = float(width)
        self.color = color

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
        if self.color == 'black':
            ctx.set_source_rgb(0, 0, 0)
        elif self.color == 'red':
            ctx.set_source_rgb(1, 0, 0)
        elif self.color == 'green':
            ctx.set_source_rgb(0, 1, 0)
        elif self.color == 'white':
            ctx.set_source_rgb(1, 1, 1)
        ctx.set_line_width(self.width)
        ctx.move_to(self.x1, self.y1)
        ctx.line_to(self.x2, self.y2)
        ctx.stroke()
        ctx.restore()

    def scale(self, alpha):
        dx = self.x2 - self.x1
        dy = self.y2 - self.y1

        return Line(self.x1,
                    self.y1,
                    self.x1 + alpha * dx,
                    self.y1 + alpha * dy,
                    width=self.width,
                    color=self.color)

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return ('Line(x1=%f, y1=%f, x2=%f, y2=%f, width=%f, color=%s)' %
                (self.x1, self.y1, self.x2, self.y2, self.width,
                 repr(self.color)))

    def __eq__(self, other):
        params = [self.x1, self.y1, self.x2, self.y2, self.width, self.color]
        other_params = [other.x1, other.y1, other.x2, other.y2, other.width,
                        other.color]

        return params == other_params


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

    def __repr__(self):
        s = ('FilledArc(cx=%f, cy=%f, rx=%f, ry=%f, line_width=%f, '+
             'start_radians=%f, end_radians=%f)')
        return s % (self.cx, self.cy, self.rx, self.ry,
              self.line_width, self.start_radians, self.end_radians)

    def __eq__(self, other):
        if not super().__eq__(other):
            return false
        return ([self.start_radians, self.end_radians] == 
                [other.start_radians, other.end_radians])


class Triangle(object):
    def __init__(self, cx, cy, v, width=0.02623, color='black'):
        super().__init__()
        self.cx = float(cx)
        self.cy = float(cy)
        self.v = v
        self.width = float(width)
        self.color = color

    def draw(self, ctx):
        ctx.save()
        ctx.set_source_rgb(0, 0, 0)
        ctx.set_line_width(self.width)
        ctx.save()

        R = rotation_matrix(2.0 * np.pi / 3.0)
        S = np.array([[1.0, 0.0], [0.0, -1.0]])
        p1 = self.v
        p2 = R.dot(self.v)
        p3 = R.dot(p2)

        p1 = S.dot(p1)
        p2 = S.dot(p2)
        p3 = S.dot(p3)

        ctx.translate(self.cx, self.cy)
        ctx.move_to(p1[0], p1[1])
        ctx.line_to(p2[0], p2[1])
        ctx.line_to(p3[0], p3[1])
        ctx.line_to(p1[0], p1[1])
        ctx.restore()
        ctx.fill()
        ctx.restore()

    def __eq__(self, other):
        params = [self.cx, self.cy, self.width]
        other_params = [other.cx, other.cy, other.width]
        if not np.all(np.isclose(params, other_params)):
            return False
        if not self.color == other.color:
            return False
        if not np.all(np.isclose(self.v, other.v)):
            return False
        return True

    def __repr__(self):
        s = 'Triangle(cx=%f, cy=%f, v=%f, width=%f, color=%s)'
        return s % (self.cx, self.cy, self.v, self.width, str(self.color))


class Diamond(object):
    def __init__(self, cx, cy, v, width=0.03, color='black'):
        super().__init__()
        self.cx = cx
        self.cy = cy
        self.v = v
        self.width = width
        self.color = color

    def draw(self, ctx):
        ctx.save()
        ctx.set_source_rgb(0, 0, 0)
        ctx.set_line_width(self.width)
        ctx.save()

        R = rotation_matrix(np.pi / 2.0)
        M = np.array([[1.0, 0.0], [0.0, -1.0]])
        S = np.array([[0.8, 0.0], [0.0, 0.8]])
        p1 = self.v
        p2 = R.dot(self.v)
        p3 = R.dot(p2)
        p4 = R.dot(p3)

        p1 = M.dot(p1)
        p2 = S.dot(p2)

        p2 = M.dot(p2)
        p3 = M.dot(p3)

        p4 = S.dot(p4)
        p4 = M.dot(p4)

        ctx.translate(self.cx, self.cy)
        ctx.move_to(p1[0], p1[1])
        ctx.line_to(p2[0], p2[1])
        ctx.line_to(p3[0], p3[1])
        ctx.line_to(p4[0], p4[1])
        ctx.line_to(p1[0], p1[1])
        ctx.restore()
        ctx.stroke()
        ctx.restore()

    def __eq__(self, other):
        params = [self.cx, self.cy, self.width]
        other_params = [other.cx, other.cy, other.width]
        if not np.all(np.isclose(params, other_params)):
            return False
        if not self.color == other.color:
            return False
        if not np.all(np.isclose(self.v, other.v)):
            return False
        return True

    def __repr__(self):
        s = 'Diamond(cx=%f, cy=%f, v=%f, width=%f, color=%s)'
        return s % (self.cx, self.cy, self.v, self.width, str(self.color))


def car2pol(v):
    rho = np.linalg.norm(v)
    phi = np.arctan2(v[1], v[0])
    return rho, phi


def pol2car(rho, phi):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)

    return x, y


def norm_angle(phi):
    while phi < 0:
        phi += 2 * np.pi
    while phi >= 2 * np.pi:
        phi -= 2 * np.pi
    return phi


def directed_angle(v1, v2):
    return np.arctan2(v2[1], v2[0]) - np.arctan2(v1[1], v1[0])


def is_counter_clockwise(v2, v1):
    r = np.cross(v2, v1)
    return (r < 0)


def rotation_matrix(theta):
    return np.array([[np.cos(theta), -np.sin(theta)],
                     [np.sin(theta), np.cos(theta)]])


def scale_matrix(scale_x, scale_y):
    return np.array([[float(scale_x), 0.0],
                     [0.0, float(scale_y)]])
