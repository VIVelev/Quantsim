import numpy as np

from .base import BaseGate, MatrixGate, SelfInverseGate

__all__ = [
    # Single Qubit Gates
    'IGate', 'I',
    'XGate', 'X',
    'HGate', 'H',
    'ZGate', 'Z',
    'SGate', 'S',
    'TGate', 'T',
    'R8Gate', 'R8',

    # Rotation Gates
    'RxGate', 'Rx',
    'RzGate', 'Rz',

    # Utility Gates
    'Measurement', 'M',
    'Display', 'D',

    # Multi Qubit Gates
    'CNOTGate', 'CNOT',
]


class IGate(MatrixGate):
    """ Identity Gate """

    matrix = np.identity(2)

    def __init__(self):
        super().__init__(IGate.matrix, 'I')

I = IGate()

# ====================================================================================================

class XGate(MatrixGate):
    """ X (Not) Gate """

    matrix = np.array([[0, 1], [1, 0]])

    def __init__(self):
        super().__init__(XGate.matrix, 'X')

X = XGate()

# ====================================================================================================

class HGate(MatrixGate):
    """ Hadamard Gate """

    matrix = np.array([[1, 1], [1, -1]]) * (1.0/np.sqrt(2))

    def __init__(self):
        super().__init__(HGate.matrix, 'H')

H = HGate()

# ====================================================================================================

class ZGate(MatrixGate):
    """ 180 Phase-flip Gate """

    matrix = np.array([[1, 0], [0, -1]])

    def __init__(self):
        super().__init__(ZGate.matrix, 'Z')

Z = ZGate()

# ====================================================================================================

class SGate(MatrixGate):
    """ 90 Phase-flip Gate """

    matrix = np.sqrt(np.vectorize(complex)(ZGate.matrix))

    def __init__(self):
        super().__init__(SGate.matrix, 'S')

S = SGate()

# ====================================================================================================

class TGate(MatrixGate):
    """ 45 Phase-flip Gate """

    matrix = np.sqrt(SGate.matrix)

    def __init__(self):
        super().__init__(TGate.matrix, 'T')

T = TGate()

# ====================================================================================================

class R8Gate(MatrixGate):
    """ 22.5 Phase-flip Gate """

    matrix = np.sqrt(TGate.matrix)

    def __init__(self):
        super().__init__(R8Gate.matrix, 'R8')

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

    @staticmethod
    def reverse(qubit):
        RxGate.theta = 360 - RxGate.theta
        RxGate.apply(qubit)

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

    @staticmethod
    def reverse(qubit):
        RzGate.phi = 360 - RzGate.phi
        RzGate.apply(qubit)

Rz = RzGate()

# ====================================================================================================

class Measurement(SelfInverseGate):
    """ Measurement """

    def __init__(self):
        super().__init__('M')

    def apply(self, *qubits):
        for qubit in qubits:
            qubit.measure()

M = Measurement()

# ====================================================================================================

class Display(SelfInverseGate):
    """ Display """

    def __init__(self):
        super().__init__('D')

    def apply(self, *qubits):
        for qubit in qubits:
            qubit.display()

D = Display()

# ====================================================================================================

class CNOTGate():
    pass

CNOT = CNOTGate()

# ====================================================================================================
