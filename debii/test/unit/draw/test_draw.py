from ....draw import is_offsets_reversed


def test_is_offsets_reversed():
    zero = [1.0, 0.0]
    pi_by_2 = [0.0, 1.0]
    pi = [-1.0, 0.0]
    three_pi_by_2 = [0.0, -1.0]

    assert not is_offsets_reversed(zero, pi_by_2)
    assert not is_offsets_reversed(pi_by_2, pi)
    assert not is_offsets_reversed(pi, three_pi_by_2)
    assert not is_offsets_reversed(three_pi_by_2, zero)

    assert is_offsets_reversed(zero, three_pi_by_2)
    assert is_offsets_reversed(three_pi_by_2, pi)
    assert is_offsets_reversed(pi, pi_by_2)
    assert is_offsets_reversed(pi_by_2, zero)
