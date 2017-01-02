from signlangmtk.draw.common import directed_angle
from signlangmtk.draw.common import is_counter_clockwise
from signlangmtk.draw.common import car2pol
import math
import numpy as np


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
    assert not is_counter_clockwise(np.array([1.0, 0.0]),
                                    np.array([0.0, 1.0]))
    assert not is_counter_clockwise(np.array([0.0, 1.0]),
                                    np.array([-1.0, 0.0]))
    assert not is_counter_clockwise(np.array([-1.0, 0.0]),
                                    np.array([0.0, -1.0]))
    assert not is_counter_clockwise(np.array([0.0, -1.0]),
                                    np.array([1.0, 0.0]))

    assert is_counter_clockwise(np.array([1.0, 0.0]),
                                np.array([0.0, -1.0]))
    assert is_counter_clockwise(np.array([0.0, -1.0]),
                                np.array([-1.0, 0.0]))
    assert is_counter_clockwise(np.array([-1.0, 0.0]),
                                np.array([0.0, 1.0]))
    assert is_counter_clockwise(np.array([0.0, 1.0]),
                                np.array([1.0, 0.0]))


def test_car2pol():
    rho, phi = car2pol((0.0, 1.0))
    assert rho == 1.0
    assert phi == math.pi / 2.0

    rho, phi = car2pol((1.0, 0.0))
    assert rho == 1.0
    assert phi == 0.0

    rho, phi = car2pol((-1.0, 0.0))
    assert rho == 1.0
    assert phi == math.pi

    rho, phi = car2pol((0.0, -1.0))
    print(rho, phi)
    assert rho == 1
    assert phi == -math.pi / 2.0
