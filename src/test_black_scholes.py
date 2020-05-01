"""
Test file for Black pricer
"""

from pytest import raises
from derivatives_maths import black_scholes


def test_call_price():
    """
    Test that call price is greater than intrinsic value
    """
    value = black_scholes(1.1, 1.0, 1.0, 0.2)
    assert value > 1.1 - 1.0


def test_errors():
    """
    Test error handling
    """
    with raises(Exception):
        black_scholes(-1.1, 1.0, 1.0, 0.2)
    with raises(Exception):
        black_scholes(1.1, -1.0, 1.0, 0.2)
