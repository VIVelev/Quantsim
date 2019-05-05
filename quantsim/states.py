from numpy import sqrt
from .qubit import Qubit

__all__ = [
    'ket'
]


def ket(sym):
    states = {
        '0': Qubit(1, 0),
        '1': Qubit(0, 1),
        '+': Qubit(1/sqrt(2), 1/sqrt(2)),
        '-': Qubit(1/sqrt(2), -1/sqrt(2)),
    }

    return states[sym]
