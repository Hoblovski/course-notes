"""DTFT in 70 lines of code

    given f (at line 49)
          sample period / freqency / radial frequency (at line 50)
          window size (at line 51)
    this program generates the plot for X(omega) (i.e. the DTFT result)
"""
from math import *
import numpy as np
import matplotlib.pyplot as plt
EPS = 1e-9

def Sa(t):
    if abs(t) < EPS:
        return 1
    else:
        return sin(t) / t

def G(t):
    if -.5 <= t <= .5:
        return 1
    else:
        return 0

def sgn(t):
    if t < 0:
        return -1
    else:
        return 1

def u(t):
    if t >= 0:
        return 1
    else:
        return 0

def set_sample(**kwargs):
    global TS
    if "T" in kwargs:
        TS = kwargs["T"]
    elif "omega" in kwargs:
        TS = 2*pi/kwargs["omega"]
    elif "nu" in kwargs:
        TS = 1/kwargs["omega"]
    else:
        assert False


f = lambda t : Sa(t)
set_sample(omega=3)
L = 4096
SAMPLE_POINTS = 512


def DTFT(x, omega):
    rv = 0
    for n in range(-L, L):
        rv += x[n+L] * e**(-1j * omega * n)
    return rv

x = [f(n*TS) for n in range(-L, L)]

sampled_vals = []
for i in range(SAMPLE_POINTS):
    omega = 2*pi*i/SAMPLE_POINTS
    v = DTFT(x, omega)
    sampled_vals += [abs(v)]
omegas = np.array(range(SAMPLE_POINTS)) / SAMPLE_POINTS * 2 * pi

maxval = np.max(sampled_vals)
for i in range(SAMPLE_POINTS):
    if sampled_vals[i] >= maxval - EPS:
        print("Maximum value at %.4f" % (omegas[i]))

plt.plot(omegas, sampled_vals)
plt.show()
