class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_set = set(list(jewels))
        answer = 0
        for stone in list(stones):
            answer += 1 if stone in jewels_set else 0
        return answer
        