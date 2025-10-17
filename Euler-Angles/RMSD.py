import numpy as np
import math
import matplotlib.pyplot as plt

def cols(A):
    return np.hsplit(A, A.shape[1])

def RMSD(B, Q, A):
    a_col = cols(A)
    b_col = cols(B)
    err_sum = 0

    for i in range(len(a_col)):
        Q_trans = Q @ a_col[i]
        diff = b_col[i] - Q_trans
        norm = 0
        for elem in diff:
            norm += elem**2

        norm = (math.sqrt(norm))**2
        err_sum += norm

    err_sum = err_sum/7

    return err_sum
#def Frobenius(B, Q, A):
