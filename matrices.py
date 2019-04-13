'''Matrix operations, ex with lists '''

#import numpy as np

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
    count = 0
    for row in matrix:
        zero = False
        for elem in row:
            if elem == 0:
                zero = True
                break
        if not zero:
            count += 1
    return count

# 1.2
def max_number(matrix):
    """
    Return maximum of numbers occurring more than once
    Parameters:
        matrix: 2d-array
            Input array (rectangular)
    """
    v_dict = {}
    for row in matrix:
        for elem in row:
            try:
                v_dict[elem] = v_dict[elem] + 1
            except KeyError:
                v_dict[elem] = 1

    max_value = None
    max_value_count = 1
    for key in v_dict:
        if v_dict[key] > max_value_count:
            max_value = key
            max_value_count = v_dict[key]
    return max_value

# 2.1
def nonzero_col_count(matrix):
    """
    Return number of columns that do not contain zero elements
    Parameters:
        matrix: array
            Input array (rectangular)
    """
    count = 0
    row_count = len(matrix)
    col_count = len(matrix[0])
    for j in range(col_count):
        zero = False
        for i in range(row_count):
            if matrix[i][j] == 0:
                zero = True
                break
        if not zero:
            count += 1
    return count

# 2.2 fix!
def row_chr(matrix, row):
    """
    Return matrix row chr - a sum of positives, that are not odd
    Parameters:
        matrix: array
            Input array (rectangular)
        row: int
            Row of matrix
    """
    count = 0
    for elem in matrix[row]:
        if (elem > 0) and (elem%2 == 0):
            count += elem
    return count

def sort_by_row_chr(matrix):
    """
    Return matrix with rows arranged in ascending order of characteristics
    Parameters:
        matrix: array
            Input array (rectangular)
    """
    rows_dict = {}
    for i in range(len(matrix)):
        rows_dict[i] = row_chr(matrix, i)
    new_matrix = []
    for key in sorted(rows_dict.keys()):
        new_matrix.append(matrix[key])
    return new_matrix

# 3.1
def col_zero(matrix, row, col):
    """
    Return number of columns that contain zero elements
    Parameters:
        matrix: array
            Array
        row: int
            Number of rows of array
        col: int
            Number of columns of array
    """
    count = 0
    for j in range(col):
        for i in range(row):
            if matrix[i][j] == 0:
                count += 1
                break
    return count

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
    idx = 0
    max_length = series_max_len(matrix[0])

    for i in range(1, len(matrix)):
        current = series_max_len(matrix[i])
        if current > max_length:
            idx = i
            max_length = current
    return idx

# 4.1
def positive_row_product(matrix):
    '''
    Return product of elements of rows without negative elements
    Parameters:
        matrix: array
            Input square matrix
    '''
    size = len(matrix)
    total_prod = 1
    has_positive = False
    for i in range(size):
        prod = 1
        negative = False
        for elem in matrix[i]:
            if elem < 0:
                negative = True
                break
            prod *= elem
        if not negative:
            total_prod *= prod
            has_positive = True
    if has_positive:
        return total_prod
    return None

# 4.2
def sum_diag(matrix, diag):
    '''
    Return sum of k-th diagonal parallel to main
    Parameters:
        a: array
           Input square matrix
        diag: int
           Diagonal number (positive - below, negative - above)
    '''
    size = len(matrix)

    if diag > 0:
        i = diag
        j = 0
    else:
        i = 0
        j = -diag

    sum_diag_elem = 0
    while (i < size) and (j < size):
        sum_diag_elem += matrix[i][j]
        i += 1
        j += 1

    return sum_diag_elem

def diag_max_sum(matrix, do_sum_main):
    '''
    Return maximal sum of elements on diagonals parallel to main diagonal
    Parameters:
        matrix: array
            Input square matrix
        do_sum_main: bool
            Incule main diagonal
    '''
    size = len(matrix)
    sums = []

    for k in range(1, size):
        sums.append(sum_diag(matrix, k))
        sums.append(sum_diag(matrix, -k))

    if do_sum_main:
        sums.append(sum_diag(matrix, 0))

    return max(sums)

# 5.1
def col_nonneg_sum(matrix):
    '''
    Return sum of elements of columns without negative elements
    Parameters:
        a: array
            Input square matrix
    '''
    size = len(matrix)
    total = 0

    for j in range(size):
        sum_neg = 0
        neg = False
        for i in range(size):
            if matrix[i][j] < 0:
                neg = True
                break
            sum_neg += matrix[i][j]
        if not neg:
            total += sum_neg
    return total

# 5.2
def sum_cdiag(matrix, diag):
    '''
    Return sum of k-th diagonal parallel to counter-main
    Parameters:
        matrix: array
           Input square matrix
        diag: int
           Diagonal number (positive - below, negative - above)
    '''
    size = len(matrix)

    if diag > 0:
        i = size - 1
        j = diag
    else:
        i = size + diag
        j = 0

    sum_cdiag_elem = 0
    while (i >= 0) and (j < size):
        sum_cdiag_elem += matrix[i][j]
        i -= 1
        j += 1
    return sum_cdiag_elem

def cdiag_min_sum(matrix, do_sum_main):
    '''
    Return minimal of sums of absolute values of elements
    in diagonals parallel to counter-diagonal
    Parameters:
        matrix: array
            Input square matrix
        do_sum_main: bool
            Count main counter diago
    '''
    size = len(matrix)
    sums = []

    for k in range(1, size):
        sums.append(sum_cdiag(matrix, k))
        sums.append(sum_cdiag(matrix, -k))

    if do_sum_main:
        sums.append(sum_cdiag(matrix, 0))

    return min(sums)

# 6.1
def row_equals_col(matrix):
    '''
    Return numbers of rows which are equal to
    columns with same indices
    Parameters:
        matrix: array
            Input square matrix
    '''
    size = len(matrix)
    nums = []
    for i in range(size):
        equal = True
        for j in range(size):
            if matrix[i][j] != matrix[j][i]:
                equal = False
                break
        if equal:
            nums.append(i+1)
    return nums

# 6.2
def row_has_zero(row):
    '''
    Return true if row hs zero elements
    Parameters:
        matrix: array
            Input square matrix
        row: int
            Row number
    '''
    zero = False
    for j in range(row):
        if row[j] == 0:
            zero = True
            break
    return zero

def sum_zero_rows(matrix):
    '''
    Return sum of elemets of rows that contain zero
    Parameters:
        matrix: array
            Input square matrix
    '''
    sum_zero = 0
    exist = False

    for row in matrix:
        if row_has_zero(row):
            exist = True
            sum_zero += sum(row)

    if exist:
        return sum_zero
    return None

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

def col_chr(matrix, col):
    '''
    Calc column characteristic
    Parameters:
        matrix: array
            Input square matrix
        col: int
            Column number
    '''
    sum_chr = 0
    for row in matrix:
        if (row[col] < 0) and (row[col] % 2 != 0):
            sum_chr += abs(row[col])
    return sum_chr

def sort_by_col_chr(matrix):
    '''
    Return array with columns arranged in ascending order of characteristics
    Parameters:
    matrix: array
        Input array
    '''
    size = len(matrix[0])
    for i in range(0, size - 1):
        for j in range(i + 1, size):
            if col_chr(matrix, i) > col_chr(matrix, j):
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
    col_sum = []
    col_ex_neg = []

    rows = len(matrix)
    cols = len(matrix[0])

    for j in range(cols):
        col_sum.append(0)
        col_ex_neg.append(False)

    for i in range(rows):
        for j in range(cols):
            col_sum[j] += matrix[i][j]
            if matrix[i][j] < 0:
                col_ex_neg[j] = True

    sums = 0
    exists = False
    for j in range(cols):
        if col_ex_neg[j]:
            exists = True
            sums += col_sum[j]

    if exists:
        return sums

    return None

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
    count = 0
    for row in matrix:
        avg = 0
        for item in row:
            avg += item
        if avg/len(row) < mean:
            count += 1
    return count

def my_test():
    '''
    Test functions
    '''
    #a = [[1,4,3],[6,0,8],[9,7,0]]
    #print(nonzero_row_count(a))
    #b = np.ndarray((3,3), buffer=np.array(a), dtype=int)
    #print(nonzero_row_count(b))

    #c = [[1,1,3],[-2,3,8],[4,6,8]]
    #print(nonzero_col_count(c))
    #print(sort_by_row_chr(c))

    #d = [[2,3,3,3,5,6,1],[5,6,7,7,7,7,7],[9,9,9,9,0,0,0]]
    #print(row_max_series(d))

    #e = [[-1,1,2],[-2,3,8],[2,4,-8]]
    #print(positive_row_product(e))

    #f = [[-1,1,2],[-2,3,8],[2,4,-8]]
    #print(diag_max_sum(f, False))
    #print(col_nonneg_sum(f))
    #print(cdiag_min_sum(f, False))

    g = [[-9, -8, -1], [6, -3, 8], [-2, -6, -4]]
    #print(row_equals_col(g))
    #print(sum_zero_rows(g))
    #print(col_chr(g, 0))
    h = sort_by_col_chr(g)
    #print(sort_by_col_chr(g))
    print(sum_cols_neg(g))
    #print(row_less_mean(g, 0))
    print(id(g), id(h))

if __name__ == "__main__":
    my_test()
    