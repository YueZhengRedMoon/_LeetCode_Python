from typing import List

class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ans = []
        for word in words:
            for s in word.split(separator):
                if len(s) > 0:
                    ans.append(s)
        return ans
