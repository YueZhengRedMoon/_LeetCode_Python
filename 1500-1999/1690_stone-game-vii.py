from itertools import accumulate
from typing import List
from functools import cache

class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)
        prefix = list(accumulate(stones, initial=0))

        # 计算sum(stones[i,j])
        def range_sum(i: int, j: int) -> int:
            return prefix[j + 1] - prefix[i]

        # dfs(i,j) 表示剩余石子从 stones[i] 到 stones[j]，先手得分减去后手得分的最大值
        @cache
        def dfs(i: int, j: int) -> int:
            if i == j:
                return 0
            return max(range_sum(i, j - 1) - dfs(i, j - 1), range_sum(i + 1, j) - dfs(i + 1, j))

        ans = dfs(0, n - 1)
        dfs.cache_clear()
        return ans
