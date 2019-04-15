'''Matrix operations, ex with numpy '''
import numpy as np
import operator

# 1.1
def nonzero_row_count(matrix):
    """
    Return number of rows that do not contain zero elements
    Parameters:
        matrix: 2d-array
            Input array (rectangular)
        row: int
            Number of rows of array
    """
    return sum([1 for row in matrix if len(np.nonzero(row))])

# 1.2
def max_number(matrix):
    """
    Return maximum of numbers occurring more than once
    Parameters:
        matrix: 2d-array
            Input array (rectangular)
    """
    flt = matrix.flatten().tolist()

    v_dict = {i:flt.count(i) for i in flt}

    return max(v_dict.items(), key=operator.itemgetter(1))[0]

# 2.1
def nonzero_col_count(matrix):
    """
    Return number of columns that do not contain zero elements
    Parameters:
        matrix: array
            Input array (rectangular)
    """
    #columns = (matrix != 0).sum(0)
    #return sum([1 for i,x in enumerate(columns) if x == matrix.shape[1]])
    return sum([1 for row in matrix.T if row.prod()!=0])

# 2.2 fix!
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
    
    return np.ndarray(matrix.shape, dtype=int, buffer=np.array(srt))

# 3.1
def col_zero(matrix):
    """
    Return number of columns that contain zero elements
    Parameters:
        matrix: array
            Array
    """
    return sum([1 for row in matrix.T if row.prod()==0])

# 3.2
def series_max_len(row):
    """
    Return length of max series length
    Parameters:
        row: array
            Input row of matrix
    Out:
        list:
            List of numbers of rows with longest series of identical elements
    """
    count = 1
    max_length = 1
    for j in range(len(row)-1):
        if row[j] == row[j+1]:
            count += 1
            if count > max_length:
                max_length = count
        else:
            count = 1
    return max_length

def row_max_series(matrix):
    """
    Return number of row with longest series of identical elements
    Parameters:
        matrix: array
            Input array
    Out:
        list:
            List of numbers of rows with longest series of identical elements
    """
    ser_len = [series_max_len(row) for i,row in enumerate(matrix)]
    
    max_len = max(ser_len) 
    
    return [i for i,x in enumerate(ser_len) if x==max_len]

# 4.1
def positive_row_product(matrix):
    '''
    Return product of elements of rows without negative elements
    Parameters:
        matrix: array
            Input square matrix
    '''
    f = lambda row: sum([1 for i in row if i < 0])
    
    lst = [elem for row in matrix for elem in row if f(row)==0]
    
    return np.prod(np.array(lst))

# 4.2
def diag_max_sum(matrix):
    '''
    Return maximal sum of elements on diagonals parallel to main diagonal
    Parameters:
        matrix: array
            Input square matrix
        do_sum_main: bool
            Incule main diagonal
    '''
    size = matrix.shape[0]
    
    return max([sum(matrix.diagonal(k)) for k in range(-size+1, size)])

# 5.1
def col_nonneg_sum(matrix):
    '''
    Return sum of elements of columns without negative elements
    Parameters:
        a: array
            Input square matrix
    '''
    f = lambda row: sum([1 for i in row if i < 0])
    
    lst = [elem for row in matrix.T for elem in row if f(row)==0]
    
    return sum(np.array(lst))

# 5.2
def cdiag_min_sum(matrix):
    '''
    Return minimal of sums of absolute values of elements
    in diagonals parallel to counter-diagonal
    Parameters:
        matrix: array
            Input square matrix
    '''
    size = matrix.shape[0]
    
    return min([sum(matrix.T.diagonal(k)) for k in range(-size+1, size)])

# 6.1
def row_equals_col(matrix):
    '''
    Return numbers of rows which are equal to
    columns with same indices
    Parameters:
        matrix: array
            Input square matrix
    '''
    cmp = lambda row, col, size: all([row[k]==col[k] for k in range(size)])
    
    size = matrix.shape[0]
    
    return [k for k in range(size) \
            if cmp(matrix[k][:], matrix[:][k].T, size)]

# 6.2
def sum_zero_rows(matrix):
    '''
    Return sum of elemets of rows that contain zero
    Parameters:
        matrix: array
            Input square matrix
    '''
    f = lambda row: all([elem==0 for elem in row])
     
    return sum([sum(row) for row in matrix if f(row)])

# 7.1 copy of 5.1

# 7.2 copy of 5.2

# 8.1 fix!
def swp_cols(matrix, i, j):
    '''
    Swap i- nd j-th columns in matrix
    Parameters:
        matrix: array
            Input square matrix
    '''
    for row in matrix:
        tmp = row[i]
        row[i] = row[j]
        row[j] = tmp
    return matrix
    
def sort_by_col_chr(matrix):
    '''
    Return array with columns arranged in ascending order of characteristics
    Parameters:
    matrix: array
        Input array
    '''
    ch = lambda elem: (elem < 0) and (elem % 2 != 0)
    
    chrc = lambda col: sum([elem for elem in col if ch(col)])
    
    size = len(matrix[0])
    for i in range(0, size - 1):
        for j in range(i + 1, size):
            if chrc(matrix[:][i]) > chrc(matrix[:][j]):
                swp_cols(matrix, i, j)
    return matrix

# 8.2
def sum_cols_neg(matrix):
    '''
    Return sums of elements in columns that contain negative element
    Parameters:
    a: array
        Input array
    '''
    ch = lambda elem: (elem < 0)    
    
    chrc = lambda col: any([elem for elem in col if ch(col)])

    return sum([sum(col) for col in matrix.T if chrc(col)])

# 9.1 copy 5.1

# 9.2 copy 5.2

# 10.1
def gauss(matrix, row, col):
    '''
    Return triangular matrix (Gaussian elimination)
    Parameters:
    matrix: array
        Input array
    row: int
        Number of rows of array
    col: int
        Number of columns of array
    '''
    for i in range(row):
        for j in range(i+1, row):
            multiplier = matrix[j][i] / matrix[i][i]
            for k in range(i, col):
                matrix[j][k] = matrix[j][k] - matrix[i][k] * multiplier
    return matrix

# 10.2
def row_less_mean(matrix, mean):
    '''
    Return number of rows whose arithmetic mean is less than given value
    Parameters:
    matrix: array
        Input array
    mean: int/float
        Value to compare
    '''
    avg = lambda row: sum(row)/len(row) if len(row) > 0 else 0

    return sum([1 for row in matrix if avg(row) < mean])

def my_test():
    '''
    Test functions
    '''
    #print('Nonzero row test')
    #a = np.ndarray(shape=(2,2), dtype=int, \
    #               buffer=np.array([[1,4,3],[6,0,8],[9,7,0]]))
    #print(nonzero_row_count(a))
    
    #print('Max number test')
    #b = np.ndarray(shape=(3,3), dtype=int, \
    #               buffer=np.array([[1,8,8],[9,0,8],[9,7,0]]))
    #print(max_number(b))

    #print('Nonezero columns test')    
    #print(nonzero_col_count(b))

    #c = np.ndarray(shape=(3,3), dtype=int, \
    #               buffer=np.array([[-2,8,4],[9,0,8],[9,7,0]]))
    
    #print(row_chr(c[0,:]))
    #print(sort_by_row_chr(c))
    
    #print(col_zero(c))
    
    #print('Series max length test')        
    #d = [[2,3,3,3,5,6,1],[5,6,7,7,7,7,7],[9,9,9,9,0,0,0]]
    #print(row_max_series(d))
    
    #e = [[-1,1,2],[-2,3,8],[2,-4,8]]
    #print(positive_row_product(e))
    
    #f = np.ndarray(shape=(3,3), dtype=int, \
    #               buffer=np.array([[-1,1,2],[-2,3,8],[2,4,-8]]))    
    #print(diag_max_sum(f))    
    #print(col_nonneg_sum(f))    
    #print(cdiag_min_sum(f))
    
    g = np.ndarray(shape=(3,3), dtype=int, \
                   buffer=np.array([[-9, -8, -1], [6, -3, 8], [-2, -6, -4]]))    
    #print(row_equals_col(g))
    
    #print(sum_zero_rows(g))    
    #print(sort_by_col_chr(g))
    #print(sum_cols_neg(g))
    
    print(row_less_mean(g, 0))

if __name__ == "__main__":
    my_test()
    