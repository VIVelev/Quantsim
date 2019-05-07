from quantsim import Qubit, H, M

def random_bit():
    # Init a Qubit
    q = Qubit()

    # Apply Hadamard Gate
    q - H - M
    # q.H().measure() is equivalent

    return q.measured_state


if __name__ == '__main__':
    print(random_bit())
    print(random_bit())
    print(random_bit())
