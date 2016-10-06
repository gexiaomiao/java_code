class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        nums_str =  [str(i) for i in nums]
        nums_str.sort(cmp=lambda a,b : cmp(b+a,a+b))

        return ''.join(nums_str).lstrip('0') or '0'
