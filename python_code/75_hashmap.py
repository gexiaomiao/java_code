class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        map ={}
        map[0] =0
        map[1] =0
        map[2] =0
        
        for num in nums:
            map[num]+=1
        nums[:] = [0]*map[0]+[1]*map[1]+[2]*map[2]

            