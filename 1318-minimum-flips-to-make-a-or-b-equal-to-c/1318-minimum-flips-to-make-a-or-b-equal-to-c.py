class Solution:
    def convert_bit_array(self, num):
        convert = list(bin(num).replace("0b", ""))
        return list(map(int, ([0] * (30 - len(convert)) + convert)))

    def minFlips(self, a: int, b: int, c: int) -> int:
        result = 0

        target_c_array = self.convert_bit_array(c)
        target_a_array = self.convert_bit_array(a)
        target_b_array = self.convert_bit_array(b)

        for i in range(len(target_c_array)):
            cur_a, cur_b, cur_c = target_a_array[i], target_b_array[i], target_c_array[i]
            if cur_a | cur_b == cur_c:
                continue

            if cur_c == 0:
                if cur_a == 1:
                    result += 1
                if cur_b == 1:
                    result += 1
            elif cur_c == 1:
                result += 1

        return result