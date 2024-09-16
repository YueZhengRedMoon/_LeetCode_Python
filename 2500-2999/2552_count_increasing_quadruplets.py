from typing import List

class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)

        great = [None] * n          # great[k][x]: nums[k]右边比x大的元素的个数
        great[-1] = [0] * (n + 1)   # 最右边右边没有数
        for k in range(n - 2, 1, -1):
            great[k] = great[k + 1].copy()  # 也可以写成great[k+1][:]
            for x in range(1, nums[k + 1]):
                great[k][x] += 1

        ans = 0
        less = [0] * (n + 1)    # less[j][x]:nums[j]左边比x小的元素的个数
        for j in range(1, n - 1):
            for x in range(nums[j - 1] + 1, n + 1):
                less[x] += 1
            for k in range(j + 1, n - 1):
                if nums[j] > nums[k]:
                    ans += less[nums[k]] * great[k][nums[j]]

        return ans
