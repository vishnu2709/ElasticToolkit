import numpy as np
import sys

posfile = sys.argv[1]

f = open(posfile, "r")
data = f.readlines()
f.close()

lv1 = np.array(map(float, data[2].strip().split()))
lv2 = np.array(map(float, data[3].strip().split()))

dp = np.dot(lv1, lv2)
lv1m = np.linalg.norm(lv1)
lv2m = np.linalg.norm(lv2)

angle = (180.0/np.pi)*np.arccos(dp/(lv1m*lv2m))
print angle
f = open("gamma.dat", "w")
f.write(str(angle) + "\n")
f.close()
