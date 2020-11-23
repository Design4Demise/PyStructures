# Wing structural analysis part 1: pressure distributions
## Admin ##
import numpy as np
import matplotlib.pyplot as plt

## Input Variables ##
b = 1
CRoot = 0.25
CTip = 0.25
Lambda = CTip/CRoot
S = 0.607882
Cl_alpha = 0.215641
q = 179

## Calculations
y = np.linspace(0, 0.5, 21)
TrapCDist = CRoot*(1-(2*y/b)*(1-Lambda))            # Trapezoidal Chord Distribution
EllipCDist = (4*S)/(np.pi*b)*(1-(2*y/b)**2)**0.5    # Elliptical Chord Distribution
TrapLDist = q*Cl_alpha*TrapCDist                    # Trapezoidal Lift Distribution
EllipLDist = q*Cl_alpha*EllipCDist                  # Elliptical Lift Distribution
AverageCDist = (TrapCDist+EllipCDist)/2             # Average Chord Distribution
AverageLDist = q*Cl_alpha*AverageCDist              # Average Lift Distribution

## Plotting
fig, axs = plt.subplots(2, 1, figsize=(12, 5), sharex=True)

axs[1].set_xlabel("Wing Span")
axs[0].set_ylabel("Chord Distribution")
axs[1].set_ylabel("Lift Distribution (N)")

axs[0].plot(y, TrapCDist,"-", label = "Trapezoidal Chord Distribution")
axs[0].plot(y, EllipCDist,"-", label = "Elliptical Chord Distribution")
axs[0].plot(y, AverageCDist,"-", label = "Average Chord Distribution")
axs[0].set_ylim([0,1])
axs[0].set_xlim([0,0.5])

axs[1].plot(y, TrapLDist,"--", label = "Trapezoidal Lift Distribution")
axs[1].plot(y, EllipLDist,"--", label = "Elliptical Lift Distribution")
axs[1].plot(y, AverageLDist,"--", label = "Schrenks Lift Distribution")
#axs[1].set_ylim([0,1])
axs[1].set_xlim([0,0.5])

for ax in axs:
    ax.grid()

fig.legend(loc = 1)
plt.show()

