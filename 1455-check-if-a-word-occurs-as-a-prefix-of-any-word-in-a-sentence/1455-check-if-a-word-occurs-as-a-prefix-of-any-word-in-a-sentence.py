class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        
        sentence_list = sentence.split()
        length = len(searchWord)

        for index, word in enumerate(sentence_list):
            if word[:length] == searchWord:
                return index + 1
        
        return -1