#this file is the signal generator, it has functions to generate standard signals

import numpy as np


#================================
#continuos time signals (ct)
#================================

## CT unit step function u(t) (ON/OFF signal)
def unit_step_ct(t):

    """Generates a continuous time unit step signal u(t).
    u(t) = 0 for t < 0
    u(t) = 1 for t >= 0
    """
#convert TRUE/FALSE to 1/0
    u = (t >= 0).astype(float)
    return u


##ramp signal r(t)
def ramp_ct(t):
    """CT ramp r(t)
    definition : r(t) = t * u(t)
    if t < 0, r(t) = 0
    if t >= 0, r(t) = t
    """
    r = t * unit_step_ct(t)
    return r


##Continuos time sine wave signal(crucial building block for many signals)
def sin_ct(t, f=1.0, A=1.0, phase=0.0):
    """
    x(t) = A * sin(2πft + phase)
    f - frequency in Hz
    A - amplitude
    phase - in radians
    """
    x = A * np.sin(2*np.pi*f*t + phase)
    return x


##continuos time exponential decay signal
def exp_decay_ct(t, a=1.0):
    """
    x(t) = e^(-at) * u(t)
    w/o u(t), x(t) would be exp growing for t < 0
    a - decay rate
    """
    x = np.exp(-a*t) * unit_step_ct(t)
    return x


##continuos time impulse funtion delta(t)/h(t)
def impulse_like_ct(t, width=0.02):
    """
    cant be exact impulse function cause that needs infinite height 
    at t = 0and thats not possible in numerical computing
    so we approximate it with a narrow rectangular pulse

    pulse width = width
    pulse height = 1/width

    ensured total area is approx 1
    """
    x = np.zeros_like(t)
    region = np.abs(t) <= (width/2) 
    x[region] = 1.0 / width
    return x




#================================
#discrete time signals (dt)
#================================

## DT unit step function u[n]
def unit_step_dt(n):
    """
    discrete time unit step signal u[n]
    definition:
    u[n] = 0 for n < 0
    u[n] = 1 for n >= 0
    """
    u = (n >= 0).astype(float)
    return u


## DT ramp signal r[n]
def ramp_dt(n):
    """
    discrete time ramp signal r[n]
    definition:
    r[n] = n * u[n]
    if n < 0, r[n] = 0
    if n >= 0, r[n] = n
    """
    r = n * unit_step_dt(n)
    return r


## DT sine wave signal x[n]
def sin_dt(n, f=0.1, A=1.0, phase=0.0):
    """
    x[n] = A * sin(2πfn + phase)
    f - frequency in cycles/sample
    A - amplitude
    phase - in radians
    """
    x = A * np.sin(2*np.pi*f*n + phase)
    return x


## Discrete time exponential decay signal
def exp_decay_dt(n, a=0.9):
    """
    definition:
    x[n] = a^n * u[n]
    a - decay rate (0 < a < 1 for decay)
    """
    x = (a**n) * unit_step_dt(n)
    return x


## Discrete time impulse function delta[n]
def impulse_dt(n):
    """
    definition:
    delta[n] = 1 for n = 0
    delta[n] = 0 otherwise
    """
    d = (n==0).astype(float)
    return d
