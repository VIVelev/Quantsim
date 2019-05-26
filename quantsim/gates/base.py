from abc import ABC, abstractmethod, abstractproperty
from copy import deepcopy

import numpy as np

__all__ = [
    'BaseGate',
    'MatrixGate',
    'RotationGate',
    'SelfInverseGate',
]


class BaseGate(ABC):
    """Base class of all gates. (Don't use it directly but derive from it)

    Parameters:
    -----------
    name : string

    """

    def __init__(self, name):
        self._name = name

    def __repr__(self):
        return self._name

    def apply(self, *qubits):
        conf = f'{self} '
        for q in qubits:
            conf += f'q_{q.qid},'

        qubits[0].circuit.qasm.append(conf[:-1])

    @abstractmethod
    def get_inverse(self):
        pass

    def inverse(self, qubit):
        self.get_inverse().apply(qubit)

# ====================================================================================================

class MatrixGate(BaseGate):
    """Matrix Qubit Gate

    Defines a gate class whose instances are defined by a matrix.

    Parameters:
    -----------
    matrix : 2d array
    name : string

    """
    
    def __init__(self, matrix, name):
        super().__init__(name)
        self._matrix = matrix

    @property
    def matrix(self):
        return self._matrix

    @matrix.setter
    def matrix(self, matrix):
        self._matrix = np.array(matrix)
    
    def apply(self, qubit):
        super().apply(qubit)

        qubit_vec = np.array([[qubit.zero], [qubit.one]])
        res_qubit_vec = self.matrix @ qubit_vec
        res_qubit_vec = np.transpose(res_qubit_vec)

        qubit.zero = res_qubit_vec[0][0]
        qubit.one = res_qubit_vec[0][1]

    def get_inverse(self):
        return MatrixGate(np.linalg.inv(self.matrix), 'Inverse'+self._name)

# ====================================================================================================

class RotationGate(MatrixGate):
    """Defines a base class of a rotation gate.

    A rotation gate has a continuous parameter (the angle), labeled 'angle' /
    self.angle.

    Parameters:
    -----------
    matrix : 2d array
    name : string
    angle : float, angle

    """

    def __init__(self, name):
        super().__init__(np.identity(2), name)
        self._angle = 0

    def __call__(self, angle):
        self._angle = angle
        return self

    def __repr__(self):
        return self._name + '(theta)'

    @abstractproperty
    def matrix(self):
        pass

# ====================================================================================================

class SelfInverseGate(BaseGate):
    """Self-inverse base gate class

    Automatic implementation of the get_inverse-member function for self-
    inverse gates.

    Parameters:
    -----------
    name : string

    """

    def get_inverse(self):
        return deepcopy(self)

# ====================================================================================================
