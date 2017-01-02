import cairo
import numpy as np


def cairo_surfaces_equal(expected, actual):
    assert isinstance(expected, cairo.ImageSurface)
    assert isinstance(actual, cairo.ImageSurface)

    assert expected.get_format() == actual.get_format()
    assert expected.get_data() == actual.get_data()


def cairo_surface(width, height):
    return cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)


def lines_similar(line1, line2):
    l1 = np.array([line1.x1, line1.y1, line1.x2, line1.y2])
    l2 = np.array([line2.x1, line2.y1, line2.x2, line2.y2])

    if not np.all(np.isclose(l1, l2)):
        return False
    if not np.isclose(line1.width, line2.width):
        return False
    if not line1.color == line2.color:
        return False
    return True
