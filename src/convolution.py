###DT CONVOLUTION

import numpy as np

def conv_dt_manual(x, h):
    """
    If x has length N and h has length M,
    output y will have length N + M - 1
    operation: y[n] = sum_k x[k] * h[n-k] (convolution)
    """

    N = len(x)
    M = len(h)

    y_length = N + M - 1

    y = np.zeros(y_length)

    for n in range(y_length):
        total = 0
        for k in range(N):
            if 0 <= n - k < M:
                total += x[k] * h[n - k]
        y[n] = total

    return y

def conv_dt_numpy(x, h):
    """
    Use numpy's built-in convolution function to perform DT convolution.
    """
    return np.convolve(x, h)


def conv_output_index_dt(n_x, n_h):
    """
    Finds the correct output index array for y[n] = x[n] * h[n].

    Important:
    In DT signals, arrays have INDEX POSITIONS.
    Example:
        n_x = [-2, -1, 0, 1]
    means x exists from n=-2 to n=1

    After convolution, output indices ALWAYS range from:
        start = (start index of x) + (start index of h)
        end   = (end index of x)   + (end index of h)
    """

    n_start = n_x[0] + n_h[0]
    n_end = n_x[-1] + n_h[-1]

    n_y = np.arange(n_start, n_end + 1)

    return n_y




### CT CONVOLUTION
def conv_ct_manual(t, x, h):
    """
    Numerical approximation of continuous-time convolution.

    CT convolution:
        y(t) = ∫ x(τ) h(t - τ) dτ

    In code, we approximate integral using sum:
        y(t) ≈ sum( x * h_shifted ) * dt

    Assumptions:
    - t is uniformly spaced (constant dt)
    - x and h are sampled on the same time grid
    """
    dt = t[1] - t[0]

    y = np.convolve(x, h) * dt

    t_start = t[0] + t[0]
    t_end = t[-1] + t[-1]

    t_y = np.linspace(t_start, t_end, len(y))
    return t_y, y


