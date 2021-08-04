class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet_set = set([chr(i) for i in range(97, 123)])

        for char in sentence:
            alphabet_set.discard(char)

        return True if len(alphabet_set) == 0 else False
