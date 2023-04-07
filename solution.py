import pandas as pd
import numpy as np

from scipy.stats import norm, chi2


chat_id = 720721680 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> float:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    n = len(x)
    s = sum(list(map(lambda i: i**2, x)))
    left_chi = chi2.ppf(1 - alpha / 2, df = 2*len(x)-2)
    rigth_chi = chi2.ppf(alpha / 2, df = 2*len(x)-2)
    left = np.sqrt( s / (40 * left_chi))
    right = np.sqrt( s / (40 * rigth_chi))
    return left, \
           right
