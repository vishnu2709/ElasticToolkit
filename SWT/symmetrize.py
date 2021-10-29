import numpy as np
import sys

cfile = sys.argv[1]
simtype = float(sys.argv[2])

Cij = np.zeros([6, 6])
Cij_symm = np.zeros([6,6])
g = open(cfile, "r")
lines = g.readlines()
for i in range(len(lines)):
    data = lines[i].strip().split()
    for j in range(0, 6):
        Cij[i, j] = float(data[j])
g.close()


if simtype == 1:  # Tetragonal
    Cij_symm[0, 0] = (1.0/2.0)*(Cij[0,0] + Cij[1,1])
    Cij_symm[1, 1] = Cij_symm[0, 0]
    Cij_symm[2, 2] = Cij[2, 2]
    Cij_symm[0, 1] = (1.0/2.0)*(Cij[0,1] + Cij[1,0])
    Cij_symm[0, 2] = (1.0/4.0)*(Cij[0,2] + Cij[1,2] + Cij[2,0] + Cij[2,1])
    Cij_symm[1, 2] = Cij_symm[0, 2]
    Cij_symm[1, 0] = Cij_symm[0, 1]
    Cij_symm[2, 0] = Cij_symm[0, 2]
    Cij_symm[2, 1] = Cij_symm[0, 2]
    Cij_symm[3, 3] = (1.0/2.0)*(Cij[3,3] + Cij[4,4])
    Cij_symm[4, 4] = Cij_symm[3, 3]
    Cij_symm[5, 5] = Cij[5, 5]

elif simtype == 2:  # Cubic
    Cij_symm[0, 0] = (1.0/3.0)*(Cij[0,0] + Cij[1,1] + Cij[2,2])
    Cij_symm[1, 1] = Cij_symm[0, 0]
    Cij_symm[2, 2] = Cij_symm[0, 0]
    Cij_symm[0, 1] = (1.0/6.0)*(Cij[0,1] + Cij[0,2] + Cij[1,2] + Cij[1,0] + Cij[2,0] + Cij[2,1])
    Cij_symm[0, 2] = Cij_symm[0, 1]
    Cij_symm[1, 2] = Cij_symm[0, 1]
    Cij_symm[1, 0] = Cij_symm[0, 1]
    Cij_symm[2, 0] = Cij_symm[0, 1]
    Cij_symm[2, 1] = Cij_symm[0, 1]
    Cij_symm[3, 3] = (1.0/3.0)*(Cij[3,3] + Cij[4,4] + Cij[5,5])
    Cij_symm[4, 4] = Cij_symm[3, 3]
    Cij_symm[5, 5] = Cij_symm[3, 3]

elif simtype == 3:  # Orthorhombic 
    Cij_symm[0, 0] = Cij[0, 0]
    Cij_symm[1, 1] = Cij[1, 1]
    Cij_symm[2, 2] = Cij[2, 2]
    Cij_symm[0, 1] = (1.0/2.0)*(Cij[0, 1] + Cij[1, 0])
    Cij_symm[1, 0] = Cij_symm[0, 1]
    Cij_symm[0, 2] = (1.0/2.0)*(Cij[0, 2] + Cij[2, 0])
    Cij_symm[2, 0] = Cij_symm[0, 2]
    Cij_symm[1, 2] = (1.0/2.0)*(Cij[1, 2] + Cij[2, 1])
    Cij_symm[2, 1] = Cij_symm[1, 2]
    Cij_symm[3, 3] = Cij[3, 3]
    Cij_symm[4, 4] = Cij[4, 4]
    Cij_symm[5, 5] = Cij[5, 5]

elif simtype == 4: # Voight only
    Cij_symm = 0.5*(Cij + np.transpose(Cij))

h = open("Cij_symm.dat", "w")
for i in range(0, 6):
    line = '%12f  %12f  %12f %12f %12f %12f' % (Cij_symm[i,0], Cij_symm[i,1], 
            Cij_symm[i,2], Cij_symm[i,3], Cij_symm[i,4], Cij_symm[i,5])
    h.write(line + "\n")
h.close()
