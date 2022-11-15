class Solution:
    def digitSum(self, s: str, k: int) -> str:

        result = s

        while len(result) > k:
            l = []
            temp_result = result + "0" * (k - len(result) % k)
            for i in range(0, len(result), k):
                l.append(temp_result[i:i + k])

            result = ""
            for item in l:
                temp = list(map(int, list(item)))
                result += str(sum(temp))
                
        return result