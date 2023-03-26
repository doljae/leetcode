class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        repeated = set()
        recorded = set()

        for i in range(len(s) - 9):
            ten = s[i:i + 10]
            if ten in recorded:
                repeated.add(ten)
            else:
                recorded.add(ten)

        return list(repeated)