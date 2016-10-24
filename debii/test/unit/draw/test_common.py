from ....draw.common import directed_angle
from ....draw.common import is_counter_clockwise
import math
import numpy as np
from numpy.testing import assert_almost_equal


def test_directed_angle():
    assert math.pi / 2.0 == directed_angle(np.array([1.0, 0.0]),
                                           np.array([0.0, 1.0]))
    assert math.pi / 2.0 == directed_angle(np.array([0.0, 1.0]),
                                           np.array([-1.0, 0.0]))
    assert -3 * math.pi / 2.0 == directed_angle(np.array([-1.0, 0.0]),
                                                np.array([0.0, -1.0]))
    assert math.pi / 2.0 == directed_angle(np.array([0.0, -1.0]),
                                           np.array([1.0, 0.0]))


def test_is_counter_clockwise():
    assert False == is_counter_clockwise(np.array([1.0, 0.0]),
                                           np.array([0.0, 1.0]))
    assert False == is_counter_clockwise(np.array([0.0, 1.0]),
                                           np.array([-1.0, 0.0]))
    assert False == is_counter_clockwise(np.array([-1.0, 0.0]),
                                           np.array([0.0, -1.0]))
    assert False == is_counter_clockwise(np.array([0.0, -1.0]),
                                           np.array([1.0, 0.0]))

    assert True == is_counter_clockwise(np.array([1.0, 0.0]),
                                           np.array([0.0, -1.0]))
    assert True == is_counter_clockwise(np.array([0.0, -1.0]),
                                           np.array([-1.0, 0.0]))
    assert True == is_counter_clockwise(np.array([-1.0, 0.0]),
                                           np.array([0.0, 1.0]))
    assert True == is_counter_clockwise(np.array([0.0, 1.0]),
                                           np.array([1.0, 0.0]))
