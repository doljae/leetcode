class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1={}
        for str in strs:
            temp="".join(sorted(list(str)))
            if temp not in dict1:
                dict1[temp]=[str]
            else:
                dict1[temp].append(str)
        return dict1.values()
        