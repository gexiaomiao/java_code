class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}
        for i,num in enumerate(nums):
            if num in map:
                return [i, map[num]]
            else:
                map[target-num] = i;
        