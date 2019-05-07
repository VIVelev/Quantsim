# Quantsim
Quantum Computing Simulation in Python 

### Simple Random Bit Generator program
```python
from quantsim import Qubit, H, M

def random_bit():
    # Init a Qubit
    q = Qubit()

    # Apply Hadamard Gate
    q - H - M
    # q.H().measure() is equivalent

    return q.measured_state
```

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

* [Python](https://www.python.org/) - The Programming Language used.
* [Pipenv](https://github.com/pypa/pipenv) - Dependency and Virtual Environment Management

***Download for Mac OSX using Homebrew***
```
brew install python
brew install pipenv
```

### Installing

A step by step series of examples that tell you how to get a development env running

1) Since we are using the **Python** programming language as a main language, you will need to download it.
You can do so from the official **Python** [website](https://www.python.org/).

2) Once you have **Python** up and running we then need to setup our development env. For that
we are using **Pipenv**. You will need to install it. Check out [these](https://pipenv.readthedocs.io/en/latest/install/#installing-pipenv) instructions to see how is done.

3) Now, that you have the prerequisites the only part left is too install all the other **Pyhton** packages
that **Quantsim** depends on. To do run the following:
    ```
    pipenv install --dev
    ```
    The `--dev` tag is used in order **Pipenv** to know to install also the packages that are used in the
    package development process.

## Built With

* [NumPy](http://www.numpy.org/) - Fundamental package for scientific computing with Python

## Contributing

Please read [CONTRIBUTING.md](https://github.com/VIVelev/PyDojoML/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

For the versions available, see the [tags on this repository](https://github.com/VIVelev/PyDojoML/tags). 

## Authors

* **Victor Velev** - *Initial work* - [VIVelev](https://github.com/VIVelev)

See also the list of [contributors](https://github.com/VIVelev/PyDojoML/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
