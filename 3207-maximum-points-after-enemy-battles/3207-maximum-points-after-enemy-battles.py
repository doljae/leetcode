from typing import List


class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        # 처음에 가장 적은 에너지를 가진 애의 애너지를 빼고 포인트를 얻어야 함
        # 그 다음에 가장 큰 에너지를 가진 애를 마킹하고 애너지를 더해야 함
        # 이걸 반복?

        enemyEnergies.sort()
        points = 0
        mark = set()

        if currentEnergy <= 0:
            return 0

        right = len(enemyEnergies) - 1

        while right:
            if currentEnergy >= enemyEnergies[0]:
                points += currentEnergy // enemyEnergies[0]
                currentEnergy = currentEnergy % enemyEnergies[0]
            else:
                currentEnergy += enemyEnergies[right]
                right -= 1

        return points
