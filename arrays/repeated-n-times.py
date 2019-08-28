import unittest


class unittest(inittest.TestCase):
    def testAlgorithm(self):


if __name__ == "__main__":
    unittest.main()


def repeatedNTimes(self, A):
    """
    :type A: List[int]
    :rtype: int
    """
    reqNum = len(A) / 2
    hMap = {}
    for i in A:
        if i in hMap:
            hMap[i] += 1
        else:
            hMap[i] = 1
    for j in hMap:
        if hMap[j] == reqNum:
            return j
    return 0


class unittest(inittest.TestCase):
    def testAlgorithm(self):


if __name__ == "__main__":
    unittest.main()
