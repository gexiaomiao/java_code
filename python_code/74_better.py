class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix)==0 :
            raise ValueError
            
        r_min = 0
        r_max = len(matrix)
        matrix.append([sys.maxint])
        
        while r_min < r_max-1:
            r_mid = (r_min+r_max)/2
            if matrix[r_mid][0]<=target:
                r_min = r_mid
            else:
                r_max = r_mid
        row = r_min
        matrix.pop()
    
        
        c_min = 0
        c_max = len(matrix[r_min])-1
        

        while c_min< c_max:
            c_mid = (c_min+c_max)/2
            if matrix[row][c_mid] == target:
                return True
            if matrix[row][c_mid] < target:
                c_min  = c_mid+1
            else:
                c_max = c_mid-1
        
        return matrix[row][c_min]== target
