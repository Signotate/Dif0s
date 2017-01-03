import logging
from collections import OrderedDict
from pyparsing import Literal, Optional, Word, OneOrMore, ZeroOrMore
from signlangmtk.model.palm import Orientation
from signlangmtk.model.palm import Palm
from signlangmtk.model.finger import FingerIndex
from signlangmtk.model.finger import FingerProperty
from signlangmtk.model.finger import Finger
from signlangmtk.model.hand import Hand


logger = logging.getLogger(__name__)


def convert_dominant(tokens):
    return 'D' == tokens[0]


def convert_start(tokens):
    return 's' == tokens[0]


def convert_orient(tokens):
    return Orientation.parse(tokens[0])


def convert_index(tokens):
    return FingerIndex.parse(tokens[0])


def convert_finger_prop(tokens):
    return FingerProperty.parse(tokens[0])


def create_palm(tokens):
    return Palm(**(tokens.asDict()['palm']))


def create_hand(tokens):
    fingers = [f for f in tokens if type(f) == Finger]
    return Hand(tokens.palm, fingers)


def create_fingers(tokens):
    logger.debug('tokens: %s' % tokens)
    finger_confs = OrderedDict()
    index_group = tuple([])
    last_token = None
    for t in tokens:
        if type(t) == FingerIndex and type(last_token) != FingerIndex:
            index_group = [t]
        elif type(t) == FingerIndex:
            index_group.append(t)
        else:
            grp = tuple(index_group)
            if grp not in finger_confs:
                finger_confs[grp] = []
            finger_confs[grp].append(t)
        last_token = t

    logger.debug('finger_confs: %s' % list(finger_confs.items()))

    fingers = []
    for indices, properties in finger_confs.items():
        index_list = indices
        if len(indices) == 0:
            index_list = list(FingerIndex)
        for i in index_list:
            f = Finger(i, properties)
            fingers.append(f)
    logger.debug('Parsed Fingers: %s' % fingers)
    return fingers


which_hand = (Optional(Literal('N'))
              + Literal('D')).setParseAction(convert_dominant)('dominant')
start_end = (Literal('s') | Literal('e')).setParseAction(
    convert_start)('start_pos')

orient = Word('iofbud', exact=1).setParseAction(convert_orient)

finger_index = Word('01234', exact=1)('f_index').setParseAction(convert_index)
finger_property = Word('-+xstcrb',
                       exact=1)('f_prop').setParseAction(convert_finger_prop)


palm = (which_hand('dominant')
        + Optional(start_end)
        + orient('palm_dir')
        + orient('finger_dir'))('palm').setParseAction(create_palm)


finger_props = OneOrMore(finger_property)
finger_indices = OneOrMore(finger_index)


finger_conf = ZeroOrMore(
    finger_index | finger_property)('fingers').setParseAction(create_fingers)


hand = (palm + finger_conf)('hand').setParseAction(create_hand)


if __name__ == '__main__':
    r = hand.parseString('Deui tc ', parseAll=True)
    print(r)
    r = hand.parseString('Deui 13tc 24t ', parseAll=True)
    print(r)
    r = hand.parseString('Deui tc 54yy ', parseAll=True)
    print(r)
