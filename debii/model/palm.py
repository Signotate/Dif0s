"""Model of palm positions"""
from collections import namedtuple
import math
from .common import rotate
from .common import flip_over_y
from .common import flip_over_x
from .common import CommonStrEnum
from .common import Ellipse
from .common import FilledArc


class Orientation(CommonStrEnum):
    """Palm and finger orientations"""

    UP = 'u'
    DOWN = 'd'
    FORWARD = 'f'
    BODY = 'b'
    IN = 'i'
    OUT = 'o'


class PalmPosition(object):
    """The position of a palm in a sign"""

    def __init__(self, palm_direction, finger_direction, dominant=True):
        self._palm_direction = palm_direction
        self._finger_direction = finger_direction
        self._dominant = dominant

    @property
    def palm_direction(self):
        return self._palm_direction

    @property
    def finger_direction(self):
        return self._finger_direction

    @property
    def dominant(self):
        return self._dominant

    def dominant_palm_position(self):
        return PalmPosition(self.palm_direction, self.finger_direction,
                            dominant=True)

    def nondominant_palm_position(self):
        return PalmPosition(self.palm_direction, self.finger_direction,
                            dominant=False)

    def draw(self, ctx):
        print(self)
        ctx.save()
        base_ctx = palm_contexts.get(self.dominant_palm_position(), None)
        ctx = transform_palm(ctx,
                             self.dominant,
                             base_ctx.mirror,
                             base_ctx.flip,
                             base_ctx.rotation)

        ellipse = palm_ellipses[base_ctx.palm]
        if base_ctx.fill:
            ellipse.filled().draw(ctx)
        else:
            ellipse.draw(ctx)
            arc = palm_arcs.get(base_ctx.palm, None)
            if arc is not None:
                arc.draw(ctx)

        palm_draw_functions[base_ctx.palm](ctx)
        ctx.restore()

    def __hash__(self):
        return hash((self.palm_direction,
                     self.finger_direction,
                     self.dominant))

    def __eq__(self, other):
        this_tuple = (self.palm_direction,
                      self.finger_direction,
                      self.dominant)
        other_tuple = (other.palm_direction,
                       other.finger_direction,
                       other.dominant)

        return this_tuple == other_tuple

    def __repr__(self):
        s = 'PalmPosition('
        s += 'palm_direction=' + str(self.palm_direction) + ', '
        s += 'finger_direction=' + str(self.finger_direction) + ', '
        s += 'dominant=' + str(self.dominant)
        s += ')'

        return s

    def __str__(self):
        s = ''
        if self.dominant:
            s = 'D'
        else:
            s = 'ND'
        s += str(self.palm_direction)
        s += str(self.finger_direction)

        return s


# All the palm positions for the dominant hand
Dfu = PalmPosition(Orientation.FORWARD, Orientation.UP)
Dfd = PalmPosition(Orientation.FORWARD, Orientation.DOWN)
Dfi = PalmPosition(Orientation.FORWARD, Orientation.IN)
Dfo = PalmPosition(Orientation.FORWARD, Orientation.OUT)

Dbu = PalmPosition(Orientation.BODY, Orientation.UP)
Dbd = PalmPosition(Orientation.BODY, Orientation.DOWN)
Dbi = PalmPosition(Orientation.BODY, Orientation.IN)
Dbo = PalmPosition(Orientation.BODY, Orientation.OUT)

Dif = PalmPosition(Orientation.IN, Orientation.FORWARD)
Dib = PalmPosition(Orientation.IN, Orientation.BODY)
Diu = PalmPosition(Orientation.IN, Orientation.UP)
Did = PalmPosition(Orientation.IN, Orientation.DOWN)

Dof = PalmPosition(Orientation.OUT, Orientation.FORWARD)
Dob = PalmPosition(Orientation.OUT, Orientation.BODY)
Dou = PalmPosition(Orientation.OUT, Orientation.UP)
Dod = PalmPosition(Orientation.OUT, Orientation.DOWN)

Duf = PalmPosition(Orientation.UP, Orientation.FORWARD)
Dub = PalmPosition(Orientation.UP, Orientation.BODY)
Dui = PalmPosition(Orientation.UP, Orientation.IN)
Duo = PalmPosition(Orientation.UP, Orientation.OUT)

Ddi = PalmPosition(Orientation.DOWN, Orientation.IN)
Ddo = PalmPosition(Orientation.DOWN, Orientation.OUT)
Ddf = PalmPosition(Orientation.DOWN, Orientation.FORWARD)
Ddb = PalmPosition(Orientation.DOWN, Orientation.DOWN)


# map each palm position to its base palm
BasePalmCtx = namedtuple('BasePalmCtx', 'palm mirror flip fill rotation')

palm_contexts = {Dfu: BasePalmCtx(Dfu, False, False, False, None),
                 Dfd: BasePalmCtx(Dfu, False, False, False, math.pi),
                 Dfi: BasePalmCtx(Dfu, False, False, False, -math.pi / 2.0),
                 Dfo: BasePalmCtx(Dfu, False, False, False, math.pi / 2.0),

                 Dbu: BasePalmCtx(Dfu, False, False, True, None),
                 Dbd: BasePalmCtx(Dfu, False, False, True, math.pi),
                 Dbi: BasePalmCtx(Dfu, False, False, True, -math.pi / 2.0),
                 Dbo: BasePalmCtx(Dfu, False, False, True, math.pi / 2.0),

                 Dif: BasePalmCtx(Dif, False, False, False, None),
                 Dib: BasePalmCtx(Dif, False, True, False, None),
                 Diu: BasePalmCtx(Diu, False, False, False, None),
                 Did: BasePalmCtx(Diu, False, True, False, None),

                 Dof: BasePalmCtx(Dif, False, False, True, math.pi),
                 Dob: BasePalmCtx(Dif, False, True, True, math.pi),
                 Dou: BasePalmCtx(Diu, True, False, True, None),
                 Dod: BasePalmCtx(Diu, False, False, True, math.pi),

                 Duf: BasePalmCtx(Duf, False, False, False, None),
                 Dub: BasePalmCtx(Dub, False, False, False, None),
                 Dui: BasePalmCtx(Ddi, False, True, False, None),
                 Duo: BasePalmCtx(Diu, False, False, False, math.pi / 2.0),

                 Ddi: BasePalmCtx(Ddi, False, False, False, None),
                 Ddo: BasePalmCtx(Diu, False, True, False, -math.pi / 2.0),
                 Ddf: BasePalmCtx(Dif, False, False, True, -math.pi / 2.0),
                 Ddb: BasePalmCtx(Dif, False, False, True, math.pi / 2.0)}


palm_ellipses = {Dfu: Ellipse(0.474492, 0.604754, 0.265738, 0.265738),
                 Ddi: Ellipse(0.389967, 0.453508, 0.284361, 0.151049),
                 Diu: Ellipse(0.471311, 0.659016, 0.161902, 0.302623),
                 Dub: Ellipse(0.393902, 0.589934, 0.302623, 0.161902),
                 Duf: Ellipse(0.606098, 0.470066, 0.302623, 0.161902),
                 Dif: Ellipse(0.333453, 0.611709, 0.159246, 0.297541)}


palm_arcs = {Dif: FilledArc(0.343289, 0.611709, 0.159246, 0.297541,
                            math.pi / 2.0, 3 * math.pi / 2.0),
             Ddi: FilledArc(0.389967, 0.453508, 0.284361, 0.151049,
                            0, math.pi),
             Dui: FilledArc(0.471311, 0.659016, 0.161902, 0.302623,
                            math.pi / 2.0, 3 * math.pi / 2.0)}


def draw_dif_palm(cairo_ctx, fill=False):
    # set_palm_source(cairo_ctx)

    # draw_ellipse(cairo_ctx, 101.70307, 186.57112, 48.57, 90.75, fill=fill)
    # if not fill:
        # draw_fill_arc(cairo_ctx, 104.70307, 186.57112, 48.57, 90.75,
        #               math.pi / 2.0, 3 * math.pi / 2.0)
    cairo_ctx.set_line_width(0.03)
    cairo_ctx.move_to(1/2.0, 1/2.0)
    cairo_ctx.line_to(1, 1/2.0)
    cairo_ctx.stroke()
    cairo_ctx.set_source_rgb(1, 0, 0)
    cairo_ctx.move_to(1/2.0, 1/2.0)
    cairo_ctx.line_to(1/2.0, 0)
    cairo_ctx.stroke()

    return cairo_ctx


def draw_dfu_palm(cairo_ctx, fill=False):
    # set_palm_source(cairo_ctx)

    # draw_ellipse(cairo_ctx, 144.72, 184.45, 81.05, 81.05, fill=fill)
    cairo_ctx.set_line_width(0.03)
    cairo_ctx.move_to(1/2.0, 1/2.0)
    cairo_ctx.line_to(1/2.0, 0)
    cairo_ctx.stroke()
    cairo_ctx.set_source_rgb(1, 0, 0)
    cairo_ctx.move_to(1/2.0, 1/2.0)
    cairo_ctx.line_to(1, 1/2.0)
    cairo_ctx.stroke()

    return cairo_ctx


def draw_ddi_palm(cairo_ctx, fill=False):
    # set_palm_source(cairo_ctx)

    # draw_ellipse(cairo_ctx, 118.94, 138.32, 86.73, 46.07, fill=fill)
    # if not fill:
        # draw_fill_arc(cairo_ctx, 118.94, 138.32, 86.73, 46.07, 0, math.pi)
    cairo_ctx.set_line_width(0.03)
    cairo_ctx.move_to(1/2.0, 1/2.0)
    cairo_ctx.line_to(1, 1/2.0)
    cairo_ctx.stroke()
    cairo_ctx.set_source_rgb(1, 0, 0)
    cairo_ctx.move_to(1/2.0, 1/2.0)
    cairo_ctx.line_to(1/2.0, 0)
    cairo_ctx.stroke()

    return cairo_ctx


def draw_diu_palm(cairo_ctx, fill=False):
    # set_palm_source(cairo_ctx)

    # draw_ellipse(cairo_ctx, 143.75, 201, 49.38, 92.30, fill=fill)
    # if not fill:
        # draw_fill_arc(cairo_ctx, 143.75, 201, 49.38, 92.30, math.pi / 2, 3 *
        #               math.pi / 2.0)
    cairo_ctx.set_line_width(0.03)
    cairo_ctx.move_to(1/2.0, 1/2.0)
    cairo_ctx.line_to(1/2.0, 0)
    cairo_ctx.set_line_width(0.03)
    cairo_ctx.stroke()
    cairo_ctx.set_source_rgb(1, 0, 0)
    cairo_ctx.move_to(1/2.0, 1/2.0)
    cairo_ctx.line_to(1, 1/2.0)
    cairo_ctx.stroke()

    return cairo_ctx


def draw_dub_palm(cairo_ctx, fill=False):
    # set_palm_source(cairo_ctx)

    # draw_ellipse(cairo_ctx, 120.14, 179.93, 92.30, 49.38, fill=fill)
    cairo_ctx.set_line_width(0.03)
    cairo_ctx.move_to(1/2.0, 1/2.0)
    cairo_ctx.line_to(1/2.0, 0)
    cairo_ctx.stroke()
    cairo_ctx.set_source_rgb(1, 0, 0)
    cairo_ctx.move_to(1/2.0, 1/2.0)
    cairo_ctx.line_to(1, 1/2.0)
    cairo_ctx.stroke()

    return cairo_ctx


def draw_duf_palm(cairo_ctx, fill=False):
    # set_palm_source(cairo_ctx)

    # draw_ellipse(cairo_ctx, 184.86, 143.37, 92.30, 49.38, fill=fill)
    cairo_ctx.set_line_width(0.03)
    cairo_ctx.move_to(1/2.0, 1/2.0)
    cairo_ctx.line_to(1/2.0, 1)
    cairo_ctx.stroke()
    cairo_ctx.set_source_rgb(1, 0, 0)
    cairo_ctx.move_to(1/2.0, 1/2.0)
    cairo_ctx.line_to(0, 1/2.0)
    cairo_ctx.stroke()

    return cairo_ctx


palm_draw_functions = {Dfu: draw_dfu_palm,
                       Dif: draw_dif_palm,
                       Diu: draw_diu_palm,
                       Duf: draw_duf_palm,
                       Dub: draw_dub_palm,
                       Ddi: draw_ddi_palm}


_PALM_IMAGE_SIZE = 1


def transform_palm(ctx, dominant=True, mirror=False, flip=False,
                   rotation=None):
    if flip:
        ctx = flip_palm(ctx)
    if mirror:
        ctx = mirror_palm(ctx)
    if not dominant:
        ctx = mirror_palm(ctx)
    if rotation is not None:
        rotate_palm(ctx, rotation)

    return ctx


def set_palm_source(cairo_ctx):
    cairo_ctx.set_source_rgb(0, 0, 0)
    cairo_ctx.set_line_width(18)


def rotate_palm(ctx, radias):
    return rotate(ctx, _PALM_IMAGE_SIZE, _PALM_IMAGE_SIZE, radias)


def mirror_palm(ctx):
    return flip_over_x(ctx, _PALM_IMAGE_SIZE, _PALM_IMAGE_SIZE)


def flip_palm(ctx):
    return flip_over_y(ctx, _PALM_IMAGE_SIZE, _PALM_IMAGE_SIZE)
