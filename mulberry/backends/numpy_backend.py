import numpy as np

from ..backend import Backend

class NumpyBackend:
    def invert(T):
        return np.linalg.inv(T)

    def compose(T1, T2):
        return np.matmul(T1, T2)

Backend.register(NumpyBackend)