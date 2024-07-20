from typing import List


class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        mininum = float("inf")
        totalEnergy = currentEnergy
        
        for energy in enemyEnergies:
            mininum = min(mininum, energy)
            totalEnergy += energy

        if mininum > currentEnergy:
            return 0

        return (totalEnergy - mininum) // mininum