import sys
import numpy as np

paramfile = sys.argv[1]
strain_z = float(sys.argv[2])
g = open(paramfile, "r")
data = g.readlines()
g.close()

second_order = map(float, data[0].strip().split())
third_order = map(float, data[1].strip().split())

C11 = second_order[0]
C12 = second_order[1]
C44 = second_order[2]
C111 = third_order[0]
C112 = third_order[1]
C123 = third_order[2]
C144 = third_order[3]
C166 = third_order[4]

a = C111 + 3*C112
b = 2*(C11 + C12 + C112*strain_z + C123*strain_z)
c = 2*C12*strain_z + C112*strain_z**2

root1 = (0.5/a)*(-b + np.sqrt(b**2 - 4*a*c))
root2 = (0.5/a)*(-b - np.sqrt(b**2 - 4*a*c))
print root1, root2
strain_xy = min(root1, root2)

pk_stress = (2*C12 + 2*C112*strain_z)*strain_xy + C11*strain_z + \
        (C112 + C123*strain_z)*strain_xy**2 + 0.5*C111*strain_z**2

stress = pk_stress #(np.sqrt(2.0*strain_z + 1.0)/(1.0 + 2*strain_xy))*pk_stress

f = open("strains.dat", "w")
f.write(str(strain_z) + "    " + str(strain_xy))
f.close()

f = open("stress.dat", "w")
f.write(str(0) + "     " + str(0) + "     " + str(stress) + "    " 
        + str(0) + "    " + str(0) + "     " + str(0))
f.close()
