def display_matrix(lst):
    for i in lst:
        for j in i:
            print(round(j, 2), end = "\t")
        print()

def multiply(n, a, b):
    mul = []

    for i in range(n):
        row = []
        for j in range(n):
            sum = 0
            for k in range(n):
                sum += a[i][k] * b[k][j]
            row.append(sum)
        mul.append(row)

    return mul

def identity(n):
    lst = list()

    for i in range(n):
        row = []
        for j in range(n):
            row.append(1 if i == j else 0)
        lst.append(row)    

    return lst

def permutation(n, row1, row2):
    lst = identity(n)

    lst[row1], lst[row2] = lst[row2], lst[row1]

    return lst

def row_swap(n, A, row1, row2):
    lst = permutation(n, row1, row2)

    return multiply(n, lst, A)

def col_swap(n, A, col1, col2):
    lst = permutation(n, col1, col2)

    return multiply(n, A, lst)

def max_pivot(n, ind, A, b):
    max = ind

    for i in range(ind+1, n):
        if abs(A[i][ind]) > abs(A[max][ind]):
            max = i

    if max != ind:
        lst = row_swap(n, A, ind, max)
        b[max], b[ind] = b[ind], b[max]
        return lst, b

    return A, b

def row_reduction(n, A, b, col, row, fact):
    iden = identity(n)
    iden[col][row] = fact

    lst = multiply(n, iden, A)

    answer_set = b[:]
    answer_set[col] += fact*answer_set[row]

    return lst, answer_set

def back_substitution(n, A, b):
    solution_set = []

    for i in range(n-1, -1, -1):
        diff = 0
        for j in range(n-1, i, -1):
            if solution_set != []:
                diff += A[i][j]*solution_set[n-1-j]

        ans = b[i]
        res = ans - diff

        solution = res/A[i][i]
        solution_set.append(solution)

    return solution_set[::-1]

A = [
    [1, -2, 5, 2, -1, 1, 4, -3, 1, 5, 5, 2, -1, -2, 2, 2, -3, 0, -1, -4],
    [2, 0, -4, -1, -5, 4, 0, 3, -5, 5, 5, 4, -3, 1, -2, 3, -3, -1, -3, 1],
    [-1, 3, 1, -4, -2, 3, -4, 4, 3, 4, -1, -4, -2, 1, 2, -3, -5, -2, -4, 2],
    [-2, -4, 0, 0, 4, -2, 0, -4, 4, -4, 4, -2, 2, 1, 3, 2, -1, -4, -1, 2],
    [4, 3, 3, -5, 3, 1, 3, 2, -5, 2, 2, 5, -3, -5, 2, -3, -3, -5, 5, -1],
    [4, 1, 4, 3, 1, 3, 2, -4, -5, 1, 1, 2, -1, -3, 2, 0, 5, -3, -5, -3],
    [-1, -3, -5, -1, 4, 1, 1, 5, 3, 4, 4, -3, 1, -5, -2, -2, -1, 1, 1, 5],
    [-2, 1, 5, -3, 0, -4, 4, 3, -1, 0, -2, 5, 4, 1, 3, 1, -5, -5, 3, 5],
    [3, -2, 3, -3, 1, 0, 2, 5, 3, -1, -5, -3, 4, 2, 5, 0, 2, 3, -2, -5],
    [-5, 4, -2, 1, -4, -3, -5, -1, -5, 2, -5, 5, -5, -4, -4, 0, 1, -1, -5, -5],
    [-3, -4, -1, 4, 0, 1, -2, 1, 5, 2, 5, -5, 0, 2, -1, -2, -4, 0, 0, 5],
    [-5, 3, 5, 0, -3, -2, 5, -2, -3, 4, -3, -3, -2, 1, -2, 3, -5, 2, 1, -4],
    [2, -5, 5, 3, 3, -4, 1, 4, -3, 1, 4, 3, -2, -5, -4, -5, -1, -1, 5, 1],
    [3, 3, -3, -3, -3, -2, 2, 0, 2, -5, 2, -2, 5, -5, 2, -2, 0, 2, -2, -3],
    [3, -3, 3, -4, -4, -4, 0, -3, 3, -2, -5, -2, -5, -1, -2, 2, 2, 1, -3, -5],
    [-5, 5, -3, 0, 1, 0, 0, 0, -3, 0, 2, 5, 5, -4, -1, -5, -5, -1, -3, -2],
    [-3, -5, -5, -1, 0, -3, 3, -1, 2, -5, -1, -3, -5, -2, -1, 1, -5, -3, -4, 3],
    [4, 0, 4, -3, 2, 2, -4, 0, 1, -4, 5, 4, -4, 4, -5, 2, -5, 3, 5, 0],
    [1, 4, 1, 4, -3, -4, 3, 2, 4, 1, 3, -2, -2, -5, 2, -3, 1, -4, -4, 1],
    [0, -3, 3, 4, 0, 4, 4, 0, -5, -2, 4, 0, 0, 5, -1, -5, 2, -1, -1, 1]
]

b = [
    -11,
    187,
    87,
    -105,
    -78,
    -53,
    -11,
    27,
    -53,
    90, 
    34,
    74,
    -44,
    -156,
    10,
    -39,
    34,
    126,
    -105,
    -5
]


lst = [row[:] for row in A]
ans = b[:]
for i in range(len(A)):
    lst, ans = max_pivot(len(lst), i, lst, ans)
    pivot = lst[i][i]
    for j in range(i+1, len(lst)):
        ele = lst[j][i]
        if ele != 0:
            factor = -1*(ele/pivot)
            lst, ans = row_reduction(len(lst), lst, ans, j, i, factor)

res = back_substitution(len(lst), lst, ans)

for i in res:
    print(round(i, 2), end = "\t")