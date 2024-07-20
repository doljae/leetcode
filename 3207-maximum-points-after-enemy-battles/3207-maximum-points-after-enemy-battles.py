from typing import List


class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:

        enemyEnergies.sort()
        points = 0
        mark = set()

        if currentEnergy <= 0:
            return 0
        if currentEnergy < enemyEnergies[0]:
            return 0

        right = len(enemyEnergies) - 1

        while right >= 0:
            if currentEnergy >= enemyEnergies[0]:
                points += currentEnergy // enemyEnergies[0]
                currentEnergy = currentEnergy % enemyEnergies[0]
            else:
                currentEnergy += enemyEnergies[right]
                right -= 1

        return points
