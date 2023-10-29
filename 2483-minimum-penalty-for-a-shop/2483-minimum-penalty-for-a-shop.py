from collections import deque

"YYNY"
"2th에 닫는다고 가정하면"
"2th부터 Nth까지의 Y 갯수"
"0th부터 2-1th까지의 N 갯수"


class Solution:
    def bestClosingTime(self, customers: str) -> int:

        y_sum, n_sum = deque([]), []

        for char in customers:
            if char == "N":
                if not n_sum:
                    n_sum.append(1)
                else:
                    n_sum.append(n_sum[-1] + 1)
            else:
                if not n_sum:
                    n_sum.append(0)
                else:
                    n_sum.append(n_sum[-1])

        for char in customers[::-1]:
            if char == "Y":
                if not y_sum:
                    y_sum.appendleft(1)
                else:
                    y_sum.appendleft(y_sum[0] + 1)
            else:
                if not y_sum:
                    y_sum.appendleft(0)
                else:
                    y_sum.appendleft(y_sum[0])

        result = []
        # print(y_sum, n_sum)
        for i in range(len(customers) + 1):
            if i == 0:
                result.append(y_sum[i])
            elif i == len(customers):
                result.append(n_sum[-1])
            else:
                result.append(y_sum[i] + n_sum[i - 1])

        return result.index(min(result))
