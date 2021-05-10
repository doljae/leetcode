class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1={}
        
        def count(input_string):
            count_list=[0]*26
            for char in input_string:
                count_list[ord(char)-ord("a")]+=1
            return tuple(count_list)
            
        
        for str in strs:
            temp=count(str)
            if temp not in dict1:
                dict1[temp]=[str]
            else:
                dict1[temp].append(str)
        return dict1.values()
        