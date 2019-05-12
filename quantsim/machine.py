from .qubit import Qubit

__all__ = [
    'QuantumMachine',
]


class QuantumMachine:
    
    def __init__(self, num_qubits=1, name='My-Quantum-Machine'):
        self.num_qubits = num_qubits
        self.name = name

        self.qubits = []

    def __enter__(self):
        self._init_qubits()
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        del self.qubits

    def _init_qubits(self):
        self.qubits = [Qubit() for _ in range(self.num_qubits)]

    def get_qubit(self, idx=None):
        if idx != None:
            return self.qubits[idx]
        else:
            return self.qubits[self.num_qubits-1]

    def set_qubit(self, idx, qubit):
        self.qubits[idx] = qubit
        return qubit
