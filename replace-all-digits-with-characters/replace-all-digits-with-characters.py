class Solution:
    def replaceDigits(self, s: str) -> str:
        def shift(input_char, shift_num):
            return chr(ord(input_char) + shift_num)

        list1 = list(s)
        for i in range(len(list1)):
            if list1[i].isdigit():
                list1[i] = shift(list1[i - 1], int(list1[i]))

        return "".join(list1)
