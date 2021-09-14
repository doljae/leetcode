from typing import *


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:

        if len(arr) < 3:
            return False

        peak_index = 0

        while peak_index < len(arr) - 1 and arr[peak_index] < arr[peak_index + 1]:
            peak_index += 1

        peak_index2 = len(arr) - 1

        while peak_index2 > 0 and arr[peak_index2 - 1] > arr[peak_index2]:
            peak_index2 -= 1

        return peak_index == peak_index2 and peak_index != 0 and peak_index2 != len(arr) - 1