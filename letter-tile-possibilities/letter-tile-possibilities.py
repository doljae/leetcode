from collections import Counter


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count_map = Counter(tiles)

        answer = set()

        def dfs(cur_val):

            if cur_val in answer:
                return
            answer.add(cur_val)

            for key in count_map:
                if count_map[key]:
                    count_map[key] -= 1
                    dfs(cur_val + key)
                    count_map[key] += 1

        dfs("")

        return len(answer) - 1


print(Solution().numTilePossibilities("AAABBC"))