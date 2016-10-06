class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def BS( nums, target, first, last):
            if first == last:
                if nums[first]==target:
                    return first
                elif nums[first]>target:
                    return first
                else :
                    return first+1
                    
            if nums[(first+last)/2]<target:
                return BS( nums, target, (first+last+1)/2, last)
            else: 
                return BS( nums, target, first, (first+last)/2)
        

        if (len(nums)==0)|(target <nums[0]):
            return 0
        elif target > nums[:-1]:
            return len(nums)
        else:
            return BS( nums, target, 0, len(nums)-1)
        