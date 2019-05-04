from abc import ABC, abstractstaticmethod

import numpy as np

__all__ = [
    'BaseGate',
    'IGate',
    'XGate',
    'HGate',
    'ZGate',
    'SGate',
    'TGate',
    'R8Gate',
    'RxGate',
    'RzGate',
]


class BaseGate(ABC):

    @abstractstaticmethod
    def apply(*qubits):
        pass

    @abstractstaticmethod
    def reverse(*qubits):
        pass

# ====================================================================================================
# ====================================================================================================

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

# ====================================================================================================

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

# ====================================================================================================

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

# ====================================================================================================

class ZGate(BaseGate):
    """180 Phase-flip Gate"""

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

# ====================================================================================================

class SGate(BaseGate):
    """90 Phase-flip Gate"""

    S_matrix = np.sqrt(ZGate.Z_matrix)

    @staticmethod
    def apply(qubit):
        vec = np.array([[qubit.zero],[qubit.one]])
        vec = SGate.S_matrix @ vec

        qubit.zero = vec[0][0]
        qubit.one = vec[1][0]

        return vec

    @staticmethod
    def reverse(qubit):
        return ZGate.reverse(SGate.apply(qubit))

# ====================================================================================================

class TGate(BaseGate):
    """45 Phase-flip Gate"""

    T_matrix = np.sqrt(SGate.S_matrix)

    @staticmethod
    def apply(qubit):
        vec = np.array([[qubit.zero],[qubit.one]])
        vec = TGate.T_matrix @ vec

        qubit.zero = vec[0][0]
        qubit.one = vec[1][0]

        return vec

    @staticmethod
    def reverse(qubit):
        return SGate.reverse(TGate.apply)

# ====================================================================================================

class R8Gate(BaseGate):
    """22.5 Phase-flip Gate"""

    R8_matrix = np.sqrt(TGate.T_matrix)

    @staticmethod
    def apply(qubit):
        vec = np.array([[qubit.zero],[qubit.one]])
        vec = R8Gate.R8_matrix @ vec

        qubit.zero = vec[0][0]
        qubit.one = vec[1][0]

        return vec

    @staticmethod
    def reverse(qubit):
        return TGate.reverse(R8Gate.apply)

# ====================================================================================================
