from quantsim import QuantumCircuit, H, CNOT, D

with QuantumCircuit(num_qubits=3) as qc:
    qc[2] - H
    qc[2]@qc[3] - CNOT - D
