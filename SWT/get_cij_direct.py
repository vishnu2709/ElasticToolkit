import sys
import numpy as np

filename = sys.argv[1]
strainfile = sys.argv[2]

f = open(filename, "r")
data = f.readlines()
f.close()

g = open(strainfile, "r")
strains = g.readlines()
g.close()

second_order = map(float, data[0].strip().split())
third_order = map(float, data[1].strip().split())
strain_list = map(float, strains[0].strip().split())
strain_z = strain_list[0]
strain_xy = strain_list[1]

C11 = second_order[0]
C12 = second_order[1]
C44 = second_order[2]
C111 = third_order[0]
C112 = third_order[1]
C123 = third_order[2]
C144 = third_order[3]
C166 = third_order[4]

C11p = C11 + (3*C11 + C12 + C111 + C112)*strain_xy + (-C11 + C12 + C112)*strain_z
C12p = C12 + (2*C12 + 2*C112)*strain_xy + (-C12 + C123)*strain_z
C13p = C12 + (C112 + C123)*strain_xy + (C12 + C112)*strain_z
C33p = C11 + (-2*C11 + 2*C12 + 2*C112)*strain_xy + (4*C11 + C111)*strain_z
C44p = C44 + 0.25*(C11 + 3*C12 + 4*C144 + 4*C166)*strain_xy + 0.25*(C11 + C12 + 4*C44 + 4*C166)*strain_z
C66p = C44 + 0.5*(C11 + C12 + 4*C44 + 4*C166)*strain_xy + 0.5*(C12 - 2*C44 + 2*C144)*strain_z

g = open("generated_Cij.dat", "w")
g.write("%4.4f  %4.4f %4.4f %4.7f %4.7f %4.7f\n" % (C11p, C12p, C13p, 0.0, 0.0, 0.0))
g.write("%4.4f  %4.4f %4.4f %4.7f %4.7f %4.7f\n" % (C12p, C11p, C13p, 0.0, 0.0, 0.0))
g.write("%4.4f  %4.4f %4.4f %4.7f %4.7f %4.7f\n" % (C13p, C13p, C33p, 0.0, 0.0, 0.0))
g.write("%4.7f  %4.7f %4.7f %4.4f %4.7f %4.7f\n" % (0.0, 0.0, 0.0, C44p, 0.0, 0.0))
g.write("%4.7f  %4.7f %4.7f %4.7f %4.4f %4.7f\n" % (0.0, 0.0, 0.0, 0.0, C44p, 0.0))
g.write("%4.7f  %4.7f %4.7f %4.7f %4.7f %4.4f\n" % (0.0, 0.0, 0.0, 0.0, 0.0, C66p))
g.close()
