class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if target < nums[0] or target > nums[len(nums)-1]:
            return [-1,-1]
        
        target1= target*1.0-0.5
        target2= target*1.0+0.5
        print target1
        
        if  target == nums[0]:
            start =0
        else:
            imin = 0
            imax = len(nums)-1
    
            
            while imin < imax-1:
                imid= (imin + imax)/2
                if nums[imid]>target1:
                    imax = imid
                else:
                    imin = imid
                    
            if nums[imax]==target :
                start = imax
            else:
                return [-1,-1]
                
        
        
        if  target == nums[len(nums)-1]:
            end =len(nums)-1
        else:
            imin = 0
            imax = len(nums)-1
            
            while imin < imax-1:
                imid= (imin + imax)/2
                if nums[imid]>target2:
                    imax = imid
                else:
                    imin = imid
            
            end = imin
        
        return [start, end]
        
        
        
            