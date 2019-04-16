# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 16:06:01 2019

@author: Дмитрий
"""
import numpy as np

def row_chr(row):
    """
    Return matrix row chr - a sum of positives, that are not odd
    Parameters:
        matrix: array
            Input array (rectangular)
        row: int
            Row of matrix
    """
    return sum([x for x in row if (x > 0) and (x%2 == 0)])

def sort_by_row_chr(matrix):
    """
    Return matrix with rows arranged in ascending order of characteristics
    Parameters:
        matrix: array
            Input array (rectangular)
    """
    srt = sorted(matrix.tolist(), key=lambda row: row_chr(row))
    #srt = sorted(matrix.tolist(), key=row_chr)
    
    return np.ndarray(matrix.shape, dtype=int, buffer=np.array(srt))

def my_test():
    '''
    Test functions
    '''
    c = np.ndarray(shape=(3,3), dtype=int, \
                   buffer=np.array([[-2,8,4],[9,0,8],[9,7,0]]))
    
    print(row_chr(c[0,:]))
    print(sort_by_row_chr(c))    

if __name__ == "__main__":
    my_test()