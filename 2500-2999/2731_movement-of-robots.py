from typing import List

class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)
        for i in range(n):
            nums[i] += d if s[i] == 'R' else -d
        nums.sort()

        right_sum = 0
        for num in nums:
            right_sum = (right_sum + num) % MOD

        ans = 0
        for i in range(n):
            right_sum = (right_sum - nums[i]) % MOD
            ans = (ans + right_sum - (n - i - 1) * nums[i]) % MOD

        return ans

class Solution2:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        for i, c in enumerate(s):
            nums[i] += d if c == 'R' else -d
        nums.sort()

        ans = s = 0
        for i, x in enumerate(nums):
            ans += i * x - s
            s += x

        return ans % (10 ** 9 + 7)
