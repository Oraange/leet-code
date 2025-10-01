class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        empty = numBottles

        while exc := (empty // numExchange):
            ans += exc
            empty = empty % numExchange + exc

        return ans
