def display_matrix(lst):
    for i in lst:
        for j in i:
            print(round(j, 2), end = "\t")
        print()

def boundary_check(a, b):
    check = True

    for i in a:
        if len(i) != len(a):
            check = False
            break

    if len(b) != len(a):
        check = False

    return check

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

def rank_check(lst, ans):
    a, ab = 0, 0

    for i in lst:
        for j in i:
            if j != 0:
                a += 1
                break

    for i in ans:
        if i == 0:
            continue
        ab += 1

    if a > ab:
        ab = a

    return a, ab

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
    [1, 1],
    [2, 3]
]

b = [
    1,
    2,
]

print("\n========= GAUSSIAN ELIMINATION SOLVER =========\n")

assert boundary_check(A, b), "INVALID INPUT"

print("Number of variables:", len(A[0]))
print("\n==================== PIVOT ====================\n")

lst = [row[:] for row in A]
ans = b[:]
for i in range(len(A)):
    lst, ans = max_pivot(len(lst), i, lst, ans)
    pivot = lst[i][i]
    print("Pivot", i+1, ":", pivot)
    for j in range(i+1, len(lst)):
        ele = lst[j][i]
        if ele != 0:
            factor = -1*(ele/pivot)
            lst, ans = row_reduction(len(lst), lst, ans, j, i, factor)

a, ab = rank_check(lst, ans)

print("\n==================== RESULT ===================\n")

if a == ab and len(lst) == a:
    print("Given system has unique solutions")
    res = back_substitution(len(lst), lst, ans)
    print("\n===============================================\n")
    for i in range(len(res)):
        print(f"x{i+1} =", round(res[i], 2))
elif a == ab and len(lst) > a:
    print("Given system has infinite solutions")
elif a < ab:
    print("Given system has no solutions")

print("\n===============================================\n")