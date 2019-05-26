from sympy.physics.quantum.qasm import Qasm

from ..qubit import ProductState, Qubit

__all__ = [
    'QuantumCircuit',
]


class QuantumCircuit:
    
    def __init__(self, num_qubits=2, name='My-Quantum-Circuit'):
        self.num_qubits = num_qubits
        self.name = name

        self.qasm = []
        qubits = []

        for i in range(num_qubits):
            self.qasm.append(f'qubit q_{i}')
            qubits.append(Qubit(circuit=self, qid=i))

        # Define custom gates
        self.qasm.append("def R8,0,'R8'")
        self.qasm.append("def Rx,0,'Rx'")
        self.qasm.append("def Rz,0,'Rz'")
        self.qasm.append("def M,0,'M'")
        self.qasm.append("def D,0,'D'")

        # Init the overall product state
        self._product_state = ProductState(*qubits)

    def __getitem__(self, idx):
        return self._product_state.qubits[idx]

    def __setitem__(self, idx, data):
        self._product_state.qubits[idx] = data
    
    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        del self._product_state

    def display(self):
        print(self.qasm)
        Qasm(*self.qasm).plot()
