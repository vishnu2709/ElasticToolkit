import numpy as np
from voight import convertFromVoight, convertToVoight, KDelta

def calculateWallaceTensor(sigma, Cij):
    wallace = np.zeros([6, 6])
    for kl in range(1, 7):
        for mn in range(1, 7):
            k, l = convertFromVoight(kl)
            m, n = convertFromVoight(mn)
            km = convertToVoight(k, m)
            ln = convertToVoight(l, n)
            kn = convertToVoight(k, n)
            lm = convertToVoight(l, m)
            wallace[kl - 1, mn - 1] = Cij[kl - 1, mn - 1] + 0.5*(sigma[km - 1]*KDelta(l, n) + 
                    sigma[kn - 1]*KDelta(l, m) + sigma[lm - 1]*KDelta(k, n) + 
                    sigma[ln - 1]*KDelta(k, m) - sigma[kl - 1]*KDelta(m, n) -
                    sigma[mn - 1]*KDelta(k, l))
    return wallace

def checkStability(wallace):
    eigenvals, eigenvec = np.linalg.eigh(wallace)
    stable_factor = 0
    isStable = True
    for i in eigenvals:
        if (i < 0):
            stable_factor = stable_factor + 1
            isStable = False
    return isStable, eigenvals, eigenvec
