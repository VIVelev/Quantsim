import numpy as np

from .gates import CNOT, R8, BaseGate, H, I, Rx, Rz, S, T, X, Z

__all__ = [
    'Qubit',
    'Entanglement',
]


class Qubit:
    def __init__(self, a=1, b=0):
        self.zero = complex(a)
        self.one  = complex(b)
        self.measured_state = None

    def __repr__(self):
        return str(self.zero) + '|0> + ' + str(self.one) + '|1>\n'
    
    def __eq__(self, other):
        return self.zero == other.zero and self.one == other.one

    def __sub__(self, gate):
        assert isinstance(gate, BaseGate)

        gate(self)
        return self

    def __matmul__(self, other_qubit):
        assert isinstance(other_qubit, Qubit)
        return Entanglement(self, other_qubit)

    def identity(self):
        I.apply(self)
        return self

    def X(self):
        X.apply(self)
        return self

    def hadamard(self):
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
        """Measure the qubit in the computational basis"""

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

class Entanglement:
    def __init__(self, q1, q2, control_qubit=0):
        self.q1 = q1
        self.q2 = q2
        self.control_qubit = control_qubit
        
        self._bits = [
            ['00', '01'],
            ['10', '11']
        ]
        self._qubits_coef = [
            [self.q1.zero * self.q2.zero, self.q1.zero * self.q2.one],
            [self.q1.one * self.q2.zero, self.q1.one * self.q2.one]
        ]

    def __repr__(self):
        string = ''

        for i in range(2):
            for j in range(2):
                if self._qubits_coef[i][j] > 0:
                    string += str(self._qubits_coef[i][j]) + '|' + self._bits[i][j] + '> +'

        return string[:-2] + '\n'

    def __sub__(self, gate):
        assert isinstance(gate, BaseGate) 

        if gate is CNOT:
            if self.control_qubit == 0:
                self._bits = [
                    ['00', '01'],
                    ['11', '10']
                ]
            else:
                self._bits = [
                    ['00', '11'],
                    ['10', '01']
                ]
        
        else:
            gate.apply(self)

        return self

    def display(self):
        print(self.__repr__())
        return self
