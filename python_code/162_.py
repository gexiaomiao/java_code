class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first =0
        last = len(nums)-1
        if last==0:
            return 0

        if nums[0]>nums[1]:
                return 0
        if nums[last]>nums[last-1]:
                return last
        
        
        #while (first<last-1):  #both OK why???
        while (first<=last):
            mid = (first + last)/2
            if (nums[mid]>nums[mid+1])&(nums[mid]>nums[mid-1]):
                return mid
            
            if (nums[mid]<nums[mid+1]):
                first = mid
            else :
                last = mid
                
                
        