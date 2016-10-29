import sys
import cairo
from ...model.palm import parse_palm
from ...draw import draw_palm
from ...draw import draw_orient_vectors
from ...draw import draw_fingers
from ...draw.common import Triangle
import numpy as np

if __name__ == "__main__":
    #p = parse_palm(sys.argv[1])
    #print(repr(p))

    surface = cairo.SVGSurface('triangle_test.svg', 1600, 1600)
    ctx = cairo.Context(surface)

    Triangle(50.0, 50.0, np.array([-20.0, 0.0])).draw(ctx)

    #ctx.save()
    #ctx.translate(50.0, 50.0)
    #ctx.scale(50.0, 50.0)

    #draw_palm(p, ctx)
    #draw_orient_vectors(p, ctx)
    #draw_fingers(p, ctx)

    ctx.show_page()
