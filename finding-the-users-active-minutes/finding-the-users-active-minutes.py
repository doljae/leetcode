class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        dict1 = {}

        for log in logs:
            user_id, time = log
            if user_id not in dict1:
                dict1[user_id] = set()
            dict1[user_id].add(time)

        answer = [0] * k

        for key in dict1:
            target = len(dict1[key])
            if target:
                answer[target - 1] += 1

        return answer