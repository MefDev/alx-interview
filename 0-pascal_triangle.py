def pascal_triangle(numRows):
    outer_list = []
    for n in range(0, numRows):
        inside_list = []
        for k in range(0, n + 1):
            val = int(findComb(n, k))
            inside_list.append(val)
        outer_list.append(inside_list)
    return outer_list


def findFact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * findFact(n - 1)


def findComb(n, k):
    return findFact(n) / (findFact(k) * findFact(n - k))
