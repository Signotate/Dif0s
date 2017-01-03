import logging
import os
from enum import Enum


def setup_logging(level=logging.DEBUG):
    logging.basicConfig(level=level,
                        format='%(asctime)s [%(levelname)s] %(name)s: %('
                               'funcName)s: %(message)s ')


def resource_location(package, resource):
    directory = os.path.dirname(package.__file__)
    location = os.path.join(directory, resource)
    if not os.path.isfile(location):
        raise Exception('No such resource \'%s\' for package \'%s\''
                        % (package, resource))
    return location


class OrderedEnum(Enum):
    def __ge__(self, other):
        if self.__class__ is other.__class__:
            return self.value >= other.value
        return NotImplemented

    def __gt__(self, other):
        if self.__class__ is other.__class__:
            return self.value > other.value
        return NotImplemented

    def __le__(self, other):
        if self.__class__ is other.__class__:
            return self.value <= other.value
        return NotImplemented

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented
