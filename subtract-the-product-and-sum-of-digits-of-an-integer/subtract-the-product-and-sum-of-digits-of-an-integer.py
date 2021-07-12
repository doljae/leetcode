class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product, ssum = 1,0
        for num in list(map(int,list(str(n)))):
            product*=num
            ssum+=num
        return product - ssum