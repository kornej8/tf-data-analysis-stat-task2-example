import pandas as pd
import numpy as np

from scipy.stats import norm, chi2


chat_id = 720721680 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> float:
    alpha = 1 - p
    loc = sum(list(map(lambda x: x**2, x)))
    left = np.sqrt(loc / 40 * chi2.ppf(alpha / 2, df = 2*len(x)) / np.sqrt(len(x)))
    right = np.sqrt(loc / 40 * chi2.ppf(1 - alpha / 2, df = 2*len(x)) / np.sqrt(len(x)))
    return left, \
           right
