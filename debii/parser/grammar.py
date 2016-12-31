from collections import OrderedDict
from pyparsing import Literal, Optional, Word, OneOrMore, ZeroOrMore
from ..model.palm import Orientation
from ..model.palm import Palm
from ..model.finger import FingerIndex
from ..model.finger import FingerProperty
from ..model.finger import Finger
from ..model.hand import Hand


def convertDominant(tokens):
    return 'D' == tokens[0]


def convertStart(tokens):
    return 's' == tokens[0]


def convertOrient(tokens):
    return Orientation.parse(tokens[0])


def convertIndex(tokens):
    return FingerIndex.parse(tokens[0])


def convertFingerProp(tokens):
    return FingerProperty.parse(tokens[0])


def createPalm(tokens):
    return Palm(**(tokens.asDict()['palm']))


def createHand(tokens):
    fingers = [f for f in tokens if type(f) == Finger]
    return Hand(tokens.palm, fingers)


def createFingers(tokens):
    print('tokens:', tokens)
    finger_confs = OrderedDict()
    index_group = tuple([])
    last_token = None
    for t in tokens:
        if type(t) == FingerIndex and type(last_token) != FingerIndex:
            index_group = []
            index_group.append(t)
        elif type(t) == FingerIndex:
            index_group.append(t)
        else:
            grp = tuple(index_group)
            if grp not in finger_confs:
                finger_confs[grp] = []
            finger_confs[grp].append(t)
        last_token = t

    print('finger_confs:', list(finger_confs.items()))

    fingers = []
    for indices, properties in finger_confs.items():
        index_list = indices
        if len(indices) == 0:
            index_list = list(FingerIndex)
        for i in index_list:
            f = Finger(i, properties)
            fingers.append(f)
    print('Parsed Fingers:', fingers)
    return fingers


which_hand = (Optional(Literal('N'))
              + Literal('D')).setParseAction(convertDominant)('dominant')
start_end = (Literal('s') | Literal('e')).setParseAction(
    convertStart)('start_pos')

orient = Word('iofbud', exact=1).setParseAction(convertOrient)

finger_index = Word('01234', exact=1)('f_index').setParseAction(convertIndex)
finger_property = Word('-+xstcrb',
                       exact=1)('f_prop').setParseAction(convertFingerProp)


palm = (which_hand('dominant')
        + Optional(start_end)
        + orient('palm_dir')
        + orient('finger_dir'))('palm').setParseAction(createPalm)


finger_props = OneOrMore(finger_property)
finger_indices = OneOrMore(finger_index)


finger_conf = ZeroOrMore(
    finger_index | finger_property)('fingers').setParseAction(createFingers)


hand = (palm + finger_conf)('hand').setParseAction(createHand)


if __name__ == '__main__':
    r = hand.parseString('Deui tc ', parseAll=True)
    print(r)
    r = hand.parseString('Deui 13tc 24t ', parseAll=True)
    print(r)
    r = hand.parseString('Deui tc 54yy ', parseAll=True)
    print(r)
