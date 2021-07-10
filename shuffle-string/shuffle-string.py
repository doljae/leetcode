class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        answer = [""]*len(s)
        for i in range(len(s)):
            answer[indices[i]]=s[i]
        return "".join(answer)