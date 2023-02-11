from typing import *


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        num_of_boats = 0

        left, right = 0, len(people) - 1

        while left <= right:
            capa = limit
            right_weight = people[right]
            capa -= right_weight
            right -= 1

            if left <= right and capa >= people[left]:
                capa -= people[left]
                left += 1

            num_of_boats += 1

        return num_of_boats