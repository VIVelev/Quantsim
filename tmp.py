from quantsim import QuantumMachine, H, CNOT, D

with QuantumMachine(num_qubits=3) as qm:
    qm[2] - H
    qm[2]@qm[3] - CNOT(1, 2) - D
