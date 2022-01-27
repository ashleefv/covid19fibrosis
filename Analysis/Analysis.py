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

path = 'C:/Users/maislam4/OneDrive - University at Buffalo/Desktop/PhysiCell_R/Final_updated/replicate_61/'
group = "replicate_61"
replication = 15
collagen_area = np.zeros(replication)

for replication in range(replication):
    itc = replication + 1
    path1 = path + str(itc) + '/output/'
    os.chdir(path1)
    xml_files = glob.glob('output*.xml')
    xml_files.sort()
    #print(xml_files)

    n = len(xml_files)
    t = np.zeros(n)
    uninfected = np.zeros(n)
    infected = np.zeros(n)
    dead = np.zeros(n)
    CD8 = np.zeros(n)
    macrophage = np.zeros(n)
    secreting_agent = np.zeros(n)
    fibroblast = np.zeros(n)
    viron = np.zeros(n)
    collagen = np.zeros(n)
    TGF = np.zeros(n)
    pro = np.zeros(n)
    idx = 0
    TGFa = [[] for _ in range(n)]
    collagena = [[] for _ in range(n)]
    timea = [[] for _ in range(n)]

    for f in xml_files:
        mcds = pyMCDS(f, '.')
        t[idx] = mcds.get_time()

        cycle = mcds.data['discrete_cells']['cycle_model']
        cycle = cycle.astype(int)
        ID_uninfected = np.where((mcds.data['discrete_cells']['assembled_virion'] < 1) & (cycle < 100) & (
                    mcds.data['discrete_cells']['cell_type'] == 1))
        ID_infected = np.where((mcds.data['discrete_cells']['assembled_virion'] >= 1) & (cycle < 100) & (
                    mcds.data['discrete_cells']['cell_type'] == 1))
        dead_ID = np.where((cycle >= 100) & (mcds.data['discrete_cells']['cell_type'] == 1))
        uninfected[idx] = len(ID_uninfected[0])
        infected[idx] = len(ID_infected[0])

        dead[idx] = len(dead_ID[0])

        ID_CD8 = np.where((cycle < 100) & (mcds.data['discrete_cells']['cell_type'] == 3))

        CD8[idx] = len(ID_CD8[0])
        ID_fibroblast = np.where((cycle < 100) & (mcds.data['discrete_cells']['cell_type'] == 8))

        fibroblast[idx] = len(ID_fibroblast[0])

        ID_macrophage = np.where((cycle < 100) & (mcds.data['discrete_cells']['cell_type'] == 4))
        macrophage[idx] = len(ID_macrophage[0])

        ID_secreting_agent = np.where((cycle < 100) & (mcds.data['discrete_cells']['cell_type'] == 9))
        secreting_agent[idx] = len(ID_secreting_agent[0])

        z_val = 0.00
        sum = 0.0
        sum1 = 0.0
        xx1 = np.ravel(mcds.get_mesh()[:][0][0])

        plane_oxy = mcds.get_concentrations('collagen', z_slice=z_val)
        plane_oxy1 = mcds.get_concentrations('anti-inflammatory cytokine', z_slice=z_val)

        if t[idx] == 21599.999999:
            pickle.dump(plane_oxy, open('baseline.p', 'wb'))


        # average concentration
        count_average = 0
        for i in range(len(xx1)):
            for j in range(len(xx1)):
                sum = sum + plane_oxy[i][j]
                sum1 = sum1 + plane_oxy1[i][j]*1e12
                count_average = count_average + 1


        # individual grid concentration
        for i in range(len(xx1)):
            for j in range(len(xx1)):
                TGFa[idx].append(plane_oxy1[i][j]*1e12)
                collagena[idx].append(plane_oxy[i][j])
                timea[idx].append(mcds.get_time()/(60*24))

        collagen[idx] = sum/(count_average)
        TGF[idx] = sum1/(count_average)
        #print(sum1)

        idx += 1


    cell1 = np.array([CD8, macrophage, secreting_agent, fibroblast, uninfected, infected, dead, TGF, collagen])

    path2 = path + 'plot/'
    os.chdir(path2)
    pickle.dump(t / (60 * 24), open('time.p', 'wb'))
    pickle.dump(cell1, open('cell'+str(itc)+'.p', 'wb'))
    #pickle.dump(collagena, open('collagena1.p', 'wb'))
    #pickle.dump(TGFa, open('TGFa1.p', 'wb'))
    #pickle.dump(timea, open('timea1.p', 'wb'))

    plt.rcParams.update({'font.size': 25})
    fig1, ax1 = plt.subplots()
    #plt.ticklabel_format(axis="y", style="sci", scilimits=(0, 0))
    ax1.plot(timea, TGFa, linewidth=2)
    ax1.set_xlabel('Time (day)')
    ax1.set_ylabel('TGF-β ($ng/mL$)')
    ax1.set_ylim([-0.25, 11])

    pathT = 'C:/Users/maislam4/OneDrive - University at Buffalo/Desktop/PhysiCell_R/Final_updated/plot/TGF/'
    os.chdir(pathT)
    fig1.savefig(group + str(itc)+".png", dpi=300, bbox_inches='tight')

    plt.rcParams.update({'font.size': 25})
    fig2, ax2 = plt.subplots()
    #plt.ticklabel_format(axis="y", style="sci", scilimits=(0, 0))
    ax2.plot(timea, collagena, linewidth=2)
    ax2.set_xlabel('Time (day)')
    ax2.set_ylabel('Collagen ($μg/μm^3$)')
    #plt.ylim([-0.25e-12, 11e-12])

    pathC = 'C:/Users/maislam4/OneDrive - University at Buffalo/Desktop/PhysiCell_R/Final_updated/plot/Collagen/'
    os.chdir(pathC)
    fig2.savefig(group + str(itc)+".png", dpi=300, bbox_inches='tight')

    os.chdir(path1)
    # Seaborn heatmap
    plane_oxy = np.array(pickle.load(open('baseline.p', 'rb')))
    xx1 = np.linspace(0,800,40)
    yy1 = np.linspace(0,800,40)

    log_data = [ [0]*len(xx1) for i in range(len(yy1))]
    threshold_u = 1e-5
    threshold = 1e-7

    for i in range(len(xx1)):
        for j in range(len(yy1)):
            if plane_oxy[i][j] <= threshold:
                log_data[i][j] = np.nan

            if plane_oxy[i][j] > threshold:
                log_data[i][j] = np.log10(plane_oxy[i][j])


    count3 = 0
    count4= 0
    print(log_data[0][0], np.isnan(log_data[0][0]), np.nan)
    for i in range(len(log_data)):
        for j in range(len(log_data)):
            if np.isnan(log_data[i][j]):
                count3 = count3 + 1
                #check1.append(log_data[i][j])
            else:
                count4 = count4 + 1
    areaf = count4/1600
    print('c3', count3)
    print('c4', count4)
    print("Area", count4/1600)

    collagen_area[replication] = areaf

    plt.rcParams.update({'font.size': 25})
    ax = sns.heatmap(log_data, linewidths=0, linecolor='black', square=True, vmin=(np.log10(threshold)), vmax=(np.log10(threshold_u)), cbar_kws={'label': 'log[Collagen] $μg/μm^3$', 'orientation': 'vertical'}, linewidth=0.5)
    ax.set_xlabel('Grids in X-distance')
    ax.set_ylabel('Grids in Y-distance')
    ax.invert_yaxis()
    plt.title('AF = %f' %areaf)
    plt.xticks(np.arange(0, 42, step=5))
    plt.yticks(np.arange(0, 42, step=5))

    pathCC = 'C:/Users/maislam4/OneDrive - University at Buffalo/Desktop/PhysiCell_R/Final_updated/plot/Collagen_contour/'
    os.chdir(pathCC)
    plt.savefig(group + str(itc)+".png", dpi=300, bbox_inches='tight')

pathCV = 'C:/Users/maislam4/OneDrive - University at Buffalo/Desktop/PhysiCell_R/Final_updated/plot/Collagen_violin/'
os.chdir(pathCV)
pickle.dump(collagen_area, open('CV'+group+'.p', 'wb'))


'''
#pickle.dump(CD8 + macrophage + neutrophil + infected, open('totalIL6.p', 'wb'))
plt.rcParams.update({'font.size': 25})
#plt.plot(t/(60*24),uninfected, label='uninfected', linewidth=2)
#plt.plot(t/(60*24),infected, label='infected', linewidth=2)
#plt.plot(t/(60*24),dead, label='dead', linewidth=2)
#plt.plot(t/(60*24),(uninfected + infected + dead), label='Total', linewidth=2)
#plt.plot(t/(60*24),(uninfected[0] - uninfected - infected), label='Total dead', linewidth=2)
plt.plot(t / (60 * 24), cell1[0], label='CD8+ T cells', linewidth=2)
plt.plot(t / (60 * 24), cell1[1], label='Macrophage', linewidth=2)
plt.plot(t / (60 * 24), cell1[2], label='Secreting agent', linewidth=2)
#plt.plot(t / (60 * 24), infected, label='infected', linewidth=2)
#plt.plot(t / (60 * 24), CD8 + macrophage + neutrophil + infected, label='Total', linewidth=2)

plt.plot(t/(60*24),cell1[3], label='Fibroblast', linewidth=2)
plt.legend(loc='upper left')
plt.xlabel('Time (day)')
plt.ylabel('Number of Cells')
plt.show()



plt.rcParams.update({'font.size': 25})
plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
plt.plot(timea, TGFa, linewidth=2)
plt.xlabel('Time (day)')
plt.ylabel('TGF-β ($ng/μm^3$)')
plt.ylim([-0.25e-12,11e-12])
plt.show()

plt.rcParams.update({'font.size': 25})
plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
plt.plot(t / (60 * 24), cell1[7], linewidth=2)
plt.xlabel('Time (day)')
plt.ylabel('TGF-β ($ng/μm^3$)')
plt.ylim([-0.25e-12,11e-12])
plt.show()

plt.rcParams.update({'font.size': 25})
plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
plt.plot(t / (60 * 24), cell1[8], linewidth=2)
plt.xlabel('Time (day)')
plt.ylabel('Collagen')
plt.show()
'''