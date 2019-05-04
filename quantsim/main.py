from .qubit import Qubit

__all__ = [
    'QuantumMachine',
]


class QuantumMachine:
    
    def __init__(self, num_qubits=1, name='My-Quantum-Machine'):
        self.num_qubits = num_qubits
        self.name = name

        self.qubits = []
        self._init_qubits()

    def _init_qubits(self):
        self.qubits = [Qubit() for _ in range(self.num_qubits)]

    def get_qubit(self, idx):
        return self.qubits[idx]

    def set_qubit(self, idx, qubit):
        self.qubits[idx] = qubit
        return qubit
