from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        ln = len(nums)
        ans = ln * (ln - 1) * (ln - 2) // 6
        nums.sort()

        for t in range(ln - 1, 1, -1):
            l, r = 0, t - 1

            while l < r:
                if nums[l] + nums[r] <= nums[t]:
                    ans -= r - l
                    l += 1

                else:
                    r -= 1

        return ans
