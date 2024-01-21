from bisect import bisect_left
from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def check(mx: int) -> bool:
            cnt = 1
            s = 0
            for x in nums:
                if s + x <= mx:
                    s += x
                else:
                    if cnt == k:
                        return False
                    cnt += 1
                    s = x
            return True

        # 必须是左闭右开区间
        right = sum(nums)
        left = max(max(nums), (right - 1) // k + 1)
        return left + bisect_left(range(left, right), True, key=check)


if __name__ == "__main__":
    solution = Solution()
    ans = solution.splitArray([1, 4, 4], 3)
    print(ans)

