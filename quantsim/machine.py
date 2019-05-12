from .qubit import Qubit, ProductState

__all__ = [
    'QuantumMachine',
]


class QuantumMachine:
    
    def __init__(self, num_qubits=2, name='My-Quantum-Machine'):
        self.num_qubits = num_qubits
        self.name = name

        # Init Qubits
        qubits = [Qubit() for _ in range(self.num_qubits)]
        # Init The Overall Product State
        self._product_state = ProductState(*qubits)

    def __getitem__(self, idx):
        return self._product_state.qubits[idx-1]

    def __setitem__(self, idx, data):
        self._product_state.qubits[idx-1] = data
    
    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        del self._product_state
