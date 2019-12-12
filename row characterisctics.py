import numpy as np
from copy import deepcopy

def CalcCharact(a, row, col):
    char = []
    for i in range(row):
        char.append(0)
        for elem in a[i]:
            if (elem > 0) and (elem%2 == 0):
                char[i] += elem
    return char

def SwapRow1(a, row, col):
    """
    Return matrix with rows arranged in ascending order of characteristics
    Parameters:
        a: array_like
            Input array (rectangular)
        row: int
            Number of rows of array
        col: int
            Number of columns of array
    """
    char = CalcCharact(a, row, col)
    for j in range(row):
        #print('pass', j)
        #print(char)
        char_min = min(char[j:])
        #print('char min', char_min)
        ind = char[j:].index(char_min) + j
        #print('ind', ind)

        tmp1 = deepcopy(a[j])
        a[j] = a[ind]
        a[ind] = tmp1
                
        tmp2 = char[j]
        char[j] = char[ind]
        char[ind] = tmp2
        
        #print('tmp1', tmp1)
        #print('tmp2', tmp2)        
        #print('a j', a[j])        
        #print('char j', char[j])        
        #print('a ind', a[ind])
        #print('char ind', char[ind])
        #print(a)
        #print()
    return a

def SwapRow2(a, row, col):
    """
    Return matrix with rows arranged in ascending order of characteristics
    Uses deepcopy
    Parameters:
        a: array_like
            Input array (rectangular)
        row: int
            Number of rows of array
        col: int
            Number of columns of array
    """
    char = CalcCharact(a, row, col)
    for j in range(row):
        #print('pass', j)
        #print(char)
        char_min = min(char[j:])
        #print('char min', char_min)
        ind = char[j:].index(char_min) + j
        #print('ind', ind)
        tmp1 = deepcopy(a[j])
        #print('tmp1', tmp1)
        tmp2 = deepcopy(char[j])
        #print('tmp2', tmp2)
        a[j] = deepcopy(a[ind])
        #print('a j', a[j])
        char[j] = deepcopy(char[ind])
        #print('char j', char[j])
        a[ind] = deepcopy(tmp1)
        #print('a ind', a[ind])
        char[ind] = deepcopy(tmp2)
        #print('char ind', char[ind])
        #print(a)
        #print()
    return a


a1 = np.array([[2, 7, 1, 0], [-5, 1, 3, 1], [1, 0, 5, 3]])
a2 = np.array([[2, 7, 1, 0], [-5, 1, 3, 1], [1, 0, 5, 3]])
row = a1.shape[0]
col = a1.shape[1]
print('source\n', a1)
print('without deepcopy\n', SwapRow1(a1, row, col))
print('with deepcopy\n', SwapRow2(a2, row, col))
