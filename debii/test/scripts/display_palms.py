"""Display all the palm positions"""

import sys
import cairo
from ...model.palm import palm_contexts


FILENAME = sys.argv[1]


def compute_full_size(palm_size):
    num_palms = len(palm_contexts)
    width = palm_size * 2
    height = num_palms * palm_size
    offset = 30
    height += offset

    # draw table
    surface = cairo.SVGSurface(FILENAME, width, height)
    ctx = cairo.Context(surface)
    ctx.save()

    ctx.set_source_rgb(0, 0, 0)
    ctx.move_to(0, offset)
    ctx.line_to(width, offset)
    ctx.stroke()

    ctx.move_to(width / 2.0, 0)
    ctx.line_to(width / 2.0, height)
    ctx.stroke()

    ctx.select_font_face('Sans')
    ctx.set_font_size(12)
    ctx.move_to(10, 24)
    ctx.show_text('Dominant')

    ctx.move_to(width / 2.0 + 10, 24)
    ctx.show_text('Non-dominant')

    ctx.save()
    for i, p in enumerate(sorted(palm_contexts.keys(), key=str)):
        # ctx.set_matrix(Matrix())
        nondominant_palm = p.nondominant_palm_position()

        pos = offset + i * 100
        ctx.move_to(0, pos)
        ctx.line_to(width, pos)
        ctx.stroke()

        ctx.move_to(2, pos + 10)
        ctx.set_font_size(10)
        ctx.show_text(str(p))
        ctx.stroke()

        ctx.move_to(width / 2.0 + 2, pos + 10)
        ctx.set_font_size(10)
        ctx.show_text(str(nondominant_palm))
        ctx.stroke()
        ctx.save()

        ctx.translate(0, pos)
        ctx.scale(palm_size, palm_size)
        p.draw(ctx)
        ctx.restore()
        ctx.save()

        ctx.translate(width / 2.0, pos)
        ctx.scale(palm_size, palm_size)
        nondominant_palm.draw(ctx)
        ctx.restore()

    ctx.show_page()


if __name__ == "__main__":
    compute_full_size(100)
