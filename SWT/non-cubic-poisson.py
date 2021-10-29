import numpy as np
import sys

eta = float(sys.argv[1])
undeformed_filename = sys.argv[2]
f = open(undeformed_filename, "r")
og_data = f.readlines()
f.close()

lv1 = map(float, og_data[2].strip().split())
lv2 = map(float, og_data[3].strip().split())
lv3 = map(float, og_data[4].strip().split())

f = open("CONTCAR", "r")
new_data = f.readlines()
f.close()

nlv1 = map(float, new_data[2].strip().split())
nlv2 = map(float, new_data[3].strip().split())
nlv3 = map(float, new_data[4].strip().split())

coeff = np.array([[lv1[0], lv1[1], 0, 0], [0, 0, lv1[0], lv1[1]], [lv2[0], lv2[1], 0, 0], [0, 0, lv2[0], lv2[1]]])
xvec = np.array([nlv1[0], nlv1[1], nlv2[0], nlv2[1]])
F12 = np.matmul(np.linalg.inv(coeff), xvec)
#F22 = (1.0/lv2[1])*(nlv2[1] - F12[1]*lv2[0])
F33 = np.sqrt(1 + 2*eta)


f = open("F.dat", "w")
f.write(str(F12[0]) + "    " + str(F12[1]) + "    " + str(0) + "\n")
f.write(str(F12[2]) + "    " + str(F12[3]) + "         " + str(0) +"\n")
f.write(str(0) + "             " + str(0) + "           " + str(F33) + "\n")
f.close()
F = np.array([[F12[0], F12[1], 0],[F12[2], F12[3], 0],[0, 0, F33]])

print "Verification"
print "New LVs should be:\n"
print np.matmul(F, np.array(lv1))
print np.matmul(F, np.array(lv2))
print np.array(lv3)

f = open("OUTCAR", "r")
outdata = f.readlines()
f.close()

for line in outdata:
    if "in kB" in line:
        tmp = line.strip().split()
        cstress = -float(tmp[-4])

cauchy_stress = np.array([[0, 0, 0],[0, 0, 0],[0, 0, cstress]])
invF = np.linalg.inv(F)
invFt = np.transpose(invF)

pk_stress =  np.linalg.det(F)*np.matmul(invF, np.matmul(cauchy_stress, invFt))

f = open("stress.dat", "w")
f.write(str(0) + "    " + str(0) + "     " + str(pk_stress[2,2]) + "     "
        + str(0) + "     " + str(0) + "      " + str(0) + "\n")
f.close()

