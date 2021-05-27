class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack = []
        answer = 0
        for price in prices:
            if not stack:
                stack.append(price)
            else:
                if stack[-1] < price:
                    answer+=price-stack[-1]
                    stack.pop()
                    stack.append(price)
                else:
                    stack.pop()
                    stack.append(price)
        return answer