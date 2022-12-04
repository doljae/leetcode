class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        list1 = sentence.split()
        
        if len(list1) == 1:
            return list1[0][0] == list1[0][-1]
        
        list1.append(list1[0])
        
        for i in range(len(list1)-1):
            if list1[i][-1] != list1[i+1][0]:
                return False
        
        return True