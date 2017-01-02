from pyparsing import ParseException
from signlangmtk.parser.grammar import hand


def parse_hand(s, parseAll=False):
    tokens = hand.parseString(s, parseAll=parseAll)
    if tokens is not None and len(tokens) > 0:
        return tokens[0]
    else:
        raise ParseException('Error parsing hand string \'' + s + '\'')


def is_hand_string(s):
    return hand.matches(s, parseAll=True)
