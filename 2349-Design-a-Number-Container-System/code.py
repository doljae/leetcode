class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits)) == 1:
            return "Flush"

        dict1 = defaultdict(int)

        for rank in ranks:
            dict1[rank] += 1

        max_val = max(dict1.values())

        if max_val >= 3:
            return "Three of a Kind"
        elif max_val >= 2:
            return "Pair"

        return "High Card"