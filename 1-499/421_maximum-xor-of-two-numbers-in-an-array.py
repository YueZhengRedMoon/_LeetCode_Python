from typing import List

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        ans = mask = 0
        high_bit = max(nums).bit_length() - 1
        for i in range(high_bit, -1, -1):
            mask |= 1 << i
            new_ans = ans | (1 << i)
            seen = set()
            for x in nums:
                x &= mask   # 低于i的比特位置为0
                if new_ans ^ x in seen:
                    ans = new_ans   # x ^ ans = new_ans, ans = new_ans ^ x
                    break
                seen.add(x)
        return ans
