from abc import ABC, abstractstaticmethod

import numpy as np

__all__ = [
    'BaseGate',
    'XGate',
    'HGate',
]


class BaseGate(ABC):

    @abstractstaticmethod
    def apply(*qubits):
        pass

    @abstractstaticmethod
    def reverse(*qubits):
        pass


class XGate(BaseGate):
    """X (Not) Gate"""

    @staticmethod
    def apply(qubit):
        qubit.zero, qubit.one = qubit.one, qubit.zero
        return np.array([[qubit.zero, qubit.one]])

    @staticmethod
    def reverse(qubit):
        return XGate.apply(qubit)


class HGate(BaseGate):
    """Hadamard Gate"""

    H_matrix = np.array([[1, 1], [1, -1]]) * (1.0 / np.sqrt(2))
    
    @staticmethod
    def apply(qubit):
        vec = np.array([[qubit.zero],[qubit.one]])
        vec = HGate.H_matrix @ vec

        qubit.zero = vec[0][0]
        qubit.one = vec[1][0]

        return vec

    @staticmethod
    def reverse(qubit):
        return HGate.apply(qubit)
