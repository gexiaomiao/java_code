class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        # if it is defined in numpy then we can transpose and easy to solve.
        if not matrix:
            return []
        List =[]
        row_min, row_max, col_min,col_max =0,len(matrix)-1,0,len(matrix[0])-1
        while row_min<row_max  and col_min<col_max:
            print row_min, row_max, col_min,col_max
            List += matrix[row_min][col_min:col_max]
            List += [matrix[i][col_max] for i in range(row_min,row_max)] 
            List += matrix[row_max][col_min+1:col_max+1][::-1]
            List += [matrix[i][col_min] for i in range(row_min+1,row_max+1)][::-1]
            
            row_min +=1
            row_max -=1
            col_min +=1
            col_max -=1
        if row_min <= row_max and  col_min <= col_max:
            if row_min == row_max:
                List += matrix[row_min][col_min:col_max+1]
            elif col_min == col_max:
                List += [matrix[i][col_min] for i in range(row_min,row_max+1)]
                
                
        return List


## better index representation

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        # if it is defined in numpy then we can transpose and easy to solve.
        if not matrix:
            return []
        List =[]
        row_min, row_max, col_min,col_max =0,len(matrix)-1,0,len(matrix[0])-1
        while row_min<row_max  and col_min<col_max:
            print row_min, row_max, col_min,col_max
            List += matrix[row_min][col_min:col_max]
            List += [matrix[i][col_max] for i in range(row_min,row_max)] 
            List += matrix[row_max][col_max:col_min:-1]
            List += [matrix[i][col_min] for i in range(row_max,row_min,-1)]
            
            row_min +=1
            row_max -=1
            col_min +=1
            col_max -=1
        if row_min <= row_max and  col_min <= col_max:
            if row_min == row_max:
                List += matrix[row_min][col_min:col_max+1]
            elif col_min == col_max:
                List += [matrix[i][col_min] for i in range(row_min,row_max+1)]
                
                
        return List