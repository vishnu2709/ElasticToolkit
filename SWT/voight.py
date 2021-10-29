# Voight notation key
# 1 -> 11, 2 -> 22, 3 -> 33, 4 -> 23, 5 -> 13, 6 -> 12

def KDelta(i, j):
    if (i == j):
        return 1
    else:
        return 0

def convertFromVoight(voight_in):
    if (voight_in == 1):
        i = 1; j = 1
        return i, j
    elif (voight_in == 2):
        i = 2; j = 2
        return i, j
    elif (voight_in == 3):
        i = 3; j = 3
        return i, j
    elif (voight_in == 4):
        i = 2; j = 3
        return i, j
    elif (voight_in == 5):
        i = 1; j = 3
        return i, j
    elif (voight_in == 6):
        i = 1; j = 2
        return i, j
    else:
        raise Exception("Index must be >= 1 and <= 6")

def convertToVoight(i, j):
    if (min(i, j) == 1):
        if (max(i, j) == 1):
            return 1
        elif (max(i, j) == 2):
            return 6
        elif (max(i, j) == 3):
            return 5
        else:
            raise Exception("Index must be >= 1 and <= 3")
    elif (min(i, j) == 2):
        if (max(i, j) == 2):
            return 2
        elif (max(i, j) == 3):
            return 4
        else:
            raise Exception("Index must be >=2 and <=3")
    elif (min(i, j) == 3):
        if (max(i, j) == 3):
            return 3
        else:
            raise Exception("Index must be 3")
    else:
        raise Exception("Both the indices are above 3!")
