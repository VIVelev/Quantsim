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

    @abstractmethod
    def apply(self, *qubits):
        pass

    def __call__(self, *qubits):
        self.apply(*qubits)
        return self

    @abstractmethod
    def get_inverse(self):
        pass

    def inverse(self, *qubits):
        self.get_inverse().apply(qubits)

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
    
    def apply(self, *qubits):
        qubits_matrix = [
            [q.zero, q.one] for q in qubits
        ]
        qubits_matrix = np.transpose(qubits_matrix)

        res_qubits_matrix = self.matrix @ qubits_matrix
        res_qubits_matrix = np.transpose(res_qubits_matrix)

        for i in range(len(qubits)):
            qubits[i].zero = res_qubits_matrix[i][0]
            qubits[i].one = res_qubits_matrix[i][1]

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
