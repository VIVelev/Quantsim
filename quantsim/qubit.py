import numpy as np
from .gates import *

__all__ = [
    'Qubit',
    'Entanglement',
]


class Qubit:
    def __init__(self, a=1, b=0):
        self.zero = complex(a)
        self.one  = complex(b)

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
        return Entanglement(self, other_qubit)

    def identity(self):
        IGate.apply(self)
        return self

    def X(self):
        XGate.apply(self)
        return self

    def hadamard(self):
        HGate.apply(self)
        return self
    
    def Z(self):
        ZGate.apply(self)
        return self

    def S(self):
        SGate.apply(self)
        return self

    def T(self):
        TGate.apply(self)
        return self
    
    def R8(self):
        R8Gate.apply(self)
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

        else:
            self.zero = complex(0)
            self.one  = complex(1)

        return self
    
    def display(self):
        print(self.__repr__())
        return self

class Entanglement:
    def __init__(self, q1, q2, control_qubit=0):
        self.q1 = q1
        self.q2 = q2
        self.control_qubit = control_qubit

    def __repr__(self):
        prob = [
            [self.q1.zero * self.q2.zero, self.q1.zero * self.q2.one],
            [self.q1.one * self.q2.zero, self.q1.one * self.q2.one]
        ]

        return str(prob[0][0]) + '|00> + ' + str(prob[0][1]) + '|01> + ' + str(prob[1][0]) + '|10> + ' + str(prob[1][1]) + '|11>\n'

    def __sub__(self, gate):
        assert isinstance(gate, BaseGate) 

        gate.apply(
            self.q1 if self.control_qubit else self.q2,
            self.q1 if self.control_qubit else self.q2,
        )
        return self

    def display(self):
        print(self.__repr__())
        return self
