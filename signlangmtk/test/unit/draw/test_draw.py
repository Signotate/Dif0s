import cairo
import os
from signlangmtk.draw import draw_hand
from signlangmtk.test.unit.draw.utils import cairo_surfaces_equal
from signlangmtk.test.unit.draw.utils import cairo_surface
from signlangmtk.test.utils import all_orients
from signlangmtk.draw import draw_hand
from nose.tools import nottest


# TODO enable this when surface.get_data() is implemented in python3
@nottest
def test_draw_folded_hands():
    test_dir = os.path.dirname(__file__)
    for hand in all_orients():
        filename = os.path.join(test_dir, 
                                'test_images',
                                'all_orients_folded',
                                str(hand.palm) + '.png')
        with open(filename, 'rb') as f:
            expected_surface = cairo.ImageSurface.create_from_png(f)

        actual_surface = cairo_surface(100, 100)
        ctx = cairo.Context(actual_surface)
        ctx.translate(50.0, 50.0)
        ctx.scale(50.0, 50.0)
        draw_hand(hand, ctx)
        
        cairo_surfaces_equal(expected_surface, actual_surface)
