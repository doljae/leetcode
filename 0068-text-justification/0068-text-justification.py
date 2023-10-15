from collections import deque
from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        temp = []
        words = deque(words)

        while words:
            cur = words[0]
            if not temp:
                temp.append(words.popleft())
            else:
                temp_length = 0
                for item in temp:
                    temp_length += len(item)

                gap = len(temp)
                if temp_length + gap + len(cur) > maxWidth:
                    result.append(temp)
                    temp = [words.popleft()]
                else:
                    temp.append(words.popleft())
        result.append(temp)

        result2 = []
        for item in result:
            used = 0
            for char in item:
                used += len(char)
            possible_gap = maxWidth - used
            # print(possible_gap)
            tt = []
            if len(item) == 1:
                result2.append("".join(item))
                continue
            a, b = divmod(possible_gap, len(item) - 1)
            if b == 0:
                for char in item:
                    tt.append(char)
                    tt.append(" " * a)
                tt.pop()
                result2.append("".join(tt))
                continue
            # print(item, a, b)
            bb = b
            for i in range(len(item)):
                tt.append(item[i])
                if i == len(item) - 1:
                    continue
                tt.append(" " * a)
                # print(1)
                # print(bb)
                if bb > 0:
                    # print("!")
                    tt.append(" ")
                    bb -= 1
                # print(tt)
            # print(2)
            # print(tt)
            # print(bb)
            result2.append("".join(tt))
            # print(len("".join(tt)))
        if result2:
            last_one = result2[-1]
            # print(last_one)
            # print(last_one.split())
            last_one = " ".join(last_one.split())
            result2.pop()
            result2.append(last_one)
        result3 = []
        for item in result2:
            result3.append(item.ljust(maxWidth))

        # for item in result3:
        #     print(item)
        #     print(len(item))
        return result3