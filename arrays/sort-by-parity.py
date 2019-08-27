def sortArrayByParity(A):
    odds = []
    evens = []
    for num in A:
        if num % 2 == 0 or num == 0:
            evens.append(num)
        else:
            odds.append(num)
    return evens + odds


def sortArrayByParity2(A):
    return ([x for x in A if x % 2 == 0] +
            [x for x in A if x % 2 == 1])
