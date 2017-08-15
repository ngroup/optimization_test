import numpy as np

def sphere(args):
    f = sum([np.power(x, 2.) for x in args])
    return f
