import numpy as np


def shearforce(y, AverageLDist):

    vf = np.zeros_like(y)
    for i in range(y.shape[0]):
        vf[i] = np.sum(AverageLDist)-np.sum(AverageLDist[0:i])
    return vf


def bendingmoment(y, AverageLDist):

    bending_moment = np.zeros_like(y)
    for i in y:
        bending_moment[i] = np.dot(y,AverageLDist)-np.dot(y[0:i], AverageLDist[0:i])
    return bending_moment

def shearstress(y, AverageLDist, b, h, iy):

    shearf = shearforce(y, AverageLDist)
    discrete_z = np.linspace(0,1,11) * h / 2

    shear_stress_dist = np.empty((discrete_z.shape[0], shearf.shape[0]))

    for idx_f, force in enumerate(shearf):
        for idx_z, z in enumerate(discrete_z):
            shear_stress_dist[idx_z, idx_f] = (force / (b * iy)) * (h / 2 - z) * (((h / 2) ** 2) / 2 - (z ** 2) / 2)

    return shear_stress_dist













