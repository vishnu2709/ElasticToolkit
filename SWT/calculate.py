import numpy as np
import sys
from wallace import calculateWallaceTensor, checkStability

sfile = sys.argv[1]
cfile = sys.argv[2]
is_tetra = sys.argv[3]

Cij = np.zeros([6, 6])
f = open(sfile, "r")
lines = f.readlines()
stress = map(float, lines[0].strip().split())
f.close()

g = open(cfile, "r")
lines = g.readlines()
for i in range(len(lines)):
    data = lines[i].strip().split()
    for j in range(0, 6):
        Cij[i, j] = float(data[j])

w = calculateWallaceTensor(stress, Cij)
isStable, eigenvals, vecs = checkStability(w)
eigenvecs = np.transpose(vecs)
print "Symmetric Wallace Tensor\n"
print w,'\n'
print "Raw Data:\n"
print "Eigenvalues:\n"
print eigenvals,'\n'
print "Eigenvectors (in same order as eigenvalues):\n"
print eigenvecs,'\n'
print "The system is stable?", isStable
if (int(is_tetra) == 1):
    s1_index = []
    print "\n","--------------------------------------------------------------","\n"
    print "System is tetragonal, further analysis can be done\n"
    for i in range(len(eigenvecs)):
        temp = eigenvecs[i]
        if(temp[0] == 0 and temp[1] == 0 and temp[2] == 0 \
                and temp[3] == 0 and temp[4] == 0 and temp[5] == 1):
            s3_index = i
        elif(np.abs(temp[2]) < 1e-5 and temp[3] == 0 and temp[4] == 0 and temp[5] == 0):
            s2_index = i
        elif(temp[2] != 0 and eigenvals[i] == max(eigenvals)):
            c2_index = i
        elif(temp[2] != 0 and eigenvals[i] != max(eigenvals)):
            c1_index = i
        else:
            s1_index.append(i)
    print "Eigenvalues are printed in below line as : S3 S1 S1 S2 C1 C2\n"
    print eigenvals[s3_index], eigenvals[s1_index[0]], eigenvals[s1_index[1]], \
            eigenvals[s2_index], eigenvals[c1_index], eigenvals[c2_index], "\n"
    print "The eigenvectors are printed in the same order\n"
    print "S3: ",eigenvecs[s3_index],"\n"
    print "S1: ",eigenvecs[s1_index[0]], "\n"
    print "S1: ",eigenvecs[s1_index[1]], "\n"
    print "S2: ",eigenvecs[s2_index], "\n"
    print "C1: ",eigenvecs[c1_index], "\n"
    print "C2: ",eigenvecs[c2_index], "\n"
