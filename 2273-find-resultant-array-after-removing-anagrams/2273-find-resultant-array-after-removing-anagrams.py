from collections import deque

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        
        deleted = []
        checked = None
        
        for index, word in enumerate(words):
            target = "".join(sorted(list(word))) 
            if target == checked:
                deleted.append(index)
            
            else:
                checked = target
        
        result = []
        for index, word in enumerate(words):
            if index not in deleted:
                result.append(word)
        
        return result
            