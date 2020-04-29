from math import log, sqrt
from scipy.stats import norm


def black_scholes(forward, strike, time_to_expiry, volatility):
    if forward < 0.0:
        raise Exception("Forward cannot be negative")
    if strike < 0.0:
        raise Exception(" Stike cannot be negative")
    d1 = (log(forward/strike) +
          volatility**2*time_to_expiry/2.0)/volatility/sqrt(time_to_expiry)
    d2 = d1 - volatility*sqrt(time_to_expiry)
    return forward*norm.cdf(d1) - strike*norm.cdf(d2)
