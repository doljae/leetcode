from typing import *


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:

        if len(arr) < 3:
            return False

        left_peak = 0

        while left_peak < len(arr) - 1 and arr[left_peak] < arr[left_peak + 1]:
            left_peak += 1

        right_peak = len(arr) - 1

        while right_peak > 0 and arr[right_peak - 1] > arr[right_peak]:
            right_peak -= 1

        return 0 < left_peak == right_peak < len(arr) - 1
