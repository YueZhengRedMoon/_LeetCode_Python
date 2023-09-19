from bisect import bisect_left
from typing import List

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        # solve(mx):返回最大金额为mx使，最多可以偷多少间房子
        def solve(mx: int) -> int:
            f0 = f1 = 0
            for x in nums:
                if x > mx:
                    f0 = f1
                else:
                    f0, f1 = f1, max(f1, f0 + 1)
            return f1

        return bisect_left(range(max(nums)), k, key=solve)

class Solution2:
    def minCapability(self, nums: List[int], k: int) -> int:
        def solve(mx: int) -> int:
            cnt = i = 0
            while i < len(nums):
                # 不偷
                if nums[i] > mx:
                    i += 1
                # 立刻偷
                else:
                    i += 2  # 跳过下一间房子
                    cnt += 1
            return cnt

        return bisect_left(range(max(nums)), k, key=solve)
