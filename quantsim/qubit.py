from itertools import product

import numpy as np

from .gates import CNOT, R8, BaseGate, H, I, Rx, Rz, S, T, X, Z

__all__ = [
    'Qubit',
    'ProductState',
]


class Qubit:

    def __init__(self, zero=1, one=0, circuit=None, qid=None):
        self.zero = complex(zero)
        self.one  = complex(one)
        self.circuit = circuit
        self.qid = qid

        self.measured_state = None

    def __repr__(self):
        return str(self.zero) + '|0> + ' + str(self.one) + '|1>\n'
    
    def __eq__(self, other):
        return self.zero == other.zero and self.one == other.one

    def __sub__(self, gate):
        assert isinstance(gate, BaseGate)

        gate.apply(self)
        return self

    def __matmul__(self, other_qubit):
        assert isinstance(other_qubit, Qubit)
        return ProductState(self, other_qubit)

    def identity(self):
        I.apply(self)
        return self

    def X(self):
        X.apply(self)
        return self

    def H(self):
        H.apply(self)
        return self
    
    def Z(self):
        Z.apply(self)
        return self

    def S(self):
        S.apply(self)
        return self

    def T(self):
        T.apply(self)
        return self
    
    def R8(self):
        R8.apply(self)
        return self
    
    def Rx(self, theta):
        Rx(theta).apply(self)
        return self
    
    def Rz(self, phi):
        Rz(phi).apply(self)
        return self

    def measure(self):
        """ Measure the qubit in the computational basis """

        if np.random.rand() < abs(self.zero) ** 2:
            self.zero = complex(1)
            self.one  = complex(0)
            self.measured_state = 0

        else:
            self.zero = complex(0)
            self.one  = complex(1)
            self.measured_state = 1

        return self
    
    def display(self):
        print(self.__repr__())
        return self

# ====================================================================================================

class ProductState:

    def __init__(self, *qubits):
        self.qubits = qubits

        self._bits = None
        self._coefs = None
        self._calc_states()

    def _calc_states(self):
        self._bits = list(map(list, product([0, 1], repeat=len(self.qubits))))
        self._coefs = []

        for config in self._bits:
            coef = 1

            for i, bit in enumerate(config):
                if bit == 0:
                    coef *= self.qubits[i].zero
                else:
                    coef *= self.qubits[i].one
            
            self._coefs.append(coef)

    def __matmul__(self, other):
        assert isinstance(other, Qubit) or isinstance(other, ProductState)

        if isinstance(other, Qubit):
            self.qubits.append(other)
        else:
            self.qubits += other.qubits

        self._calc_states()

    def __repr__(self):
        string = ''

        for config, coef in zip(self._bits, self._coefs):
            if coef**2 != 0:
                string += str(coef) + '|' + ''.join(map(str, config)) + '> +'

        return string[:-2] + '\n'

    def __sub__(self, gate):
        assert isinstance(gate, BaseGate)

        gate.apply(self)
        return self

    def display(self):
        print(self.__repr__())
        return self

# ====================================================================================================
