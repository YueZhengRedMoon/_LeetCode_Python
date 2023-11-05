from typing import List
from collections import Counter

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        counter = Counter()
        for i in range(10, n + 1):
            counter[s[i - 10:i]] += 1
        ans = [sub_str for sub_str, cnt in counter.items() if cnt > 1]
        return ans
