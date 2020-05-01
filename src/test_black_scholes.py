from derivatives_maths import black_scholes
from pytest import raises

def test_call_price():
    F = 1.1
    K = 1.0
    T = 1.0
    vol = 0.2
    value = black_scholes(F, K, T, vol)
    assert(value > F - K)


def test_errors():
    with raises(Exception):
        black_scholes(-1.1, 1.0, 1.0, 0.2)
    with raises(Exception):
        black_scholes(1.1, -1.0, 1.0, 0.2)