###SIGNAL OPERATIONS MODULE

#helps apply basic, standard operations on signals like shifting, scaling, time reversal
#and addition/multiplication

import numpy as np


#AMPLITUDE OPERATIONS
def amplitude_scale(x, scale):
    """
    scale a signal amplitude
    operation: y[n] = scale * x[n] or y(t) = scale * x(t)
    """
    y = scale * x
    return y


# -----------------------------
# CONTINUOUS-TIME (CT) OPERATIONS
# -----------------------------
def time_shift_ct(t,x,shift):
    """
    if shift > 0, shifts signal to right
    if shift < 0, shifts signal to left
    operation: y(t) = x(t - shift)
    """
    t_shifted = t + shift
    y = x.copy()
    return t_shifted, y

def time_reverse_ct(t,x):
    """
    reverses signal in time
    operation: y(t) = x(-t)
    """
    t_reversed = -t
    y = x.copy()
    return t_reversed, y


# -----------------------------
# DISCRETE-TIME (DT) OPERATIONS
# -----------------------------
def shift_dt(n,x,shift):
    """
    if shift > 0, shifts signal to right
    if shift < 0, shifts signal to left
    operation: y[n] = x[n - shift]
    """
    n_shifted = n + shift
    y = x.copy()
    return n_shifted, y

def reverse_dt(n,x):
    """
    reverses signal in time
    operation: y[n] = x[-n]
    """
    n_reversed = -n
    y = x.copy()
    return n_reversed, y


# -----------------------------
# SIGNAL COMBINATION OPERATIONS
# -----------------------------
def add_signals(x1, x2):
    """
    adds two signals of same length
    operation: y = x1 + x2
    """
    if len(x1) != len(x2):
        raise ValueError("Signals must be of the same length to add.")
    y = x1 + x2
    return y

def multiply_signals(x1, x2):
    """
    multiplies two signals of same length
    operation: y = x1 * x2
    """
    if len(x1) != len(x2):
        raise ValueError("Signals must be of the same length to multiply.")
    y = x1 * x2
    return y