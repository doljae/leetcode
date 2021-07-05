class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        answer = 0 
        for account in accounts:
            answer = max(answer, sum(account))
        return answer