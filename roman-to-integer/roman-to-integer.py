class Solution:
    def romanToInt(self, s: str) -> int:
        dict1 = {'I': 1,
                 'V': 5,
                 'X': 10,
                 'L': 50,
                 'C': 100,
                 'D': 500,
                 'M': 1000}
        answer, index = 0, 0
        while index < len(s):
            if s[index] == 'I' and index + 1 < len(s) and s[index + 1] in ['V', 'X']:
                answer += (dict1[s[index + 1]] - dict1[s[index]])
                index += 1
            elif s[index] == 'X' and index + 1 < len(s) and s[index + 1] in ['L', 'C']:
                answer += (dict1[s[index + 1]] - dict1[s[index]])
                index += 1
            elif s[index] == 'C' and index + 1 < len(s) and s[index + 1] in ['D', 'M']:
                answer += (dict1[s[index + 1]] - dict1[s[index]])
                index += 1
            else:
                answer += dict1[s[index]]
            index += 1

        return answer
