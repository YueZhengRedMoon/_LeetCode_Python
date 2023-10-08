from typing import List
from collections import Counter

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)
        if 1 in counter.values():
            return -1
        return sum((c + 2) // 3 for c in counter.values())
