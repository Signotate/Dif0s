from .grammar import hand


def parse_hand(s, parseAll=False):
    tokens = hand.parseString(s, parseAll=False)
    if tokens is not None and len(tokens) > 0:
        return tokens[0]
    else:
        raise ParseException('Error parsing hand string \'' + s + '\'')
