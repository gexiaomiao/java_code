class Solution(object):
        
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def swap(nums,i0,i2):            
            while ((nums[i0]!=1)|(nums[i2]!=1))&(i0<i2):
                if nums[i0]==0:
                    i0+=1
                elif nums[i0]==2:
                    nums[i0]=nums[i2]
                    nums[i2]=2
                    i2-=1
                elif nums[i2]==2:
                    i2-=1
                elif nums[i2]==0:
                    nums[i2]=nums[i0]
                    nums[i0]=0
                    i0+=1
            
            return [i0,i2]
        
        
        [i0,i2]=swap(nums,0,len(nums)-1)
        i=i0
        print i0,i2
        print nums
        
        
        while (i<=i2)&(i0<i2):
            if nums[i]==0:
                nums[i]=nums[i0]
                nums[i0] = 0
                [i0,i2]=swap(nums,i0,i2)
            elif nums[i]==2:
                nums[i]=nums[i2]
                nums[i2] = 2
                [i0,i2]=swap(nums,i0,i2)
                
            i= max(i+1,i0)
            
        print nums
            

            
