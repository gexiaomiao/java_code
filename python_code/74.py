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
        r_max = len(matrix)-1
        if target >= matrix[r_max][0] :
            row = r_max
        elif target<matrix[0][0] :
            return False
        elif r_max<2:
            row =0
        else:
            while r_min < r_max-1:
                r_mid = (r_min+r_max)/2
                if matrix[r_mid][0]<=target:
                    r_min = r_mid
                else:
                    r_max = r_mid
            row = r_min
        
        
        c_min = 0
        c_max = len(matrix[r_min])-1
        
        if target>=matrix[row][c_max] :
            return target == matrix[row][c_max]
        elif c_max<2:
            return target == matrix [row][0]
        else:
            while c_min< c_max-1:
                c_mid = (c_min+c_max)/2
                if matrix[row][c_mid]<= target:
                    c_min  = c_mid
                else:
                    c_max = c_mid
            return matrix[row][c_min]== target

        
        
        