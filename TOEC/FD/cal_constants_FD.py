import numpy as np
import sys

eta = float(sys.argv[1])
volume = float(sys.argv[2])
energies = []

for i in range(1,35):
    dirname = "straintype-"+str(i)+"-"+str(eta)
    f = open(dirname + "/output", "r")
    data = f.readlines()
    f.close()

    for line in data:
        if "E0=" in line:
            tmp = line.strip().split(); e = tmp[-4]

    energies.append(float(e))

# C111 = (0.5/(V*eta^3))*(E(2*eta) - 2*E(eta) + 2*E(-eta) - E(-2*eta))

ediff = energies[6] - 2*energies[7] + 2*energies[8] - energies[9]
C111 = 1602.1766*(0.5/(volume*eta**3))*ediff

# C112 = (0.5/(V*eta^3))*(E(eta,eta) - E(-eta,-eta) - 2*E(0,eta) + 2*E(0,-eta))

ediff = energies[0] - energies[1] - 2*energies[2] + 2*energies[3] + energies[4] - energies[5]
C112 = 1602.1766*(0.5/(volume*eta**3))*ediff

# C113
ediff = energies[10] - energies[11] - energies[12] + energies[13] - energies[14] + \
        energies[15] + energies[16] - energies[17]
C123 = 1602.1766*(1.0/8.0)*(1.0/volume)*(1.0/eta**3)*ediff

# C144
ediff = energies[18] - 2*energies[7] + energies[19] - energies[20] + 2*energies[8]  \
        - energies[21]
C144 = 1602.1766*(1.0/8.0)*(1.0/(volume*eta**3))*ediff

# C166
ediff = energies[22] - 2*energies[7] + energies[23] - energies[24] + 2*energies[8]  \
        - energies[25]
C166 = 1602.1766*(1.0/8.0)*(1.0/(volume*eta**3))*ediff

# C456
ediff = energies[26] - energies[27] - energies[28] + energies[29] - energies[30] + \
        energies[31] + energies[32] - energies[33]
C456 = 1602.1766*(1.0/64.0)*(1.0/(volume*eta**3))*ediff

print C111, C112, C123, C144, C166, C456
