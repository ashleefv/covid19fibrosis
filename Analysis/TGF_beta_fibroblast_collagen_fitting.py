import numpy as np
from scipy.optimize import curve_fit
from scipy.integrate import odeint
import matplotlib
import math
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# given data we want to fit
TGF = [0, 0, 0.07, 0.97, 10]
FgTb_exp = [5.01, 8.03, 8.55, 13.04, 22.928]

calculated_data = []

tspan1 = np.arange(0.0, 15, 0.001)
print(tspan1)
for i in tspan1:
        tb = i
        FgTb = 0.0492*math.pow(tb,3) - 0.9868*math.pow(tb,2) + 6.5408*tb + 7.1092
        calculated_data.append(FgTb)

plt.rcParams.update({'font.size': 25})
plt.plot(TGF, FgTb_exp, 'ro', label='data', markersize=12)
plt.plot(tspan1,calculated_data, 'b-', label='fit', linewidth=3)
plt.axvline(x = 10, color = 'black', label = 'threshold', linewidth=3)
plt.hlines(22.928, 10, 15, color='green', linewidth=3)
plt.legend(loc='best')
plt.xlabel('TGF-β $(ng/mL)$')
plt.ylabel('$F_g(T_β)$')
plt.ylim(-2,50)
plt.savefig("COVID_fitting.png", dpi=300, bbox_inches='tight')
plt.show()
