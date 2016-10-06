# the change is that some times the duplicate will give both side the same value:
# [1,3,1,1,1,1]

# one simples way is to limit the array first.



class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
#########################################################        
        def BS (nums, first, last):
            
            if first ==last:
                if nums[first] == target:
                    return True
                else:
                    return False
                
            if nums[(first+last)/2] < target:
                return BS(nums, (first+last+1)/2, last)
            else: 
                return BS(nums, first, (first+last)/2)
            

                
#########################################################                
        def search_rec(nums,target,first,last):
            if first == last:
                if nums[first] == target:
                    return True
                else:
                    return False
            elif (nums[first]==nums[last]):
                last-=1
                return search_rec(nums,target,first,last)
                
            else:
                if (nums[first]<=nums[(first+last)/2]):
                    if (target<=nums[(first+last)/2])&(target>=nums[first]):
                        return search_rec(nums,target, first, (first+last)/2)
                    else:
                        return search_rec(nums,target,(first+last+1)/2,last)
                else:
                    if (target>=nums[(first+last)/2])&(target<=nums[last]):
                        return search_rec(nums,target,(first+last)/2,last)
                    else:
                        return search_rec (nums,target, first, (first+last)/2)
                        
##########################################################   
        return search_rec(nums,target,0,len(nums)-1)     
                
        