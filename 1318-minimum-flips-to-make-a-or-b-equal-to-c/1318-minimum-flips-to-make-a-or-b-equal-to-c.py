class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        need_flips = ((a | b) ^ c).bit_count()
        need_extra_flips = (a & b & ((a | b) ^ c)).bit_count()

        return need_flips + need_extra_flips
