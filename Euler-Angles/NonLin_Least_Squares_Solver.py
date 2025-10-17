import numpy as np
import math
import matplotlib.pyplot as plt

from RMSD import *
from Gauss_Newton import *

A = np.matrix([[0, 0, 1, 1, 0, -1, 0],
              [0, 1, 1, 0, 0, 1, 2],
              [0, 1, 2, 3, 4, 4, 4]])

yaw = math.pi / 4
roll = math.pi / 9
pitch_beta = -math.pi / 2

Init_Guess = np.array([1.0, 1.0, 1.0], dtype=np.float64)

steps = 120

sample_numbers = []
yaw_vals = []
roll_vals = []
pitch_vals = []
err_vals = []

for i in range(steps + 1):

    pitch = pitch_beta +  (i * math.pi)/steps
    Q_prime = Q_form(yaw,roll,pitch)
    B_prime = Q_prime @ A

    Q = Gauss_Newton(A, B_prime, Init_Guess, yaw, pitch, roll)
    B = Q @ A

    sample_numbers.append(i)
    yaw_vals.append(yaw)
    roll_vals.append(roll)
    pitch_vals.append(pitch)


    err = RMSD(B,Q_prime,A)

    print(err)
    err_vals.append(err)

fig, axs = plt.subplots(2, 1, figsize=(8, 10))

axs[0].plot(sample_numbers, yaw_vals, 'b+', label='Yaw (ϕ)')
axs[0].plot(sample_numbers, pitch_vals, 'go', label='Pitch (θ)')
axs[0].plot(sample_numbers, roll_vals, 'rx', label='Roll (ψ)')
axs[0].set_title("Challenge 12.2")
axs[0].set_ylabel("Angle (radians)")
axs[0].set_xlabel("Sample Number")
axs[0].legend()
axs[0].grid(True)

axs[1].semilogy(sample_numbers, err_vals, 'b+', label='Q error')
#axs[1].semilogy(sample_numbers, pos_errors_ch2, 'go', label='Position error')
axs[1].set_title("Challenge 2 Errors")
axs[1].set_ylabel("error")
axs[1].set_xlabel("sample number")
axs[1].legend()
axs[1].grid(True)

plt.tight_layout()
plt.show()