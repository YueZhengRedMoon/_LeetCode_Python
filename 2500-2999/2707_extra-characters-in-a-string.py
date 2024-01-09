from typing import List

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dictionary = set(dictionary)
        dp = [0] * (n + 1)  # dp[i]:s[0:i]分隔后最小剩下的字符
        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + 1
            for j in range(i - 1, -1, -1):
                if s[j:i] in dictionary:
                    dp[i] = min(dp[i], dp[j])
        return dp[n]
