import numpy as np
import math

def Q_form(yaw, pitch, roll):
    Qroll = np.matrix([
        [1, 0, 0],
        [0, math.cos(roll), math.sin(roll)],
        [0, -math.sin(roll), math.cos(roll)]
    ])
    Qyaw = np.matrix([
        [math.cos(yaw), math.sin(yaw), 0],
        [-math.sin(yaw), math.cos(yaw), 0],
        [0, 0, 1]
    ])
    Qpitch = np.matrix([
        [math.cos(pitch), 0, math.sin(pitch)],
        [0, 1, 0],
        [-math.sin(pitch), 0, math.cos(pitch)]
    ])
    Q = Qroll @ Qyaw @ Qpitch

    return Q



def matrix_transform(X1, X2):
    return X1 @ X2