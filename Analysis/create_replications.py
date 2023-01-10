import os

######### user input #############
group = 'DM'
replication = 15

root_directory = os.getcwd()
try:
    os.chdir(group)
except:
    print('Add a template directory for simulation')

path = root_directory+ '\\' + group + '\\'

for i in range(replication):
    itc = i + 1
    os.chdir(path)
    new_simulation = 'cp -rf template ' + str(itc)
    os.system(new_simulation)

    path1 = path + str(itc)
    os.chdir(path1)
    os.system("start /B make data-cleanup & make & .\COVID19")