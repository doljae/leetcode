class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:

        def make_trace(input_string):
            trace, index = [], 0
            while index < len(input_string):
                cur = input_string[index]
                temp = [cur]
                while index + 1 < len(input_string) and input_string[index + 1] == cur:
                    temp.append(cur)
                    index += 1
                trace.append("".join(temp))
                index += 1
            return trace

        def match(str1, str2):
            if str1 in str2:
                return True
            return False

        trace1, trace2 = make_trace(name), make_trace(typed)

        if len(trace1) != len(trace2):
            return False

        for i in range(len(trace1)):
            if not match(trace1[i], trace2[i]):
                return False

        return True