from typing import List


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        while len(nums) > 1:
            for i in range(len(nums) - 1):
                nums[i] += nums[i + 1]
                nums[i] %= 10

            nums.pop()

        return nums[0]
