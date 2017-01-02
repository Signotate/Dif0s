import cairo
from ...util import all_orients
from ..unit.draw.cairo_test_utils import cairo_surface
from ...draw import draw_hand


if __name__ == '__main__':
    for hand in all_orients():
        surface = cairo_surface(100, 100)
        ctx = cairo.Context(surface)
        
        ctx.save()
        ctx.translate(50, 50)
        ctx.scale(50, 50)
        draw_hand(hand, ctx)
        ctx.restore()

        ctx.show_page()
        surface.write_to_png(str(hand) + '.png')
