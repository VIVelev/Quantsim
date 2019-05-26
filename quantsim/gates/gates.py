import numpy as np

from .base import MatrixGate, RotationGate, SelfInverseGate

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
    'CNOTGate', 'CNOT', 'CX'
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

class RxGate(RotationGate):
    """ Continuous Phase-flip Gate """

    def __init__(self):
        super().__init__('Rx')

    @property
    def matrix(self):
        theta = self._angle

        return np.array([[np.cos(theta/2), -1j*np.sin(theta/2)],
                        [-1j*np.sin(theta/2), np.cos(theta/2)]])

Rx = RxGate()

# ====================================================================================================

class RzGate(RotationGate):
    """ Continuous Phase-flip Gate """

    def __init__(self):
        super().__init__('Rz')

    @property
    def matrix(self):
        phi = self._angle

        return np.array([[1, 0], [0, np.exp(1j*phi/2)]])

Rz = RzGate()

# ====================================================================================================

class Measurement(SelfInverseGate):
    """ Measurement """

    def __init__(self):
        super().__init__('M')

    def apply(self, *qubits):
        super().apply(*qubits)

        for qubit in qubits:
            qubit.measure()

M = Measurement()

# ====================================================================================================

class Display(SelfInverseGate):
    """ Display """

    def __init__(self):
        super().__init__('D')

    def apply(self, *qubits):
        super().apply(*qubits)

        for qubit in qubits:
            qubit.display()

D = Display()

# ====================================================================================================

class CNOTGate(SelfInverseGate):
    """ Controlled Not (X) Gate """
    
    def __init__(self):
        super().__init__('CNOT')
        self._control = 0
        self._target = 1

    def __call__(self, control, target):
        self._control = control-1
        self._target = target-1
        return self

    def apply(self, bits):
        super().apply(*bits)

        for i in range(len(bits)):
            if bits[i][self._control] == 1:
                bits[i][self._target] = int(not bits[i][self._target])

CNOT = CX = CNOTGate()

# ====================================================================================================
