class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        size = m+n
        while (n>0):
            if (nums1[m-1]<=nums2[n-1])|(m<=0):  # first one is the regular one ,second one means the old nums1 is empty so we keep adding num2;
                nums1[m+n-1] = nums2[n-1]
                n-=1
            else:   # the rest situation is that nums1[m-1]>nums2[n-1] and m>0
                nums1[m+n-1] = nums1[m-1]
                m-=1