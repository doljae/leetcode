from typing import *


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        def helper(input_val):
            if ruleKey == "type":
                return True if input_val[0] == ruleValue else False
            elif ruleKey == "color":
                return True if input_val[1] == ruleValue else False
            elif ruleKey == "name":
                return True if input_val[2] == ruleValue else False

        return len(list(filter(lambda x: helper(x), items)))