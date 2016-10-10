import sys
import cairo
from ...model.palm import parse_palm
from ...draw import draw_palm2
from ...draw import draw_orient_vectors2
from ...draw import draw_orient_thumb
from ...draw import draw_test_fingers
#from ...draw import draw_demo_fingers

if __name__ == "__main__":
    p = parse_palm(sys.argv[1])
    print(repr(p))

    surface = cairo.SVGSurface('build_test.svg', 1600, 1600)
    ctx = cairo.Context(surface)
    ctx.save()
    ctx.translate(50.0, 50.0)
    ctx.scale(50.0, 50.0)

    draw_palm2(p, ctx)
    #draw_orient_thumb(p, ctx)
    draw_orient_vectors2(p, ctx)
    #draw_test_fingers(p, ctx)
    #draw_demo_fingers(p, ctx)

    ctx.show_page()
