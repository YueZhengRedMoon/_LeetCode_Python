from typing import List
from collections import Counter

class Solution:
    def countInterestingSubarrays(self, nums: List[int], m: int, k: int) -> int:
        n = len(nums)
        pre = [0] * (n + 1) # 前缀和数组
        for i, x in enumerate(nums):
            pre[i + 1] = pre[i] + (x % m == k)

        ans = 0
        cnt = Counter()
        for s in pre:
            ans += cnt[(s % m - k + m) % m]
            cnt[s % m] += 1
        return ans

class Solution2:
    def countInterestingSubarrays(self, nums: List[int], m: int, k: int) -> int:
        ans = 0
        cnt = Counter()
        cnt[0] = 1
        s = 0
        for x in nums:
            s += (x % m == k)
            ans += cnt[(s % m - k + m) % m]
            cnt[s % m] += 1
        return ans
