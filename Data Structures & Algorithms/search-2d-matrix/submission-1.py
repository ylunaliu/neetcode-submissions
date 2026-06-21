class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        #Need to do a binary search for rows:
        top = 0
        bottom = rows-1
        target_row = -1
        while top <= bottom:
            row = (top+bottom)//2
            if target<matrix[row][0]:
                bottom = row-1
            elif target>matrix[row][-1]:
                top = row+1
            else:
                target_row = row
                break
        if target_row == -1:
            return False
            
        left = 0
        right = cols-1
        while left<=right:
            col = (left+right)//2
            if matrix[row][col]==target:
                return True
            elif(target>matrix[row][col]):
                left = col+1
            else:
                right = col-1
        return False
