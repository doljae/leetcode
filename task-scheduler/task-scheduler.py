from typing import *
from heapq import *
from collections import defaultdict


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 모든 일을 마칠 수 있는 최소 시간을 반환해라
        # 단 같은 일 사이의 간격은 n 이상이 되어야 한다.
        # n=2, a -> idle -> idle -> a
        # n=1, a-> idle -> a
        # n=2, a -> b -> idle -> a -> b
        # t1 = ["A", "A", "A", "B", "B", "B"]
        # 최소시간이 되려면 idle 시간이 최소여야 한다
        # 그러기 위해선 최대한 모든 일을 골고루 처리해야한다.
        # 특정 일을 수행한 마지막 시간을 기록하고 이것을 우선순위큐랑 조합하면
        # 될 것 같은데?...
        dict1 = defaultdict(int)
        for task in tasks:
            dict1[task] += 1
        q = []
        for task in dict1:
            q.append([0, -dict1[task], task])
        heapify(q)
        seq, time = [], 0
        while q:
            for i in range(len(q)):
                if q[i][0] > 0:
                    q[i][0] -= 1
            # print("!", q)
            heapify(q)
            gap, left_task, task_name = heappop(q)
            left_task = -left_task
            # print(f"{task_name}, gap: {gap}, 남은 작업: {left_task}")
            if gap > 0:
                for i in range(gap):
                    seq.append("idle")
                for i in range(len(q)):
                    if q[i][0] > 0:
                        q[i][0] -= gap
                seq.append(task_name)
                if left_task - 1 > 0:
                    q.append([n + 1, -(left_task - 1), task_name])
            else:
                seq.append(task_name)
                if left_task - 1 > 0:
                    q.append([n + 1, -(left_task - 1), task_name])
            # print(q)
            # print(seq)
        return len(seq)