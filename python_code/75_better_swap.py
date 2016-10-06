
class Solution(object):
        
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        
        
        i0=0
        i=i0
        i2=len(nums)-1
        print i0,i2
        print nums
        
        
        while (i<=i2):
            if nums[i]==0:
                nums[i]=nums[i0]
                nums[i0] = 0
                i+=1
                i0+=1
                
            elif nums[i]==1:
                i+=1
            else:
                nums[i]=nums[i2]
                nums[i2] = 2
                i2-=1

            
                