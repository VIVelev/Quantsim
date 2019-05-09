from quantsim import Qubit, H, CNOT, D

if __name__ == '__main__':
    q1, q2 = Qubit(), Qubit()
    q1 - H
    q1@q2 - CNOT - D
