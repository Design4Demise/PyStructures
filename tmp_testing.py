from pystructures.wing_dist import CalcAverageLDist
from pystructures.ShearBending import shearstress
import numpy as np

y = np.linspace(0, 0.5, 21)
b = 1

averageliftdist = CalcAverageLDist(179, 0.22, 1, 0.25, 0.25, 0.6)

output = shearstress(y, averageliftdist, 0.25, 0.25, 0.000326)

print(output)


