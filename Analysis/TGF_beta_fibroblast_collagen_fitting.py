import numpy as np
from scipy.optimize import curve_fit
from scipy.integrate import odeint
import matplotlib
import math
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# given data we want to fit
#tspan = [1, 1.33, 1.48, 1.63, 1.81, 2, 2.2, 2.58, 2.77, 3]
#Ca_data = [1.46, 6.5, 9.8, 13.57, 16.6, 21.50, 22.93, 24.54, 26.34, 27.45]

#tspan = [0, 0.07, 0.23, 0.78, 2.48, 10]
#Ca_data = [2.99, 7.34, 13, 17.57, 19.83, 24.07]
#Ca_data = [2.99/24.07, 7.34/24.07, 13/24.07, 17.57/24.07, 19.83/24.07, 24.07/24.07]

tspan = [0, 0, 0.07, 0.97, 10]
#tspan = [0*1e-12, 0.07*1e-12, 0.97*1e-12, 10*1e-12]
Ca_data = [5.01, 8.03, 8.55, 13.04, 22.928]

# (M(T_beta))
#tspan = [0.05, 0.1, 0.5, 1, 10]
#Ca_data = [30.2, 60.5, 123.3, 90.3, 80.5]

#tspan = [0.04, 0.07, 0.48, 0.96, 10]
#Ca_data = [30.2, 60.5, 123.3, 90.3, 80.5]

calculated_data = []

tspan1 = np.arange(0.0, 15, 0.001)
print(tspan1)
for i in tspan1:
        tb = i
        FgTb = 0.0492*math.pow(tb,3) - 0.9868*math.pow(tb,2) + 6.5408*tb + 7.1092
        #FgTb = 0.3350 * math.pow(tb, 3) - 6.3095 * math.pow(tb, 2) + 32.2810 * tb + 57.3019
        calculated_data.append(FgTb)

print(calculated_data[-1])
#plt.scatter(tspan, Ca_data)
#plt.plot(tspan1,calculated_data)
#plt.show()

plt.rcParams.update({'font.size': 25})
plt.plot(tspan, Ca_data, 'ro', label='data', markersize=12)
plt.plot(tspan1,calculated_data, 'b-', label='fit', linewidth=3)
plt.axvline(x = 10, color = 'black', label = 'threshold', linewidth=3)
plt.hlines(22.928, 10, 15, color='green', linewidth=3)
plt.legend(loc='best')
plt.xlabel('TGF-β $(ng/mL)$')
#plt.ylabel('$F_c(T_β)$')
plt.ylabel('$F_g(T_β)$')
#plt.ylabel('$M(T_β)$')
#plt.xscale('log')
plt.ylim(-2,50)
plt.savefig("COVID_fitting.png", dpi=300, bbox_inches='tight')
plt.show()

#tspan = [1, 2, 3]
#Ca_data = [1.46, 26.35, 46.40]
'''
def fitfunc(x, a, b):
        return (a*x)/(b+x)
'''

def fitfunc(x, a, b, c,d):
        return (a*x*x*x + b*x*x + c*x + d)

#init_guess = [0,1]
init_guess = [0,0,0,0]
#bounds = ((0,0,0),(np.inf,np.inf,np.inf))
k_fit, kcov = curve_fit(fitfunc, tspan, Ca_data, p0=init_guess)
print (k_fit, kcov)

tfit = np.linspace(0,10)
#fit = fitfunc(tfit, k_fit[0], k_fit[1])
fit = fitfunc(tfit, k_fit[0], k_fit[1], k_fit[2], k_fit[3])

'''
data = [1e-3, 1e-2, 1e-1, 1, 1e1, 1e2]

data1 = np.array([-3.261438, -2.782135, -2.3137255, -1.8235294, -1.3551198, -0.8649238, -0.38562092, 0.08278867, 0.5620915, 1.0305011, 1.5206971, 2])
data1 = [math.pow(10,x) for x in data1]
data2 = np.array([19.753086, 16.358025, 17.28395, 46.60494, 58.024693, 75.0, 105.55556, 95.679016, 103.703705, 102.77778, 101.234566, 100.30864])
data2 = data2/105.55556


collagen = [0.0 for i in range(len(data))]

for i in range(len(data)):
        collagen[i] = (22.67*data[i])/(0.174+data[i])*0.014

collagen = np.array(collagen)

plt.rcParams.update({'font.size': 25})
plt.plot(data, collagen/collagen[-1], linewidth=3)
plt.plot(data1, data2, 'ro', label='data', markersize=12)
plt.xlabel('TGF-beta')
plt.ylabel('Collagen')
plt.xscale('log')
#plt.ylim(0,30)
plt.show()

'''
plt.rcParams.update({'font.size': 25})
plt.plot(tspan, Ca_data, 'ro', label='data', markersize=12)
plt.plot(tfit, fit, 'b-', label='fit', linewidth=3)
plt.legend(loc='best')
plt.xlabel('TGF-β $(ng/mL)$')
#plt.ylabel('$F_c(T_β)$')
plt.ylabel('$F_g(T_β)$')
#plt.xscale('log')
#plt.ylim(0,30)
#plt.savefig("COVID_fitting.png", dpi=300, bbox_inches='tight')
plt.show()
