import numpy as np


def shearforce(y: np.ndarray, average_l_dist: np.ndarray) -> np.ndarray:
    vf = np.zeros_like(y)
    for i in range(y.shape[0]):
        vf[i] = np.sum(average_l_dist) - np.sum(average_l_dist[0:i])
    return vf


def bendingmoment(y: np.ndarray, average_l_dist: np.ndarray) -> np.ndarray:
    bending_moment = np.zeros_like(y)
    for i in y:
        bending_moment[i] = np.dot(y[i], average_l_dist) - np.dot(y[0:i], average_l_dist[0:i])
    return bending_moment


def shearstress(y: np.ndarray,
                average_l_dist: np.ndarray,
                wing_span: float,
                wing_thickness: float,
                iy: float) -> np.ndarray:

    shearf = shearforce(y, average_l_dist)
    discrete_z = np.linspace(0, 1, 11) * wing_thickness / 2

    shear_stress_dist = np.empty((discrete_z.shape[0], shearf.shape[0]))

    for idx_f, force in enumerate(shearf):
        for idx_z, z in enumerate(discrete_z):
            shear_stress_dist[idx_z, idx_f] = (force / (wing_span * iy))\
                                              * (wing_thickness / 2 - z)\
                                              * (((wing_thickness / 2) ** 2) / 2 - (z ** 2) / 2)

    return shear_stress_dist
