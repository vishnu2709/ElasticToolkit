from shutil import copy2
import sys
import subprocess
import os
import numpy as np

def run_VASP(dirname):
    runstring = "qvasp -p n12 -WholeNode"
    process = subprocess.Popen(runstring.split(), cwd=dirname)


def create_strain_list(setup_file):
    f = open(setup_file, "r")
    params = f.readlines()
    f.close()
    param_list = map(float, params[0].strip().split())
    smin = param_list[0]
    smax = param_list[1]
    points = int(param_list[2])
    spacing = (smax - smin)/(points - 1.0)
    strain_list = np.zeros(points)
    for i in range(1,points+1):
        strain_list[i - 1] = smin + (i - 1)*spacing
    return strain_list


def create_deformation_gradient(strain_mat):
    eigenval, eigenmat = np.linalg.eigh(2*strain_mat + np.eye(3))
    diag_mat = np.zeros((3,3))
    for i in range(3):
        diag_mat[i, i] = np.sqrt(eigenval[i])
    eigeninv = np.linalg.inv(eigenmat)
    F = np.matmul(eigenmat, np.matmul(diag_mat, eigeninv))
    return F


def create_strain_dir(dirname, defmat):
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    
    copy2("INCAR", dirname)
    copy2("POTCAR", dirname)
    copy2("KPOINTS", dirname)
    
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

def setup_tetra_run(dirname):
    if not os.path.exists(dirname + "/tetra"):
        os.makedirs(dirname + "/tetra")

    copy2("tetra/INCAR", dirname + "/tetra")
    copy2("tetra/KPOINTS", dirname + "/tetra")
    copy2("tetra/POTCAR", dirname + "/tetra")
    copy2(dirname + "/CONTCAR", dirname + "/tetra/POSCAR")
