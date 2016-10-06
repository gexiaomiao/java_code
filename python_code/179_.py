class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        
        def getStack (A):
            result = []
            while A>0:
                result.append(A%10)
                A=A/10
            return result
        
        not nums    
            
        # def compare(A,B):
        #     A_list = getStack(A)
        #     B_list = getStack(B)
        #     while not A_list and not B_list:
        #         print A_list, B_list
        #         if A_list.pop() > B_list.pop():
        #             return 1
        #         elif A_list.pop() < B_list.pop():
        #             return -1

        #     if not A_list:
        #         return B_list.pop()
        #     elif not B_list:
        #         return -1
        
                    
        def compare_int(A,B):
            if A==0:
                return -1
            if B==0:
                return 1
            AAA=A
            BBB=B
            
            AA =A
            BB= B
            while AA>0:
                AA=AA/10
                B=B*10
            
            while BB>0:
                BB=BB/10
                A=A*10
            
            if A+BBB>B+AAA:
                return 1
            else:
                return -1

                

        # print getStack(1)
        # print getStack(10)
        print compare_int(0,2)
        print compare_int(9,0)    
        print nums
        
        
        nums.sort(compare_int,reverse=True)
        print nums
        
        if nums[0] ==0:
            return "0"
        
        result = ""
        for item in nums:
            result = result+str(item)
        
        return result
                
