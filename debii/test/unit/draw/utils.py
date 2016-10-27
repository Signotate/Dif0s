import cairo


def cairo_surfaces_equal(expected, actual):
    assert isinstance(expected, cairo.ImageSurface)
    assert isinstance(actual, cairo.ImageSurface)

    assert expected.get_format() == actual.get_format()
    assert expected.get_data() == actual.get_data()


def cairo_surface(width, height):
    return cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
