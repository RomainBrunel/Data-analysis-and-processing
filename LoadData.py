import numpy as np
import h5py

SpecA13 = np.genfromtxt('C:/Users/rasmu/OneDrive/FysTek_Semester3/10387/scientific_computing/jens/SPEC_1.3_A.csv', skip_header=45, delimiter=',')
SpecA25 = np.genfromtxt('C:/Users/rasmu/OneDrive/FysTek_Semester3/10387/scientific_computing/jens/SPEC_2.5_A.csv', skip_header=45, delimiter=',')
SpecA34 = np.genfromtxt('C:/Users/rasmu/OneDrive/FysTek_Semester3/10387/scientific_computing/jens/SPEC_3.4_A.csv', skip_header=45, delimiter=',')

SpecS13 = np.genfromtxt('C:/Users/rasmu/OneDrive/FysTek_Semester3/10387/scientific_computing/jens/SPEC_1.3_S.csv', skip_header=45, delimiter=',')
SpecS25 = np.genfromtxt('C:/Users/rasmu/OneDrive/FysTek_Semester3/10387/scientific_computing/jens/SPEC_2.5_S.csv', skip_header=45, delimiter=',')
SpecS34 = np.genfromtxt('C:/Users/rasmu/OneDrive/FysTek_Semester3/10387/scientific_computing/jens/SPEC_3.4_S.csv', skip_header=45, delimiter=',')

PowA05 = np.genfromtxt('C:/Users/rasmu/OneDrive/FysTek_Semester3/10387/scientific_computing/jens/5MHz_0.5_A.csv', skip_header=45, delimiter=',')
PowA11 = np.genfromtxt('C:/Users/rasmu/OneDrive/FysTek_Semester3/10387/scientific_computing/jens/5MHz_1.1_A.csv', skip_header=45, delimiter=',')
PowA14 = np.genfromtxt('C:/Users/rasmu/OneDrive/FysTek_Semester3/10387/scientific_computing/jens/5MHz_1.4_A.csv', skip_header=45, delimiter=',')
PowA19 = np.genfromtxt('C:/Users/rasmu/OneDrive/FysTek_Semester3/10387/scientific_computing/jens/5MHz_1.9_A.csv', skip_header=45, delimiter=',')
PowA24 = np.genfromtxt('C:/Users/rasmu/OneDrive/FysTek_Semester3/10387/scientific_computing/jens/5MHz_2.4_A.csv', skip_header=45, delimiter=',')
PowA29 = np.genfromtxt('C:/Users/rasmu/OneDrive/FysTek_Semester3/10387/scientific_computing/jens/5MHz_2.9_A.csv', skip_header=45, delimiter=',')
PowA34 = np.genfromtxt('C:/Users/rasmu/OneDrive/FysTek_Semester3/10387/scientific_computing/jens/5MHz_3.4_A.csv', skip_header=45, delimiter=',')
PowA36 = np.genfromtxt('C:/Users/rasmu/OneDrive/FysTek_Semester3/10387/scientific_computing/jens/5MHz_3.6_A.csv', skip_header=45, delimiter=',')
PowA43 = np.genfromtxt('C:/Users/rasmu/OneDrive/FysTek_Semester3/10387/scientific_computing/jens/5MHz_4.3_A.csv', skip_header=45, delimiter=',')
PowA47 = np.genfromtxt('C:/Users/rasmu/OneDrive/FysTek_Semester3/10387/scientific_computing/jens/5MHz_4.7_A.csv', skip_header=45, delimiter=',')

PowS05 = np.genfromtxt('C:/Users/rasmu/OneDrive/FysTek_Semester3/10387/scientific_computing/jens/5MHz_0.5_A.csv', skip_header=45, delimiter=',')
PowS11 = np.genfromtxt('C:/Users/rasmu/OneDrive/FysTek_Semester3/10387/scientific_computing/jens/5MHz_1.1_A.csv', skip_header=45, delimiter=',')
PowS14 = np.genfromtxt('C:/Users/rasmu/OneDrive/FysTek_Semester3/10387/scientific_computing/jens/5MHz_1.4_A.csv', skip_header=45, delimiter=',')
PowS19 = np.genfromtxt('C:/Users/rasmu/OneDrive/FysTek_Semester3/10387/scientific_computing/jens/5MHz_1.9_A.csv', skip_header=45, delimiter=',')
PowS24 = np.genfromtxt('C:/Users/rasmu/OneDrive/FysTek_Semester3/10387/scientific_computing/jens/5MHz_2.4_A.csv', skip_header=45, delimiter=',')
PowS29 = np.genfromtxt('C:/Users/rasmu/OneDrive/FysTek_Semester3/10387/scientific_computing/jens/5MHz_2.9_A.csv', skip_header=45, delimiter=',')
PowS34 = np.genfromtxt('C:/Users/rasmu/OneDrive/FysTek_Semester3/10387/scientific_computing/jens/5MHz_3.4_A.csv', skip_header=45, delimiter=',')
PowS36 = np.genfromtxt('C:/Users/rasmu/OneDrive/FysTek_Semester3/10387/scientific_computing/jens/5MHz_3.6_A.csv', skip_header=45, delimiter=',')
PowS43 = np.genfromtxt('C:/Users/rasmu/OneDrive/FysTek_Semester3/10387/scientific_computing/jens/5MHz_4.3_A.csv', skip_header=45, delimiter=',')
PowS47 = np.genfromtxt('C:/Users/rasmu/OneDrive/FysTek_Semester3/10387/scientific_computing/jens/5MHz_4.7_A.csv', skip_header=45, delimiter=',')

# Python program to create a m x n x j (for Spec) and m x n x k (for Pow) matrix 
# with all 0s 
m = 5000
n = 2
j = 3
k = 10

#List for SpecA

a = [[[0. for x in range(n)] for y in range(m)] for z in range(j)]
a = np.array(a)

#List for SpecS

b = [[[0. for x in range(n)] for y in range(m)] for z in range(j)]
b = np.array(b)

# List for PowA

c = [[[0. for x in range(n)] for y in range(m)] for z in range(k)]
c = np.array(c)

# List for PowS
d = [[[0. for x in range(n)] for y in range(m)] for z in range(k)]
d = np.array(d)

#Update values

for x in range(n):
    for y in range(m):
        for z in range(j):
            if z==0:
                a[z][y][x] = SpecA13[y][x]
                b[z][y][x] = SpecS13[y][x]
            if z==1:
                a[z][y][x] = SpecA25[y][x]
                b[z][y][x] = SpecS25[y][x]
            else:
                a[z][y][x] = SpecA34[y][x]
                b[z][y][x] = SpecS34[y][x]

for x in range(n):
    for y in range(m):
        for z in range(k):
            if z==0:
                c[z][y][x] = PowA05[y][x]
                d[z][y][x] = PowS05[y][x]
            if z==1:
                c[z][y][x] = PowA11[y][x]
                d[z][y][x] = PowS11[y][x]
            if z==2:
                c[z][y][x] = PowA14[y][x]
                d[z][y][x] = PowS14[y][x]
            if z==3:
                c[z][y][x] = PowA19[y][x]
                d[z][y][x] = PowS19[y][x]
            if z==4:
                c[z][y][x] = PowA24[y][x]
                d[z][y][x] = PowS24[y][x]
            if z==5:
                c[z][y][x] = PowA29[y][x]
                d[z][y][x] = PowS29[y][x]
            if z==6:
                c[z][y][x] = PowA34[y][x]
                d[z][y][x] = PowS34[y][x]
            if z==7:
                c[z][y][x] = PowA36[y][x]
                d[z][y][x] = PowS36[y][x]
            if z==8:
                c[z][y][x] = PowA43[y][x]
                d[z][y][x] = PowS43[y][x]
            else:
                c[z][y][x] = PowA47[y][x]
                d[z][y][x] = PowS47[y][x]

hdf5_path_SpecA = 'C:/Users/rasmu/OneDrive/FysTek_Semester3/10387/scientific_computing/asdf/data_Spec_A.hdf5'
hdf5_path_SpecS = 'C:/Users/rasmu/OneDrive/FysTek_Semester3/10387/scientific_computing/asdf/data_Spec_S.hdf5'
hdf5_path_PowA = 'C:/Users/rasmu/OneDrive/FysTek_Semester3/10387/scientific_computing/asdf/data_Pow_A.hdf5'
hdf5_path_PowS = 'C:/Users/rasmu/OneDrive/FysTek_Semester3/10387/scientific_computing/asdf/data_Pow_S.hdf5'

print(c)

with h5py.File(hdf5_path_SpecA, 'w') as hdf5_file:
    hdf5_file.create_dataset('dataset', data=a)

with h5py.File(hdf5_path_SpecS, 'w') as hdf5_file:
    hdf5_file.create_dataset('dataset', data=b)

with h5py.File(hdf5_path_PowA, 'w') as hdf5_file:
    hdf5_file.create_dataset('dataset', data=c)

with h5py.File(hdf5_path_PowS, 'w') as hdf5_file:
    hdf5_file.create_dataset('dataset', data=d)