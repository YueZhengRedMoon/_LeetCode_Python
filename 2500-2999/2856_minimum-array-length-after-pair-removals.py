from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    '''
        假设x出现次数最多，其出现次数为maxCnt

        如果 maxCnt * 2 > n，则其余所有n - maxCnt个数都要与x消除，还剩下maxCnt * 2 - n个数
        如果 maxCnt * 2 <= n且n是偶数，则可以把其余数消除致剩下maxCnt个数，然后再和x消除，最后剩下0个数
            - 例如: 1 1 1 1 2 2 2 3 3 3 -> 1 1 1 1 2 2 3 3 -> 全部消除
        如果 maxCnt * 2 <= n且n是奇数，同上，最后还会剩下一个数

        由于nums是有序的，如果maxCnt超过数组长度的一半，那么nums[n/2]一定是出现次数最多的数
    '''

    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        x = nums[n // 2]
        # bisect_right返回第一个>x的num的索引，bisect_left返回第一个>=x的索引
        max_cnt = bisect_right(nums, x) - bisect_left(nums, x)
        return max(max_cnt * 2 - n, n % 2)
