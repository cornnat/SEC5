#########
# TASK 2
#######################

##############
# Part C
###############################

import numpy as np
import matplotlib.pyplot as plt

# Constants
N = 100  # Total number of bosons
epsilon = 1.0  # Energy of the excited state (in arbitrary units)
k_B = 1.0  # Boltzmann constant (in arbitrary units)

# Temperature range
T = np.linspace(0.1, 10, 100)  # Avoid T=0 to prevent division by zero

# Compute the partition function and occupation numbers
n0 = N / (1 + np.exp(-epsilon / (k_B * T)))  # Ground state occupation
nE = N - n0  # Excited state occupation, since n0 + nE = N

# Plot results
plt.figure(figsize=(8, 6))
plt.plot(T, n0, label='Ground state ⟨n0⟩')
plt.plot(T, nE, label='Excited state ⟨nε⟩', linestyle='dashed')
plt.xlabel("Temperature (T)")
plt.ylabel("Average number of particles")
plt.title("Bose-Einstein Condensate Occupation Numbers")
plt.legend()
plt.grid()
plt.savefig('plots/partC_BEC_occupation.png')
plt.show()
