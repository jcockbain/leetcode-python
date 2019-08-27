def sortedSquares(A):
    squares = map(lambda x: x**2, A)
    return (sorted(squares))


def sortedSquares2(A):
    return sorted(x*x for x in A)
