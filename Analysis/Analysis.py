import glob
from pyMCDS import pyMCDS
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


######### user input #############
group = 'DM'
replication = 15

root_directory = os.getcwd()
try:
    os.chdir(group)
except:
    print('No folder found! Add a template directory and run simulation file')

collagen_area = np.zeros(replication)

path = root_directory+ '\\' + group + '\\'

path2 = path + 'plot'
try:
    os.chdir(path2)
except:
    os.mkdir('plot')

pathC = path + 'Collagen_contour'
try:
    os.chdir(pathC)
except:
    os.mkdir('Collagen_contour')

os.chdir(root_directory)
pathCV = root_directory +'\\' + 'Collagen_violin'
try:
    os.chdir(pathCV)
except:
    os.mkdir('Collagen_violin')

for replication in range(replication):
    itc = replication + 1
    path1 = path + str(itc) + '\output'
    os.chdir(path1)
    xml_files = glob.glob('output*.xml')
    xml_files.sort()

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
    M1 = np.zeros(n)
    M2 = np.zeros(n)
    MI = np.zeros(n)
    MH = np.zeros(n)
    ME = np.zeros(n)
    idx = 0
    TGFa = [[] for _ in range(n)]
    collagena = [[] for _ in range(n)]
    timea = [[] for _ in range(n)]

    for f in xml_files:
        mcds = pyMCDS(f, '.')
        t[idx] = mcds.get_time()

        cycle = mcds.data['discrete_cells']['cycle_model']
        cycle = cycle.astype(int)
        phase = mcds.data['discrete_cells']['ability_to_phagocytose_infected_cell']
        phase = phase.astype(int)
        active = mcds.data['discrete_cells']['activated_immune_cell']
        active = active.astype(int)
        ex = mcds.data['discrete_cells']['M2_phase']
        ex = ex.astype(int)
        ex2 = mcds.data['discrete_cells']['total_volume']
        ex2 = ex2.astype(int)
        cell_type = mcds.data['discrete_cells']['cell_type']
        cell_type = cell_type.astype(int)


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

        mac1 = np.where((cell_type == 4) & (cycle < 100) & (active == 1) & (ex == 0))
        M1[idx] = len(mac1[0])
        mac2 = np.where((cell_type == 4) & (cycle < 100) & (ex == 1))
        M2[idx] = len(mac2[0])
        mac3 = np.where((cell_type == 4) & (cycle < 100) & (active == 0))
        MI[idx] = len(mac3[0])
        mac4 = np.where((cell_type == 4) & (cycle < 100) & (phase == 1))
        MH[idx] = len(mac4[0])
        mac5 = np.where((cell_type == 4) & (cycle < 100) & (ex2 > 6500))
        ME[idx] = len(mac5[0])

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


    cell1 = np.array([CD8, macrophage, secreting_agent, fibroblast, uninfected, infected, dead, TGF, collagen, M1, M2, MI, MH, ME])


    os.chdir(path2)
    pickle.dump(t / (60 * 24), open('time.p', 'wb'))
    pickle.dump(cell1, open('cell'+str(itc)+'.p', 'wb'))

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

    os.chdir(pathC)
    plt.savefig(group + str(itc)+".png", dpi=300, bbox_inches='tight')
    plt.clf()


os.chdir(pathCV)

pickle.dump(collagen_area, open('CV'+group+'.p', 'wb'))
