import numpy as np

def rosenbrock(x):
    x = np.asarray(x)
    f = sum(100.0 * (x[1:] - x[:-1] ** 2.0) ** 2.0 + (x[:-1] - 1) ** 2.0)
    return f
