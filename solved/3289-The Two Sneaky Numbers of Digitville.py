from collections import Counter
from typing import List


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        return [x[0] for x in Counter(nums).items() if x[1] > 1]
