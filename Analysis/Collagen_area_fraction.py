import glob
from Butyrate.mcds.pyMCDS import pyMCDS
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import matplotlib.pyplot as plt  # if you want to plot results
import random, pickle
import pandas as pd
import seaborn as sns


#xold=[0.34, 0.351, 0.344, 0.292, 0.351, 0.335, 0.307, 0.241, 0.304, 0.291, 0.326, 0.313, 0.328, 0.299, 0.288, 0.298]
DM = np.array(pickle.load(open('CVreplicate_51.p', 'rb')))
D = np.array(pickle.load(open('CVreplicate_21.p', 'rb')))
M = np.array(pickle.load(open('CVreplicate_212.p', 'rb')))
DHMH = np.array(pickle.load(open('CVreplicate_52.p', 'rb')))
DLML = np.array(pickle.load(open('CVreplicate_53.p', 'rb')))
DHML = np.array(pickle.load(open('CVreplicate_54.p', 'rb')))
DLMH = np.array(pickle.load(open('CVreplicate_55.p', 'rb')))
ATL = np.array(pickle.load(open('CVreplicate_12.p', 'rb')))
ATH = np.array(pickle.load(open('CVreplicate_17.p', 'rb')))
dA = np.array(pickle.load(open('CVreplicate_61.p', 'rb')))

#x_data = np.array(['D+M','M', 'D'])
x_data = np.array(['DM','D', 'M', 'DHMH', 'DLML', 'DHML', 'DLMH', 'ATH', 'DdAM'])
#x_data = np.array(['DM','D', 'M', 'DHMH', 'DLML', 'DHML', 'DLMH', 'ATH'])
#x_data = np.array(['DM'])
#y_data = np.array([x72, x75, x70])

y_data = np.array([DM, D, M, DHMH, DLML, DHML, DLMH, ATH, dA])
#y_data = np.array([DM, D, M, DHMH, DLML, DHML, DLMH, ATH])
#y_data = np.array([DM])

y_data = np.transpose(y_data)
#print(y_data[0][0], y_data[1][0], y_data[0][1])
print(len(DM))
#print(y_data[:][1])
#print(y_data)

y_mean = np.mean(y_data, axis=0)
print(len(y_mean))


plt.rcParams.update({'font.size': 25})
sns.set_theme(style="whitegrid")
#ax = sns.violinplot(data=y_data, inner='points')
ax = sns.violinplot(data=y_data, color="white")
#ax = plt.boxplot(y_data)
ax.set_xticklabels(x_data)

for i in range(len(DM)):
    plt.scatter(x=range(len(y_mean)),y=y_data[:][i], c="red")
plt.ylabel('Collagen area fraction')
plt.savefig("00.png", dpi=300, bbox_inches='tight')
plt.show()


