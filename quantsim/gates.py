from abc import abstractstaticmethod

import numpy as np

__all__ = [
    'BaseGate',
    'IGate',
    'I',
    'XGate',
    'X',
    'HGate',
    'H',
    'ZGate',
    'Z',
    'SGate',
    'S',
    'TGate',
    'T',
    'R8Gate',
    'R8',
    'RxGate',
    'Rx',
    'RzGate',
    'Rz',
    'Measurement',
    'M',
]


class BaseGate():

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

I = IGate()

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

X = XGate()

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

H = HGate()

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

Z = ZGate()

# ====================================================================================================

class SGate(BaseGate):
    """90 Phase-flip Gate"""

    S_matrix = np.sqrt(np.vectorize(complex)(ZGate.Z_matrix))

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

S = SGate()

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

T = TGate()

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

R8 = R8Gate()

# ====================================================================================================

class RxGate(BaseGate):
    """Continuous Phase-flip Gate"""

    theta = 0

    def __call__(self, theta):
        RxGate.theta = theta
        return self
    
    @staticmethod
    def get_matrix():
        theta = RxGate.theta

        return np.array([
            [np.cos(theta/2), -1j*np.sin(theta/2)],
            [-1j*np.sin(theta/2), np.cos(theta/2)]
        ])

    @staticmethod
    def apply(qubit):
        vec = np.array([[qubit.zero],[qubit.one]])
        vec = RxGate.get_matrix() @ vec

        qubit.zero = vec[0][0]
        qubit.one = vec[1][0]

        return vec

    @staticmethod
    def reverse(qubit):
        RxGate.theta = 360 - RxGate.theta
        return RxGate.apply(qubit)

Rx = RxGate()

# ====================================================================================================

class RzGate(BaseGate):
    """Continuous Phase-flip Gate"""

    phi = 0

    def __call__(self, phi):
        RzGate.phi = phi
        return self
    
    @staticmethod
    def get_matrix():
        phi = RzGate.phi

        return np.array([
            [1, 0],
            [0, np.exp(1j*phi/2)]
        ])

    @staticmethod
    def apply(qubit):
        vec = np.array([[qubit.zero],[qubit.one]])
        vec = RzGate.get_matrix() @ vec

        qubit.zero = vec[0][0]
        qubit.one = vec[1][0]

        return vec

    @staticmethod
    def reverse(qubit):
        RzGate.phi = 360 - RzGate.phi
        return RzGate.apply(qubit)

Rz = RzGate()

# ====================================================================================================

class Measurement(BaseGate):
    """Measurement"""

    @staticmethod
    def apply(qubit):
        qubit.measure()
        qubit.display()

    @staticmethod
    def reverse(qubit):
        pass

M = Measurement()

# ====================================================================================================
