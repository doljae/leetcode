class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 1_000_000_007

        count = 1

        seats = 0

        previous_pair_last = None

        for index, thing in enumerate(corridor):
            if thing == "S":
                seats += 1

                if seats == 2:
                    previous_pair_last = index
                    seats = 0
                
                elif seats == 1 and previous_pair_last is not None:
                    count *= (index - previous_pair_last)
                    count %= MOD
        
        if seats == 1 or previous_pair_last is None:
            return 0

        return count