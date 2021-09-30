class Solution:
    def reverseWords(self, s: str) -> str:
        list1 = s.split()
        for i in range(len(list1)):
            target=list1[i]
            list1[i]=target[::-1]
        
        return " ".join(list1)