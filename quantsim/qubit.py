import numpy as np

__all__ = [
    'Qubit',
]


class Qubit:
    def __init__(self, a, b):
        self.zero = complex(a)
        self.one  = complex(b)

    def measure(self):
        """Measure the qubit in the computational basis"""

        if np.random.rand() < abs(self.zero) ** 2:
            self.zero = complex(1)
            self.one  = complex(0)
            return 0

        else:
            self.zero = complex(0)
            self.one  = complex(1)
            return 1

    def __repr__(self):
        return str(self.zero) + '|0> + ' + str(self.one) + '|1>\n'
    
    def __eq__(self, other):
        return self.zero == other.zero and self.one == other.one
