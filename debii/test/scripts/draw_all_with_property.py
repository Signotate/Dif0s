import sys
import cairo
from ...model.palm import parse_palm
from ...model.palm import Orientation
from ...model.palm import Palm
from ...model.finger import FingerIndex
from ...model.finger import FingerProperty
from ...model.finger import Finger
from ...model.hand import Hand
from ...draw import draw_palm
from ...draw import draw_orient_vectors
from ...draw import draw_fingers
from ...draw import draw_hand
from ...draw.common import Line
from ...util import setup_logging


def draw_grid(ctx, total_size, cell_size, props):
    labels_x = ['', 'F Up', 'F Down', 'F In', 'F Out', 'F Forward', 'F Body']
    labels_y = ['', 'P Forward', 'P Body', 'P In', 'P Out', 'P Up', 'P Down']

    finger_orients = [None,
                      Orientation.UP,
                      Orientation.DOWN,
                      Orientation.IN,
                      Orientation.OUT,
                      Orientation.FORWARD,
                      Orientation.BODY]

    palm_orients = [None,
                    Orientation.FORWARD,
                    Orientation.BODY,
                    Orientation.IN,
                    Orientation.OUT,
                    Orientation.UP,
                    Orientation.DOWN]

    ctx.save()
    for l, x in zip(labels_x, range(0, total_size[0], cell_size[0])):
        Line(x, 0, x, total_size[1], width=2.0).draw(ctx)
        ctx.move_to(x + 10, cell_size[1] / 2.0)
        ctx.set_font_size(16)
        ctx.show_text(l)
        ctx.stroke()
    for l, y in zip(labels_y, range(0, total_size[1], cell_size[1])):
        Line(0, y, total_size[0], y, width=2.0).draw(ctx)
        ctx.move_to(10, y + cell_size[1] / 2.0)
        ctx.set_font_size(16)
        ctx.show_text(l)
        ctx.stroke()
    
    ctx.restore()

    fingers = [Finger(index, props) for index in list(FingerIndex)]

    for o_finger, x in zip(finger_orients, range(0, total_size[0], cell_size[0])):
        for o_palm, y in zip(palm_orients, 
                               range(0, total_size[1], cell_size[1])):
            if (o_palm is not None and o_finger is not None and not
                o_palm.conflicts(o_finger)):
                
                p = Palm(o_palm, o_finger)
                h = Hand(p, fingers)

                ctx.save()
                ctx.translate(x + cell_size[0] / 4.0, y + cell_size[1] / 2.0)
                ctx.scale(cell_size[1] / 2.0 , cell_size[1] / 2.0)
                draw_hand(h, ctx)
                ctx.restore()

                p = Palm(o_palm, o_finger, dominant=False)
                h = Hand(p, fingers)

                ctx.save()
                ctx.translate(x + 3.0 * cell_size[0] / 4.0,
                              y + cell_size[1] / 2.0)
                ctx.scale(cell_size[1] / 2.0 , cell_size[1] / 2.0)
                draw_hand(h, ctx)
                ctx.restore()
            elif (o_palm is not None and o_finger is not None and
                  o_palm.conflicts(o_finger)):

                ctx.save()
                ctx.set_source_rgb(0.5, 0.5, 0.5)
                ctx.rectangle(x, y, cell_size[0], cell_size[1])
                ctx.fill()
                ctx.restore()


if __name__ == "__main__":
    setup_logging()

    surface = cairo.SVGSurface('build_test.svg', 1400, 700)
    ctx = cairo.Context(surface)
    draw_grid(ctx, (1400, 700), (200, 100), [FingerProperty.STRAIGHT,
                                             FingerProperty.SPREAD])
    ctx.show_page()
