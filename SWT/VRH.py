# Symmetrize cubic Cij; convert kBar to GPa
import numpy as np
import sys


Cij=np.loadtxt(sys.stdin)/10
Sij=np.linalg.inv(Cij)
Cdiag=np.diagonal(Cij)
C11=sum(Cdiag[0:3])/3
Sdiag=np.diagonal(Sij)
S11=sum(Sdiag[0:3])/3
C12=(Cij[0,1]+Cij[0,2]+Cij[1,2]+Cij[1,0]+Cij[2,0]+Cij[2,1])/6
S12=(Sij[0,1]+Sij[0,2]+Sij[1,2]+Sij[1,0]+Sij[2,0]+Sij[2,1])/6
C44=sum(Cdiag[3:6])/3
S44=sum(Sdiag[3:6])/3
mu=(C11-C12)/2
CP=C12-C44
BV=(C11+2*C12)/3
BR=1/(3*S11+6*S12)
KH=(BV+BR)/2
GV=(C11-C12+3*C44)/5
GR=5/(4*S11-4*S12+3*S44)
GH=(GV+GR)/2
PR=(3*KH-2*GH)/(6*KH+2*GH)
AZ=C44/mu
E=3*KH*(1-2*PR)
#print(C11,C12,C44,mu)
#print(KH/GH,PR,CP,AZ)

print "C11=%1f C12=%1f C44=%1f" %(C11,C12,C44)
print "(C11-C12)/2=%1f C12-C44=%1f K=%1f G=%1f E=%1f" %(mu,CP,KH,GH,E)
print "K/G=%2f PR=%3f AZ=%3f" %(KH/GH,PR,AZ)

#print(Sij)
