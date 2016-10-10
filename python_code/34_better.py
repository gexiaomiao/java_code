class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        ## better binary:
        imin = 0
        imax = len(nums)-1
        ## find the lwo bound
        while imin<imax:
            imid= (imin + imax)/2
            if nums[imid]<target :
                imin = imid+1
            else:
                imax = imid
        if nums[imax] == target:
            start =imax
        else:
            return [-1,-1]
        
        ## find the hight bound
        
        imin = start
        imax = len(nums)-1
        
        while imin<imax:
            imid= (imin + imax+1)/2
            if nums[imid]>target :
                imax = imid-1
            else:
                imin = imid
        return [start, imin]
