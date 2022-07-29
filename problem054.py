# submitted, but metrics aren't great

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        #result = []
        result = [0]*(m*n)
        rl = 0
        top = 0
        bottom = m
        left = 0
        right = n
        while (rl< m*n):
            for j in range(left, right):
                #result.append(matrix[top][j])
                result[rl] = matrix[top][j]
                rl+=1
            if rl == m*n:
                continue
            top +=1
            for i in range(top, bottom):
                #result.append(matrix[i][right-1])
                result[rl] = matrix[i][right-1]
                rl+=1
            if rl == m*n:
                continue
            right -=1
            for j in range(right-1, left-1, -1):
                #result.append(matrix[bottom-1][j])
                result[rl] = matrix[bottom-1][j]
                rl+=1
            if rl == m*n:
                continue
            bottom -= 1
            for i in range(bottom-1, top-1, -1):
                #result.append(matrix[i][left])
                result[rl] = matrix[i][left]
                rl+=1
            if rl == m*n:
                continue
            left += 1
        return result