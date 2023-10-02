from typing import List
from collections import Counter

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        diff = Counter()
        for start, end in flowers:
            diff[start] += 1
            diff[end + 1] -= 1
        times = sorted(diff.keys())

        j = s = 0
        for p, i in sorted(zip(people, range(len(people)))):
            while j < len(times) and times[j] <= p:
                s += diff[times[j]]
                j += 1
            people[i] = s

        return people
