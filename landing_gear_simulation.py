#!/usr/bin/env python
# coding: utf-8

# In[1]:


# ============================================
# A320 Landing Gear Simulation (Clean Version)
# Stable for Good Plots in Jupyter
# ============================================

get_ipython().run_line_magic('matplotlib', 'inline')

import numpy as np
import matplotlib.pyplot as plt

# ============================================
# PARAMETERS (Tuned for Stability & Clean Plots)
# ============================================

m = 15000            # kg (per gear)
g = 9.81

# Oleo system (moderate values for stability)
V0 = 0.05            # m^3
P0 = 4e5              # Pa (reduced for smooth response)
gamma = 1.3
A_piston = 0.01

# Damping
c = 100000           # linear damping

# Tire stiffness (moderate)
k_tire = 200000

# Simulation
t0 = 0
tf = 3
dt = 0.001

landing_velocity = 2.5   # realistic value

# ============================================
# MODEL (ODE SYSTEM)
# ============================================

def system(t, y):
    z, v = y

    # Gas force
    V = max(V0 - z, 1e-5)
    P = P0 * (V0 / V)**gamma
    F_gas = P * A_piston

    # Damping
    F_damp = c * v

    # Tire
    F_tire = k_tire * z

    # Net force
    F = m * g - F_gas - F_damp - F_tire

    a = F / m

    return np.array([v, a])

# ============================================
# RK4 SOLVER
# ============================================

def rk4(f, t0, tf, y0, h):

    t = np.arange(t0, tf, h)
    Y = np.zeros((len(t), len(y0)))
    Y[0] = y0

    for i in range(1, len(t)):

        k1 = f(t[i-1], Y[i-1])
        k2 = f(t[i-1] + h/2, Y[i-1] + (h/2)*k1)
        k3 = f(t[i-1] + h/2, Y[i-1] + (h/2)*k2)
        k4 = f(t[i-1] + h,   Y[i-1] + h*k3)

        Y[i] = Y[i-1] + (h/6)*(k1 + 2*k2 + 2*k3 + k4)

    return t, Y

# ============================================
# RUN SIMULATION
# ============================================

y0 = np.array([0.0, landing_velocity])

t, Y = rk4(system, t0, tf, y0, dt)

z = Y[:,0]
v = Y[:,1]

# Acceleration & G-load
a = np.array([system(t[i], Y[i])[1] for i in range(len(t))])
g_load = a / g

# ============================================
# RESULTS
# ============================================

print("Max Compression:", np.max(z))
print("Max G-Load:", np.max(g_load))

# ============================================
# PLOTS
# ============================================

plt.figure(figsize=(15,5))

plt.subplot(1,3,1)
plt.plot(t, z)
plt.title("Compression")
plt.xlabel("Time (s)")
plt.ylabel("z (m)")
plt.grid()

plt.subplot(1,3,2)
plt.plot(t, v)
plt.title("Velocity")
plt.xlabel("Time (s)")
plt.ylabel("v (m/s)")
plt.grid()

plt.subplot(1,3,3)
plt.plot(t, g_load)
plt.title("G-Load")
plt.xlabel("Time (s)")
plt.ylabel("g")
plt.grid()

plt.tight_layout()
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




