from typing import *
from collections import deque, defaultdict


class Solution:
    def decodeString(self, s: str) -> str:
        list1 = deque(list(s))
        stack = []
        dict1 = {}
        dict_key = 65
        while list1:
            # print(list1)
            # print(stack)
            cur = list1.popleft()
            if cur != "]":
                stack.append(cur)
            else:
                temp = []
                while stack and stack[-1] != "[":
                    t = stack.pop()
                    if t in dict1:
                        temp.append(dict1[t])
                    else:
                        temp.append(t)
                stack.pop()
                temp = temp[::-1]
                temp2 = []
                while stack and stack[-1].isdigit():
                    temp2.append(stack.pop())
                temp2 = temp2[::-1]
                target_num, target_str = int("".join(temp2)), "".join(temp)
                dict1[chr(dict_key)] = target_str * target_num
                stack.append(chr(dict_key))
                dict_key += 1
        result = ""
        for string in stack:
            if string in dict1:
                result += dict1[string]
            else:
                result += string
        return result