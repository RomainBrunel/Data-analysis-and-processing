import numpy as np
import h5py

SpecA13 = np.genfromtxt('jens/SPEC_1.3_A.csv', skip_header=45, delimiter=',')
SpecA25 = np.genfromtxt('jens/SPEC_2.5_A.csv', skip_header=45, delimiter=',')
SpecA34 = np.genfromtxt('jens/SPEC_3.4_A.csv', skip_header=45, delimiter=',')

SpecS13 = np.genfromtxt('jens/SPEC_1.3_S.csv', skip_header=45, delimiter=',')
SpecS25 = np.genfromtxt('jens/SPEC_2.5_S.csv', skip_header=45, delimiter=',')
SpecS34 = np.genfromtxt('jens/SPEC_3.4_S.csv', skip_header=45, delimiter=',')

PowA05 = np.genfromtxt('jens/5MHz_0.5_A.csv', skip_header=45, delimiter=',')
PowA11 = np.genfromtxt('jens/5MHz_1.1_A.csv', skip_header=45, delimiter=',')
PowA14 = np.genfromtxt('jens/5MHz_1.4_A.csv', skip_header=45, delimiter=',')
PowA19 = np.genfromtxt('jens/5MHz_1.9_A.csv', skip_header=45, delimiter=',')
PowA24 = np.genfromtxt('jens/5MHz_2.4_A.csv', skip_header=45, delimiter=',')
PowA29 = np.genfromtxt('jens/5MHz_2.9_A.csv', skip_header=45, delimiter=',')
PowA34 = np.genfromtxt('jens/5MHz_3.4_A.csv', skip_header=45, delimiter=',')
PowA36 = np.genfromtxt('jens/5MHz_3.6_A.csv', skip_header=45, delimiter=',')
PowA43 = np.genfromtxt('jens/5MHz_4.3_A.csv', skip_header=45, delimiter=',')
PowA47 = np.genfromtxt('jens/5MHz_4.7_A.csv', skip_header=45, delimiter=',')

PowS05 = np.genfromtxt('jens/5MHz_0.5_A.csv', skip_header=45, delimiter=',')
PowS11 = np.genfromtxt('jens/5MHz_1.1_A.csv', skip_header=45, delimiter=',')
PowS14 = np.genfromtxt('jens/5MHz_1.4_A.csv', skip_header=45, delimiter=',')
PowS19 = np.genfromtxt('jens/5MHz_1.9_A.csv', skip_header=45, delimiter=',')
PowS24 = np.genfromtxt('jens/5MHz_2.4_A.csv', skip_header=45, delimiter=',')
PowS29 = np.genfromtxt('jens/5MHz_2.9_A.csv', skip_header=45, delimiter=',')
PowS34 = np.genfromtxt('jens/5MHz_3.4_A.csv', skip_header=45, delimiter=',')
PowS36 = np.genfromtxt('jens/5MHz_3.6_A.csv', skip_header=45, delimiter=',')
PowS43 = np.genfromtxt('jens/5MHz_4.3_A.csv', skip_header=45, delimiter=',')
PowS47 = np.genfromtxt('jens/5MHz_4.7_A.csv', skip_header=45, delimiter=',')

A = np.vstack((SpecA13, SpecA25, SpecA34)).reshape(3,5000,2)
B = np.vstack((SpecS13, SpecS25, SpecS34)).reshape(3,5000,2)
C = np.vstack((PowA05, PowA11, PowA14, PowA19, PowA24, PowA29, PowA34, PowS36, PowS43, PowS47)).reshape(10,5000,2)
D = np.vstack((PowS05, PowS11, PowS14, PowS19, PowS24, PowS29, PowS34, PowS36, PowS43, PowS47)).reshape(10,5000,2)


with h5py.File('jens_data.hdf5', 'w') as hdf5_file:
    hdf5_file.create_dataset('data_Spec_A', data=A)
    hdf5_file.create_dataset('data_Spec_S', data=B)
    hdf5_file.create_dataset('data_Pow_A', data=C)
    hdf5_file.create_dataset('data_Pow_S', data=D)