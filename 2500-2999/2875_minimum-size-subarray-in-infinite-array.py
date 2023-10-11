from math import inf
from typing import List

class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        n = len(nums)
        ans = inf
        left = s = 0
        target_mod_total = target % total
        for right in range(n * 2):
            s += nums[right % n]
            while s > target_mod_total:
                s -= nums[left % n]
                left += 1
            if s == target_mod_total:
                ans = min(ans, right - left + 1)
        return (ans + target // total * n) if ans < inf else -1

