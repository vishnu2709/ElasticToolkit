from create_strains import create_deformation_gradient
from shutil import copy2
import numpy as np
import os
import sys

eta = float(sys.argv[1])
# C112 strains
strain_mat1 = np.array([[eta, 0, 0], [0, eta, 0], [0, 0, 0]])
strain_mat2 = np.array([[-eta,0, 0], [0, -eta, 0], [0, 0, 0]])
strain_mat3 = np.array([[0, 0, 0], [0, eta, 0], [0, 0, 0]])
strain_mat4 = np.array([[0, 0, 0], [0, -eta, 0], [0, 0, 0]])
strain_mat5 = np.array([[-eta, 0, 0], [0, eta, 0], [0, 0, 0]])
strain_mat6 = np.array([[eta, 0, 0], [0, -eta, 0], [0, 0, 0]])
# C111 strains
strain_mat7 = np.array([[2*eta, 0, 0], [0, 0, 0], [0, 0, 0]])
strain_mat8 = np.array([[eta, 0, 0], [0, 0, 0], [0, 0, 0]])
strain_mat9 = np.array([[-eta, 0, 0], [0, 0, 0], [0, 0, 0]])
strain_mat10 = np.array([[-2*eta, 0, 0], [0, 0, 0], [0, 0, 0]])
# C123 strains
strain_mat11 = np.array([[eta, 0, 0], [0, eta, 0], [0, 0, eta]])
strain_mat12 = np.array([[-eta, 0, 0], [0, eta, 0], [0, 0, eta]])
strain_mat13 = np.array([[eta, 0, 0], [0, -eta, 0], [0, 0, eta]])
strain_mat14 = np.array([[-eta, 0, 0], [0, -eta, 0], [0, 0, eta]])
strain_mat15 = np.array([[eta, 0, 0], [0, eta, 0], [0, 0, -eta]])
strain_mat16 = np.array([[-eta, 0, 0], [0, eta, 0], [0, 0, -eta]])
strain_mat17 = np.array([[eta, 0, 0], [0, -eta, 0], [0, 0, -eta]])
strain_mat18 = np.array([[-eta, 0, 0], [0, -eta, 0], [0, 0, -eta]])
# C144 strains (some included in C111)
strain_mat19 = np.array([[eta, 0, 0], [0, 0, eta], [0, eta, 0]])
strain_mat20 = np.array([[eta, 0, 0], [0, 0, -eta], [0, -eta, 0]])
strain_mat21 = np.array([[-eta, 0, 0], [0, 0, eta], [0, eta, 0]])
strain_mat22 = np.array([[-eta, 0, 0], [0, 0, -eta], [0, -eta, 0]])
# C166 strains (some included in C111)
strain_mat23 = np.array([[eta, eta, 0], [eta, 0, 0], [0, 0, 0]])
strain_mat24 = np.array([[eta, -eta, 0], [-eta, 0, 0], [0, 0, 0]])
strain_mat25 = np.array([[-eta, eta, 0], [eta, 0, 0], [0, 0, 0]])
strain_mat26 = np.array([[-eta, -eta, 0], [-eta, 0, 0], [0, 0, 0]])
# C456 strains
strain_mat27 = np.array([[0, eta, eta], [eta, 0, eta], [eta, eta, 0]])
strain_mat28 = np.array([[0, eta, eta], [eta, 0, -eta], [eta, -eta, 0]])
strain_mat29 = np.array([[0, eta, -eta], [eta, 0, eta], [-eta, eta, 0]])
strain_mat30 = np.array([[0, eta, -eta], [eta, 0, -eta], [-eta, -eta, 0]])
strain_mat31 = np.array([[0, -eta, eta], [-eta, 0, eta], [eta, eta, 0]])
strain_mat32 = np.array([[0, -eta, eta], [-eta, 0, -eta], [eta, -eta, 0]])
strain_mat33 = np.array([[0, -eta, -eta], [-eta, 0, eta], [-eta, eta, 0]])
strain_mat34 = np.array([[0, -eta, -eta], [-eta, 0, -eta], [-eta, -eta, 0]])


strain_mat = [strain_mat1, strain_mat2, strain_mat3, strain_mat4, 
        strain_mat5, strain_mat6, strain_mat7, strain_mat8, strain_mat9, 
        strain_mat10, strain_mat11, strain_mat12, strain_mat13, strain_mat14,
        strain_mat15, strain_mat16, strain_mat17, strain_mat18,
        strain_mat19, strain_mat20, strain_mat21, strain_mat22,
        strain_mat23, strain_mat24, strain_mat25, strain_mat26,
        strain_mat27, strain_mat28, strain_mat29, strain_mat30,
        strain_mat31, strain_mat32, strain_mat33, strain_mat34]

for i in range(1, len(strain_mat)+1):
    dirname = "straintype-"+str(i)+"-"+str(eta) 
    if not os.path.exists(dirname):
        os.makedirs(dirname)

    copy2("INCAR", dirname)
    copy2("KPOINTS", dirname)
    copy2("POTCAR", dirname)

    defmat = create_deformation_gradient(strain_mat[i-1])

    f = open("CONTCAR", "r")
    data = f.readlines()
    f.close()

    lv1 = map(float, data[2].strip().split())
    lv2 = map(float, data[3].strip().split())
    lv3 = map(float, data[4].strip().split())

    lv1 = np.matmul(defmat, np.array(lv1))
    lv2 = np.matmul(defmat, np.array(lv2))
    lv3 = np.matmul(defmat, np.array(lv3))

    g = open(dirname + "/POSCAR", "w")
    g.writelines(data[0:2])
    g.write("     " + str("%.16f" % lv1[0]) + "    " + str("%.16f" % lv1[1])
        + "    " + str("%.16f" % lv1[2]) + "\n")
    g.write("     " + str("%.16f" % lv2[0]) + "    " + str("%.16f" % lv2[1])
        + "    " + str("%.16f" % lv2[2]) + "\n")
    g.write("     " + str("%.16f" % lv3[0]) + "    " + str("%.16f" % lv3[1])
        + "    " + str("%.16f" % lv3[2]) + "\n")
    g.writelines(data[5:])
    g.close()
