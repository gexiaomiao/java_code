class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        ## the key is to get ride of the part we do not need.
        
        col = len(matrix[0])-1
        row =0
        while  row<len(matrix) and col>=0 : 
            if matrix[row][col]== target:
                return True
            elif matrix[row][col] < target: ## the target is still large, so we should increase the row, the same row is ruled out.
                row+=1
            else:
                col-=1
                
        return False
        