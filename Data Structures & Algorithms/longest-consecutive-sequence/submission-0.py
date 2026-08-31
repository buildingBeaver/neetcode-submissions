class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        out = 0
        longest = 0
        for n in nums:
            if (n - 1) not in numsSet:
                longest = 1
                i = 1
                while (n + i) in numsSet:
                    longest += 1
                    i += 1
                out = max(longest, out)
        return out
