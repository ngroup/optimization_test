import numpy as np

def rastrigin(args):
    f = 10 * len(args) + sum([np.power(x, 2.) - 10 * np.cos(2 * np.pi * x) for x in args])
    return f
