class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        
######
# |       1        |mid1|       2        |
# |   3   |mid2|   4   |


# if mid1< mid2  1<2,4  4>1,3
# if mid1> mid2  3<2,4  2>1,3


        
        f1 = 0
        f2 = 0
        l1 = len(nums1)-1
        l2 = len(nums2)-1
        
        if len(nums1)==0 and len(nums2)==0:
            return nums1
        if len(nums1)==0:
            return (nums2[(f2+l2)/2]+nums2[(f2+l2+1)/2])/2.0
        if len(nums2)==0:
            return (nums1[(f1+l1)/2]+nums1[(f1+l1+1)/2])/2.0
            
        
        while(f1<l1 and f2<l2):
            mid1 = (f1+l1)/2
            mid11 = (f1+l1+1)/2
            mid2 = (f2+l2)/2
            mid22 = (f2+l2+1)/2
            
            if nums1[mid1]<nums2[mid2] and nums1[mid11]>nums2[mid22]:
                return (nums2[mid2]+nums2[mid22])/2.0
            
            if nums1[mid1]>nums2[mid2] and nums1[mid11]<nums2[mid22]:
                return (nums1[mid1]+nums1[mid11])/2.0
            
            if nums1[mid1]+nums1[mid11]<nums2[mid2]+nums2[mid22]:
                if (l1-f1)>=(l2-f2): # the num2 is short
                    f1 = f1+(l2-mid2)
                    l2 = mid2
                else:
                    l2 = l2-(mid11-f1)
                    f1= mid11
            else:
                if (l1-f1)>=(l2-f2): # the num2 is short
                    l1 = l1-(mid22-f2)
                    f2 = mid22
                else:
                    f2 = f2+(l1-mid1)
                    l1= mid1
                
        print f1,f2,l1,l2
        if f1==l1:
            if f2 ==l2:        
                return  (nums1[f1]+nums2[f2])/2.0
            elif (l2-f2)%2: 
                if nums1[f1]< nums2[(f2+l2)/2] : # nums1 below the mid of num2, 
                    l2 =l2-1
                    return (nums2[(f2+l2)/2])
                elif nums1[f1]> nums2[(f2+l2+1)/2] :
                    f2= f2+1
                    return (nums2[(f2+l2)/2])
                else:
                    return nums1[f1] 
            else:
                if nums1[f1]<= nums2[(f2+l2)/2] : # nums1 below the mid of num2, 
                    return (max(nums1[f1],nums2[(f2+l2)/2-1])+nums2[(f2+l2)/2])/2.0
                else:
                    return (min(nums1[f1],nums2[(f2+l2)/2+1])+nums2[(f2+l2)/2])/2.0
                
        else:
            if (l1-f1)%2: 
                if nums2[f2]< nums1[(f1+l1)/2] : # nums1 below the mid of num2, 
                    l1 =l1-1
                    return (nums1[(f1+l1)/2])
                elif nums2[f2]> nums1[(f1+l1+1)/2] :
                    f1= f1+1
                    return (nums1[(f1+l1)/2])
                else:
                    return nums2[f2] 
            else:
                if nums2[f2]<= nums1[(f1+l1)/2] : # nums1 below the mid of num2, 
                    return (max(nums2[f2],nums1[(f1+l1)/2-1])+nums1[(f1+l1)/2])/2.0
                else :
                    return (min(nums2[f2],nums1[(f1+l1)/2+1])+nums1[(f1+l1)/2])/2.0
        
                    
                