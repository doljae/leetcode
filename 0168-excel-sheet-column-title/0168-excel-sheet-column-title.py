class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        temp = columnNumber
        while temp:
            temp -= 1
            result.append(chr((temp % 26) + ord('A')))
            temp = temp // 26

        return "".join(result[::-1])