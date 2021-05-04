import numpy as np
import matplotlib.pyplot as plt

# ODE solver for generic 2D Hamiltonian
def solve(t, x0, y0, px0, py0, dVdx, dVdy):
    """
    Solve for the trajectory of a 2D Hamiltonian using Omelyan SST symplectic integration algorithm.
    
    Inputs:
        - t: time over which to solve the system (numpy array)
        - x0, y0, px0, py0: initial conditions for position and momentum (floats)
        - dVdx, dVdy: partial derivatives of the potential in question (callable functions of x,y)

    Returns:
        - x, y, px, py: trajectory over the specified time (numpy arrays, same length as t)
    
    """
    dt = t[1] - t[0]
    # Initialize solution
    x, y, px, py = np.zeros_like(t), np.zeros_like(t), np.zeros_like(t), np.zeros_like(t)
    x[0], y[0], px[0], py[0] = x0, y0, px0, py0
    
    for i in range(len(t) - 1):
        # V dt/6
        px_temp = px[i] - dt/6 * dVdx(x[i], y[i])
        py_temp = py[i] - dt/6 * dVdy(x[i], y[i])
        # T dt/2
        x_temp = x[i] + dt/2 * px_temp
        y_temp = y[i] + dt/2 * py_temp
        # V 2dt/3
        px_temp = px_temp - 2*dt/3 * dVdx(x_temp, y_temp)
        py_temp = py_temp - 2*dt/3 * dVdy(x_temp, y_temp)
        # T dt/2
        x[i+1] = x_temp + dt/2 * px_temp
        y[i+1] = y_temp + dt/2 * py_temp
        # V dt/6
        px[i+1] = px_temp - dt/6 * dVdx(x[i+1], y[i+1])
        py[i+1] = py_temp - dt/6 * dVdy(x[i+1], y[i+1])
    
    return x, y, px, py


# Define dVdx, dVdy to be used for the above solver, as well as the total energy E for the Henon-Heiles potential
def dVHH_dx(x,y):
    return 2*x*y + x
def dVHH_dy(x,y):
    return x**2 - y**2 + y

def E_HH(x, y, px, py):
    return 1/2 * (px**2 + py**2 + x**2 + y**2) + x**2*y - 1/3*y**3