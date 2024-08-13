import numpy as np
import h5py

with open('test.txt','w') as f:
    f.write('fgdfg')

SpecA13 = np.genfromtxt('C:/Users/rasmu/OneDrive/FysTek_Semester3/10387/scientific_computing/jens/SPEC_1.3_A.csv', skip_header=45, delimiter=',')
SpecA25 = np.genfromtxt('C:/Users/rasmu/OneDrive/FysTek_Semester3/10387/scientific_computing/jens/SPEC_2.5_A.csv', skip_header=45, delimiter=',')
SpecA34 = np.genfromtxt('C:/Users/rasmu/OneDrive/FysTek_Semester3/10387/scientific_computing/jens/SPEC_3.4_A.csv', skip_header=45, delimiter=',')

print(SpecA13.shape)

# Python program to create a m x n x j matrix 
# with all 0s 
m = 5000
n = 2
j = 3
  
a = [[[0 for x in range(n)] for x in range(m)] for x in range(j)]
a = np.array(a)

for x in range(n):
    for y in range(m):
        for z in range(j):
            if z==0:
                a[z][y][x] = SpecA13[y][x]
            if z==1:
                a[z][y][x] = SpecA25[y][x]
            else:
                a[z][y][x] = SpecA34[y][x]

hdf5_path = 'C:/Users/rasmu/OneDrive/FysTek_Semester3/10387/scientific_computing/asdf/data.hdf5'

with h5py.File(hdf5_path, 'w') as hdf5_file:
    hdf5_file.create_dataset('dataset', data=a)