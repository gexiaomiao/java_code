class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # loop one integer over the whole array once, and make sure the rest two are not duplicates;
        # so this devide into  a problem that each loop we get a new target : target - num1,  find the best num2+num3.
        
        nums.sort()
        min_val = sys.maxint
        
        for i in range(len(nums)-2):
            istart = i+1
            iend = len(nums)-1
            itarget = target-nums[i]
            while  istart<iend :

                if min_val > abs(nums[istart]+nums[iend]-itarget):
                    min_val = abs(nums[istart]+nums[iend]-itarget)
                    output = nums[istart]+nums[iend]+nums[i];
                
                if min_val == 0:
                    return output
                
                if nums[istart]+nums[iend]<itarget:
                    istart +=1
                else:
                    iend -=1
                    
                
        
        
        
        return output
        