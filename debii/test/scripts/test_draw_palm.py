import cairo
from ...model.palm import parse_palm
from ...draw import draw_palm
from ...draw import draw_orient_vectors

if __name__ == "__main__":
    p = parse_palm("Ddi")
    print(repr(p))

    surface = cairo.SVGSurface('build_test.svg', 1600, 1600)
    ctx = cairo.Context(surface)
    ctx.save()
    ctx.translate(50.0, 50.0)
    ctx.scale(50.0, 50.0)

    draw_palm(p, ctx)
    draw_orient_vectors(p, ctx)

    ctx.show_page()