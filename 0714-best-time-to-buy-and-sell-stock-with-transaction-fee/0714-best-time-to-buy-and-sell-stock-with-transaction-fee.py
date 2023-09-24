# day[i]에 파는 경우, 사는 경우 두 케이스를 고려해야 함
from typing import *


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy, sell = [0] * len(prices), [0] * len(prices)

        for i, price in enumerate(prices):
            if i == 0:
                buy[i], sell[i] = -price, 0
            else:
                buy[i] = max(buy[i - 1], sell[i - 1] - price)
                sell[i] = max(sell[i - 1], buy[i - 1] + price - fee)

        return max(buy[-1], sell[-1])