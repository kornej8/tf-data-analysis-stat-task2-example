import pandas as pd
import numpy as np

from scipy.stats import norm, chi2


chat_id = 720721680 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> float:
    alpha = 1 - p
    n = len(x)
    s = sum([(x_i - x.mean())**2 for x_i in list(x)]) / n
    left_chi = chi2.ppf(1 - alpha / 2, df = 2*len(x))
    rigth_chi = chi2.ppf(alpha / 2, df = 2*len(x))
    left = np.sqrt(((n-1) * s**2) / (40 * left_chi))
    right = np.sqrt(((n-1) * s**2) / (40 * left_chi))
    return left, \
           right
