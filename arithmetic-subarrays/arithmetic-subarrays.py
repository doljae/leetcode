class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        index = 0
        answer = []
        while index < len(l):
            left, right = l[index], r[index]
            target_list = nums[left:right + 1]
            set_list = set(target_list)
            max_val, min_val = max(set_list), min(set_list)
            length = len(target_list)

            gap = (max_val - min_val) // (length - 1)
            if len(set_list) == 1:
                answer.append(True)
                index += 1
                continue
            elif len(set_list) != length:
                answer.append(False)
                index += 1
                continue
            left, right = min_val + gap, max_val - gap

            while left <= right:
                if left not in set_list:
                    answer.append(False)
                    break
                if right not in set_list:
                    answer.append(False)
                    break
                left, right = left + gap, right - gap

            if left > right:
                answer.append(True)

            index += 1
        return answer