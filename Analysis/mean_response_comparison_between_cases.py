import glob
from Butyrate.mcds.pyMCDS import pyMCDS
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt  # if you want to plot results
import random, pickle
import os
import seaborn as sns
from pylab import  array, linspace, subplots

#path = ["" for _ in range(4)]
path = ["" for _ in range(2)]


path[0] = 'C:/Users/maislam4/OneDrive - University at Buffalo/Desktop/PhysiCell_R/Final_updated/replicate_51/plot/'
path[1] = 'C:/Users/maislam4/OneDrive - University at Buffalo/Desktop/PhysiCell_R/Final_updated/replicate_61/plot/'
#path[2] = 'C:/Users/maislam4/OneDrive - University at Buffalo/Desktop/PhysiCell_R/Final_updated/replicate_72/plot/'
#path[3] = 'C:/Users/maislam4/OneDrive - University at Buffalo/Desktop/PhysiCell_R/Final_updated/replicate_71/plot/'

plt.rcParams.update({'font.size': 15})
fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()
fig3, ax3 = plt.subplots()
fig4, ax4 = plt.subplots()
fig5, ax5 = plt.subplots()
fig6, ax6 = plt.subplots()

for i in range(len(path)):
    os.chdir(path[i])

    cell1 = np.array(pickle.load(open('cell1.p', 'rb')))
    cell2 = np.array(pickle.load(open('cell2.p', 'rb')))
    cell3 = np.array(pickle.load(open('cell3.p', 'rb')))
    cell4 = np.array(pickle.load(open('cell4.p', 'rb')))
    cell5 = np.array(pickle.load(open('cell5.p', 'rb')))
    cell6 = np.array(pickle.load(open('cell6.p', 'rb')))
    cell7 = np.array(pickle.load(open('cell7.p', 'rb')))
    cell8 = np.array(pickle.load(open('cell8.p', 'rb')))
    cell9 = np.array(pickle.load(open('cell9.p', 'rb')))
    cell10 = np.array(pickle.load(open('cell10.p', 'rb')))
    cell11 = np.array(pickle.load(open('cell11.p', 'rb')))
    cell12 = np.array(pickle.load(open('cell12.p', 'rb')))
    cell13 = np.array(pickle.load(open('cell13.p', 'rb')))
    cell14 = np.array(pickle.load(open('cell14.p', 'rb')))
    cell15 = np.array(pickle.load(open('cell15.p', 'rb')))
    time = np.array(pickle.load(open('time.p', 'rb')))

    CD8 = np.array(
        [cell1[0], cell2[0], cell3[0], cell4[0], cell5[0], cell6[0], cell7[0], cell8[0], cell9[0], cell10[0], cell11[0],
         cell12[0], cell13[0], cell14[0], cell15[0]])
    macrophage = np.array(
        [cell1[1], cell2[1], cell3[1], cell4[1], cell5[1], cell6[1], cell7[1], cell8[1], cell9[1], cell10[1], cell11[1],
         cell12[1], cell13[1], cell14[1], cell15[1]])
    secreteing_agent = np.array(
        [cell1[2], cell2[2], cell3[2], cell4[2], cell5[2], cell6[2], cell7[2], cell8[2], cell9[2], cell10[2], cell11[2],
         cell12[2], cell13[2], cell14[2], cell15[2]])
    fibroblast = np.array(
        [cell1[3], cell2[3], cell3[3], cell4[3], cell5[3], cell6[3], cell7[3], cell8[3], cell9[3], cell10[3], cell11[3],
         cell12[3], cell13[3], cell14[3], cell15[3]])
    TGF = np.array(
        [cell1[7], cell2[7], cell3[7], cell4[7], cell5[7], cell6[7], cell7[7], cell8[7], cell9[7], cell10[7], cell11[7],
         cell12[7], cell13[7], cell14[7], cell15[7]])
    collagen = np.array(
        [cell1[8], cell2[8], cell3[8], cell4[8], cell5[8], cell6[8], cell7[8], cell8[8], cell9[8], cell10[8], cell11[8],
         cell12[8], cell13[8], cell14[8], cell15[8]])
    t = np.array([time, time, time, time, time, time, time, time, time, time, time, time, time, time, time])

    mean_CD8 = np.mean(CD8, axis=0)
    mean_macrophage = np.mean(macrophage, axis=0)
    mean_secreteing_agent = np.mean(secreteing_agent, axis=0)
    mean_fibroblast = np.mean(fibroblast, axis=0)
    mean_TGF = np.mean(TGF, axis=0)
    mean_collagen = np.mean(collagen, axis=0)


    ax1.plot(time, mean_CD8, linewidth=2)
    ax2.plot(time, mean_macrophage, linewidth=2)
    ax3.plot(time, mean_secreteing_agent, linewidth=2)
    ax4.plot(time, mean_fibroblast, linewidth=2)
    ax5.plot(time, mean_TGF, linewidth=2)
    ax6.plot(time, mean_collagen, linewidth=2)

pathC = 'C:/Users/maislam4/OneDrive - University at Buffalo/Desktop/PhysiCell_R/Final_updated/plot_average/'
os.chdir(pathC)
#plt.legend(loc='upper left', prop={"size":15})
ax1.set_xlabel('Time (day)')
ax1.set_ylabel('Number of CD8+ T')
ax1.set_ylim([-20,450])
ax1.legend(['Baseline', 'Delayed rule'])
#ax1.legend(['$D = 3000$ $μm^2/min$', '$D = 300$ $μm^2/min$', '$D = 30$ $μm^2/min$', '$D = 3$ $μm^2/min$'])
fig1.savefig("CD8.png", dpi=300, bbox_inches='tight')

ax2.set_xlabel('Time (day)')
ax2.set_ylabel('Number of Macrophage')
ax2.set_ylim([-20,450])
ax2.legend(['Baseline', 'Delayed rule'])
#ax2.legend(['$D = 3000$ $μm^2/min$', '$D = 300$ $μm^2/min$', '$D = 30$ $μm^2/min$', '$D = 3$ $μm^2/min$'])
fig2.savefig("Macrophage.png", dpi=300, bbox_inches='tight')

ax3.set_xlabel('Time (day)')
ax3.set_ylabel('Number of Secreting agent')
ax3.set_ylim([-20,450])
ax3.legend(['Baseline', 'Delayed rule'])
#ax3.legend(['$D = 3000$ $μm^2/min$', '$D = 300$ $μm^2/min$', '$D = 30$ $μm^2/min$', '$D = 3$ $μm^2/min$'])
fig3.savefig("Secreting agent.png", dpi=300, bbox_inches='tight')

ax4.set_xlabel('Time (day)')
ax4.set_ylabel('Number of Fibroblast')
ax4.set_ylim([-20,450])
ax4.legend(['Baseline', 'Delayed rule'])
#ax4.legend(['$D = 3000$ $μm^2/min$', '$D = 300$ $μm^2/min$', '$D = 30$ $μm^2/min$', '$D = 3$ $μm^2/min$'])
fig4.savefig("Fibroblast", dpi=300, bbox_inches='tight')

ax5.set_xlabel('Time (day)')
ax5.set_ylabel('TGF-β ($ng/mL$)')
ax5.set_ylim([-0.25, 11])
ax5.legend(['Baseline', 'Delayed rule'])
#ax5.legend(['$D = 3000$ $μm^2/min$', '$D = 300$ $μm^2/min$', '$D = 30$ $μm^2/min$', '$D = 3$ $μm^2/min$'])
fig5.savefig("TGF", dpi=300, bbox_inches='tight')

ax6.set_xlabel('Time (day)')
ax6.set_ylabel('Collagen ($μg/μm^3$)')
ax6.set_ylim([-0.25e-8,11e-8])
ax6.legend(['Baseline', 'Delayed rule'])
#ax6.legend(['$D = 3000$ $μm^2/min$', '$D = 300$ $μm^2/min$', '$D = 30$ $μm^2/min$', '$D = 3$ $μm^2/min$'])
fig6.savefig("Collagen", dpi=300, bbox_inches='tight')

