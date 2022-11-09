class Solution:
    def capitalizeTitle(self, title: str) -> str:
        result = []
        
        for word in title.split():
            if len(word) in [1, 2]:
                word = word.lower()
            else:
                word = word[0].upper() + word[1:].lower()
            result.append(word)
        
        return " ".join(result)