import numpy as np
'''
Work with ndarray objects
'''

# 1.1
def RowNonzero(a, row):
    """
    Return number of rows that do not contain zero elements
    Parameters:
        a: array
            Input array (rectangular)
        row: int
            Number of rows of array
    """
    count = 0
    for i in range(row):
        zero = False
        for elem in a[i]:
            if elem == 0:
                zero = True
                break
        if not zero: count += 1
    return count

# 1.2
def MaxNumber(a):
    """
    Return maximum of numbers occurring more than once
    Parameters:
        a: array
            Input array (rectangular)
    """
    a = a.flatten()
    a = list(a)
    b = []
    for elem in a:
        if a.count(elem) >= 2:
            b.append(elem)
    if b == []:
        return 'all elements of array occur only once'
    elem_max = b[0]
    for elem in b:
        if elem > elem_max:
            elem_max = elem
    return elem_max


# 2.1
def ColNonzero(a, row, col):
    """
    Return number of columns that do not contain zero elements
    Parameters:
        a: array
            Input array (rectangular)
        row: int
            Number of rows of array
        col: int
            Number of columns of array
    """
    count = 0
    for j in range(col):
        zero = False
        for i in range(row):
            if a[i][j] == 0:
                zero = True
                break
        if not zero:
            count += 1
    return count

# 2.2 fix!
def CharactRow(a, row, col):
    """
    Return matrix with rows arranged in ascending order of characteristics
    Parameters:
        a: array
            Input array (rectangular)
        row: int
            Number of rows of array
        col: int
            Number of columns of array
    """
    char = []
    for i in range(row):
        char.append(0)
        for elem in a[i]:
            if (elem > 0) and (elem%2 == 0):
                char[i] += elem
    for j in range(row):
        char_min = min(char[j:])
        ind = char.index(char_min)
        a = np.insert(a, j, a[ind], axis=0)
        char.insert(j, char_min)
        del(char[ind+1])
        a = np.delete(a, ind+1, axis=0)
    return a

# 3.1
def ColZero(a, row, col):
    """
    Return number of columns that contain zero elements
    Parameters:
        a: array
            Array
        row: int
            Number of rows of array
        col: int
            Number of columns of array
    """
    count = 0
    for j in range(col):
        for i in range(row):
            if a[i][j] == 0:
                count += 1
                break
    return count

# 3.2
def SeriesIdentical(a, row, col):
    """
    Return number of row with longest series of identical elements
    Parameters:
        a: array
            Input array
        row: int
            Number of rows of array
        col: int
            Number of columns of array
    Out: list
        List of numbers of rows with longest series of identical elements
    """
    series = []
    for i in range(row):
        count = 1
        count_max = 1
        for j in range(col-1):
            if a[i][j] == a[i][j+1]:
                count += 1
            if count > count_max:
                count_max = count
            else: count = 1
        series.append(count_max)
    series_max = max(series)
    if series_max == 1:
        return 'all elements in rows of array occur only once'
    ind = []
    for j in range(row):
        if series[j] == series_max:
            ind.append(j+1)
    return ind

# 4.1
def PositiveProduct(a, n):
    '''
    Return product of elements of rows without negative elements
    Parameters:
        a: array
            Input square matrix
        n: int
            Size of each axis
    '''
    prod = []
    for i in range(n):
        p = 1
        negative = False
        for elem in a[i]:
            if elem < 0:
                negative = True
                break
        if not negative:
            for elem in a[i]:
                p *= elem
            prod.append(p)
    if prod == []:
        return 'all rows contain negative elements'
    return prod

# 4.2
def DiagonalSum(a, n):
    '''
    Return maximal sum of elements on diagonals parallel to main diagonal
    Parameters:
        a: array
            Input square matrix
        n: int
            Size of each axis
    '''
    sums = []
    for k in range(1, n):
        s_below = 0
        s_above = 0
        i = k
        while i < n:
            j = i -k
            s_below += a[i][j]
            s_above += a[j][i]
            i += 1
        sums.append(s_below)
        sums.append(s_above)
    s = max(sums)
    return s

# 5.1
def ColNonnegSum(a, n):
    '''
    Return sum of elements of columns without negative elements
    Parameters:
        a: array
            Input square matrix
        n: int
            Size of each axis
    '''
    sums = []
    for j in range(n):
        s = 0
        neg = False
        for i in range(n):
            if a[i][j] < 0:
                neg = True
                break
            else:
                s += a[i][j]
        if not neg:
            sums.append(s)
    return sums

# 5.2
def MinCDiagSum(a, n):
    '''
    Return minimal of sums of absolute values of elements
    in diagonals parallel to counter-diagonal
    Parameters:
        a: array
            Input square matrix
        n: int
            Size of each axis
    '''
    sums = []
    for k in range(n-1):
        s = 0
        for i in range(k+1):
            j = abs(i - k)
            if (i == n-1) and (j == 0):
                break
            s += abs(a[i][j])
        sums.append(s)
    for k in range(1, n):
        s = 0
        for i in range(k, n):
            j = n - 1 + k - i  # weird
            s += abs(a[i][j])
        sums.append(s)
    s = min(sums)
    return s

# 6.1
def RowEqualsCol(a, n):
    '''
    Return numbers of rows which are equal to
    columns with same indices
    Parameters:
        a: array
            Input square matrix
        n: int
            Size of each axis
    '''
    nums = []
    for i in range(n):
        equal = True
        for j in range(n):
            if a[i][j] != a[j][i]:
                equal = False
                break
        if equal: nums.append(i+1)
    if nums == []:
        return 'there are no rows equal to columns with same indices'
    return(nums)

# 6.2
def RowZeroSum(a, n):
    '''
    Return sum of elemets of rows that contain zero
    Parameters:
        a: array
            Input square matrix
        n: int
            Size of each axis
    '''
    sums = []
    for i in range(n):
        s = 0
        for elem in a[i]:
            if 0 in a[i]:
                s += elem
        if s > 0: sums.append(s)
    if sums == []:
        return 'there are no rows with zeros'
    return sums

# 7.1 copy of 5.1

# 7.2 copy of 5.2

# 8.1 fix!
def CharactCol(a, row, col):
    '''
    Return array with columns arranged in ascending order of characteristics
    Parameters:
    a: array
        Input array
    row: int
        Number of rows of array
    col: int
        Number of columns of array
    '''
    char = []
    for j in range(col):
        char.append(0)
        for i in range(row):
            if (a[i][j] < 0) and (a[i][j]%2 != 0):
                char[j] += abs(a[i][j])
    a = a.T
    for j in range(col):
        char_min = min(char[j:])
        ind = char.index(char_min)
        a = np.insert(a, j, a[ind], 0)
        char.insert(j, char_min)
        del(char[ind+1])
        a = np.delete(a, ind+1, 0)
    a = a.T
    return a

# 8.2
def ColNegSum(a, row, col):
    '''
    Return sums of elements in columns that contain negative element
    Parameters:
    a: array
        Input array
    row: int
        Number of rows of array
    col: int
        Number of columns of array
    '''
    sums = []
    for j in range(col):
        s = 0
        neg = False
        for i in range(row):
            s += a[i][j]
            if a[i][j] < 0:
                neg = True
        if neg:
            sums.append(s)
    if sums == []:
        return 'there are no columns with negative elements'
    return sums

# 9.1 copy 5.1

# 9.2 copy 5.2

# 10.1
def Gauss(a, row, col):
    '''
    Return triangular matrix (Gaussian elimination)
    Parameters:
    a: array
        Input array
    row: int
        Number of rows of array
    col: int
        Number of columns of array
    '''
    for i in range(row):
        for j in range(i+1, row):
            multiplier = a[j][i] / a[i][i]
            for s in range(i, col):
                a[j][s] = a[j][s] - a[i][s] * multiplier
    return a
    
# 10.2
def ArithmeticMean(a, row, col, eps):
    '''
    Return number of rows whose arithmetic mean is less than given value
    Parameters:
    a: array
        Input array
    row: int
        Number of rows of array
    col: int
        Number of columns of array
    eps: int/float
        Value to compare
    '''
    count = 0
    for i in range(row):
        total = 0
        avg = 0
        for item in a[i]:
            total += item
        avg = total/col
        if avg < eps:
            count += 1
    return count

if __name__ == "__main__":
    print("!")


