from abc import ABC, abstractstaticmethod

import numpy as np

__all__ = [
    'BaseGate',
    'XGate',
    'HGate',
    'IGate',
    'ZGate',
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

    X_matrix = np.array([[0, 1], [1, 0]])

    @staticmethod
    def apply(qubit):
        vec = np.array([[qubit.zero],[qubit.one]])
        vec = XGate.X_matrix @ vec

        qubit.zero = vec[0][0]
        qubit.one = vec[1][0]

        return vec

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


class IGate(BaseGate):
    """Identity Gate"""

    I_matrix = np.array([[1, 0], [0, 1]])

    @staticmethod
    def apply(qubit):
        vec = np.array([[qubit.zero],[qubit.one]])
        vec = IGate.I_matrix @ vec

        qubit.zero = vec[0][0]
        qubit.one = vec[1][0]

        return vec

    @staticmethod
    def reverse(qubit):
        return IGate.apply(qubit)


class ZGate(BaseGate):
    """Phase-flip Gate"""

    Z_matrix = np.array([[1, 0], [0, -1]])

    @staticmethod
    def apply(qubit):
        vec = np.array([[qubit.zero],[qubit.one]])
        vec = ZGate.Z_matrix @ vec

        qubit.zero = vec[0][0]
        qubit.one = vec[1][0]

        return vec

    @staticmethod
    def reverse(qubit):
        return ZGate.apply(qubit)
