from typing import List
from collections import Counter

class Solution:
    '''
    x1 XOR x2 + y1 XOR y2 = k
    x1 XOR x2 = i       -> x1 = i XOR x2
    y1 XOR y2 = k-i     -> y1 = (k-i) XOR y2

    枚举(x2, y2),则(x1, y1) = (i XOR x2, (k-i) XOR y2)

    '''

    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        ans = 0
        cnt = Counter()
        for x, y in coordinates:
            for i in range(k + 1):
                ans += cnt[x ^ i, y ^ (k - i)]  # 对于Counter()，当元组作为键时，可以省略圆括号
            cnt[x, y] += 1
        return ans
