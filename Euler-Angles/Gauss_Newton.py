import numpy as np

from Quaternion_Calc import *
from RMSD import cols

def res(x, A, B):

    res = Q_form(x[0], x[1], x[2])

    res = res @ A  # Transform A using rotation (should be 3×N)

    res = res - B
    res = res.flatten()
    return res

def Jacobian(A, B, eulers, eps=1e-8):
    A = np.reshape(A, (3, -1))
    m = A.shape[1] * 3
    J = np.zeros((m, 3))

    for i in range(3):
        trans_angles = eulers.copy()
        trans_angles[i] += eps

        new_res = res(trans_angles, A, B)
        orig_res = res(eulers, A, B)


        J[:,i] = (new_res - orig_res) / eps

    return J

def Gauss_Newton(A, B, x0, y, p, r, tol = 1e-3, max_iter = 1000):

    x = x0

    for i in range(max_iter):
        residual = res(x, A, B)
        J = Jacobian(A, B, x)
        JTJ = J.T @ J + 1e-10*np.eye(3)

        JTr = J.T @ residual.reshape(-1, 1)
        
        delta = np.linalg.solve(JTJ, -JTr)
        delta = np.ravel(delta)
        x += 0.1 * delta
        

    
    return Q_form(x[0],x[1],x[2])

