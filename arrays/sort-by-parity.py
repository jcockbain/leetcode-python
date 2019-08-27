def sortArrayByParity(A):
    odds = []
    evens = []
    for num in A:
        if num % 2 == 0 or num == 0:
            evens.append(num)
        else:
            odds.append(num)
    return evens + odds
