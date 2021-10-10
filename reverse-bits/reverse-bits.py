class Solution:
    def reverseBits(self, n: int) -> int:

        bin_str = bin(n)[2:].zfill(32)
        
        return int(bin_str[::-1], 2)