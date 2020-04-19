from math import log, sqrt
from scipy.stats import norm


def black_scholes(forward, strike, time_to_expiry, payoff, volatility):
    eta = 1.0 if payoff == "Call" else -1.0
    d1 = (log(forward/strike) +
          volatility**2*time_to_expiry/2.0)/volatility/sqrt(time_to_expiry)
    d2 = d1 - volatility*sqrt(time_to_expiry)
    return eta*(forward*norm.cdf(d1) - strike*norm.cdf(d2))
