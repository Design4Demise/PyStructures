import numpy as np


def shearforce(y: np.ndarray, average_l_dist: np.ndarray) -> np.ndarray:
    vf = np.zeros_like(y)
    for i in range(y.shape[0]):
        vf[i] = np.sum(average_l_dist) - np.sum(average_l_dist[0:i])
    return vf


def shearstress(y: np.ndarray,
                average_l_dist: np.ndarray,
                wing_thickness: float,
                wing_chord: np.ndarray,
                iy: float) -> np.ndarray:

    shearf = shearforce(y, average_l_dist)
    discrete_z = np.linspace(0, 1, 11) * wing_thickness / 2

    shear_stress_dist = np.empty((discrete_z.shape[0], shearf.shape[0]))

    for idx_f, force in enumerate(shearf):
        for idx_z, z in enumerate(discrete_z):
            shear_stress_dist[idx_z, idx_f] = (force / (wing_chord[idx_f] * iy))\
                                              * (wing_thickness / 2 - z)\
                                              * (((wing_thickness / 2) ** 2) / 2 - (z ** 2) / 2)

    return shear_stress_dist


def bendingmoment(y: np.ndarray, average_l_dist: np.ndarray) -> np.ndarray:
    bending_moment = np.zeros_like(y)
    for i in y:
        bending_moment[i] = np.dot(y[i], average_l_dist) - np.dot(y[0:i], average_l_dist[0:i])
    return bending_moment


def bendingstress(y: np.ndarray,
                  average_l_dist: np.ndarray,
                  wing_thickness,
                  moment_of_inertia_y: float,
                  n_points: int = 11) -> np.ndarray:

    bendingm = bendingmoment(y, average_l_dist)
    discrete_z = np.linspace(0, 1, n_points) * wing_thickness / 2

    bending_stress_dist = np.empty((discrete_z.shape[0], bendingm.shape[0]))

    for idx_m, moment in enumerate(bendingm):
        for idx_z, z in enumerate(discrete_z):
            bending_stress_dist[idx_z, idx_m] = moment * z / moment_of_inertia_y

    return bending_stress_dist
