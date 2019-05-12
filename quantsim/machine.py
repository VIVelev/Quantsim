from .qubit import Qubit

__all__ = [
    'QuantumMachine',
]


class QuantumMachine:
    
    def __init__(self, num_qubits=1, name='My-Quantum-Machine'):
        self.num_qubits = num_qubits
        self.name = name

        self._qubits = []

    def __getitem__(self, idx):
        return self._qubits[idx-1]

    def __setitem__(self, idx, data):
        self._qubits[idx-1] = data
    
    def __enter__(self):
        self._init_qubits()
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        del self._qubits

    def _init_qubits(self):
        self._qubits = [Qubit() for _ in range(self.num_qubits)]
