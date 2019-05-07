from quantsim import Qubit, H, CNOT

if __name__ == '__main__':
    q1, q2 = Qubit(), Qubit()
    q1 - H
    ent = q1@q2
    ent - CNOT

    ent.display()
