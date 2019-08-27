def selfDividingNumbers(left, right):
    """
    :type left: int
    :type right: int
    :rtype: List[int]
    """
    selfDividers = []
    for i in range(left, right+1):
        for c in range(len(str(i))):
            if int(str(i)[c]) == 0:
                break
            if i % int(str(i)[c]) != 0:
                break
            if c == len(str(i)) - 1:
                selfDividers.append(i)
    return selfDividers
