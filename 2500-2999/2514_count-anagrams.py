from collections import Counter

class Solution:
    def countAnagrams(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        cnt = Counter()
        ans = mul = 1
        for s in s.split():
            cnt = Counter()
            for i, c in enumerate(s, 1):
                cnt[c] += 1
                mul = mul * cnt[c] % MOD
                ans = ans * i % MOD
        return ans * pow(mul, -1, MOD) % MOD