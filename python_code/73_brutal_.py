class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row=[]
        col=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    row.append(i)
                    col.append(j)
            
        print row,col    
        for i in row:
            matrix[i]=[0]*len(matrix[0])
        
        for j in col:
            for i in range(len(matrix)):
                matrix[i][j]=0
        


 # use set() is better than List

 class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # row=[]
        # col=[]
        
        # use set will be better:
        row = set()
        col = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    row.add(i)
                    col.add(j)
            
        print row,col    
        for i in row:
            matrix[i]=[0]*len(matrix[0])
        
        for j in col:
            for i in range(len(matrix)):
                matrix[i][j]=0
        
        
        
        
        