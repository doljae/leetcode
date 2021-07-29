class Solution:
    def sortSentence(self, s: str) -> str:
        list1 = s.split()
        list1.sort(key=lambda x:x[-1])
        list1 = list(map(lambda x: x[:len(x)-1],list1))
        return " ".join(list1)