from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp, value))
        # print("==========================")
        # for key in self.time_map:
        #     print(key, self.time_map[key])

    def get(self, key: str, timestamp: int) -> str:

        if not self.time_map[key]:
            return ""

        if self.time_map[key][-1][0] <= timestamp:
            return self.time_map[key][-1][1]

        left, right = 0, len(self.time_map[key]) - 1
        res = ""
        while left <= right:
            mid = (left + right) // 2
            target = self.time_map[key][mid]

            if target[0] <= timestamp:
                res = target[1] 
                left = mid + 1 
            else:
                right = mid - 1
        return res