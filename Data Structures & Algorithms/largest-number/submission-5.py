from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(n) for n in nums]
        
        def compare(a, b):
            if a + b > b + a:
                return -1
            if b + a > a + b:
                return 1
            return 0
        
        nums.sort(key=cmp_to_key(compare))
        result = "".join(nums)
        if result[0] == '0': return '0'
        return result
        