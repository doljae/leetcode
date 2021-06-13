class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        dict1 = defaultdict(int)
        for n1 in nums1:
            for n2 in nums2:
                dict1[n1 + n2] += 1
        dict2 = defaultdict(int)
        for n3 in nums3:
            for n4 in nums4:
                dict2[n3 + n4] += 1
        answer = 0
        for key in dict1:
            if -key in dict2:
                answer += dict1[key] * dict2[-key]
        return answer