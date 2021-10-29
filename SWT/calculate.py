import numpy as np
import sys
from wallace import calculateWallaceTensor, checkStability

sfile = sys.argv[1]
cfile = sys.argv[2]

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
print w
isStable, eigenvals, vecs = checkStability(w)
eigenvecs = np.transpose(vecs)
print isStable, eigenvals, eigenvecs
