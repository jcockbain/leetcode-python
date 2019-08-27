

def flipAndInvertImage(self, A):
    """
    :type A: List[List[int]]
    :rtype: List[List[int]]
    """
    result = []
    for image in A:
        B = image[::-1]
        for i in range(len(B)):
            if B[i] == 1:
                B[i] = 0
            elif B[i] == 0:
                B[i] = 1
        print(B)
        result.append(B)
    return result


def flipAndInvertImage2(A):
    result = []
    for row in A:
        result.append(list(map(lambda x: 0 if x == 1 else 1, row[::-1])))
    return result
