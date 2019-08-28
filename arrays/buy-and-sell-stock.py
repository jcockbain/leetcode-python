import unittest
import sys


def maxProfit(prices):
    max_profit = 0
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            profit = prices[j] - prices[i]
            max_profit = max(max_profit, profit)
    return max_profit


def maxProfit2(prices):
    min_price = sys.maxsize
    max_profit = 0
    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        elif (prices[i] - min_price > max_profit):
            max_profit = prices[i] - min_price
    return max_profit


class Test(unittest.TestCase):
    def testMaxProfit(self):
        self.assertEqual(maxProfit([7, 1, 5, 3, 6, 4]), 5)
        self.assertEqual(maxProfit2([7, 6, 4, 3, 1]), 0)


if __name__ == "__main__":
    unittest.main()
