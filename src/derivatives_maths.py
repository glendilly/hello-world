"""
Derivatives mathematics functions
"""


from math import log, sqrt
from scipy.stats import norm


def black_scholes(forward, strike, time_to_expiry, volatility):
    """
    Black-Scholes pricer
    """
    if forward < 0.0:
        raise Exception("Forward cannot be negative")
    if strike < 0.0:
        raise Exception("Strike cannot be negative")
    d_1 = (log(forward/strike) +
           volatility**2*time_to_expiry/2.0)/volatility/sqrt(time_to_expiry)
    d_2 = d_1 - volatility*sqrt(time_to_expiry)
    return forward*norm.cdf(d_1) - strike*norm.cdf(d_2)
