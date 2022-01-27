import os

path = 'C:/Users/maislam4/OneDrive - University at Buffalo/Desktop/PhysiCell_R/Final_updated/replicate_61/'
#path = 'C:/Users/maislam4/OneDrive - University at Buffalo/Desktop/PhysiCell_R/Final_updated/replicate_55/'
replication = 15

for i in range(replication):
    print(i)
    itc = i + 1
    os.chdir(path)
    new_simulation = 'cp -rf template ' + str(itc)
    os.system(new_simulation)

    path1 = path + str(itc)
    os.chdir(path1)
    os.system("start /B make data-cleanup & make & .\COVID19")

    print("success")



'''
path = 'C:/Users/maislam4/OneDrive - University at Buffalo/Desktop/PhysiCell_R/Final_updated/replicate_20/'
#path1 = 'C:/Users/maislam4/OneDrive - University at Buffalo/Desktop/PhysiCell_R/Final_updated/replicate_20/check'

os.chdir(path)

os.system('cp -rf template 1')
os.system('cp -rf template 2')
os.system('cp -rf template 3')
os.system('cp -rf template 4')
os.system('cp -rf template 5')
os.system('cp -rf template 6')
os.system('cp -rf template 7')
os.system('cp -rf template 8')
os.system('cp -rf template 9')
os.system('cp -rf template 10')
os.system('cp -rf template 11')
os.system('cp -rf template 12')
os.system('cp -rf template 13')
os.system('cp -rf template 14')
os.system('cp -rf template 15')
'''

'''
#os.system("@cmd /k make")
#os.system('cmd /c "start cmd.exe && make data-cleanup && make && ./COVID19"')
os.system("echo 'hello world'")
os.system('cmd /k "make data-cleanup"')
os.system("echo 'hello world'")
os.system('cmd /k "make"')
os.system("echo 'hello world'")
os.system('cmd /k "./COVID19"')
'''
