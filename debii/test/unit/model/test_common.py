from ....draw.common import pol2car
from ....draw.common import car2pol
import math


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
