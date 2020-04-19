from derivatives_maths import black_scholes


def test_call_price():
    F = 1.1
    K = 1.0
    T = 1.0
    vol = 0.2
    value = black_scholes(F, K, T, "Call", vol)
    assert(value > F - K)
