from typing import *


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        cur_num = int("".join(list(map(str, digits))))
        target_num = cur_num + 1
        return list(map(int, list(str(target_num))))
