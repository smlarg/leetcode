# Rank = 1,029,876
# finished 12 med, 45.8%

mat = [[0,0,0],[0,1,0],[0,0,0]]

mat = [[0,0,0],[0,1,0],[1,1,1]]

mat = [[0,1],[1,1]]

mat = [[0,1,1],[1,1,1],[1,1,1]]

mat = [[0,5,27,835],[1,1,1,1],[5,5,5,5],[6,6,6,5]]

mat = [[0,5,27,835],[515,'taco',3.14159,[]],[5,5,5,5],[6,6,6,5]]

mat = [[0],[0],[0],[0],[0]]

# oh my god
# anyway
# 1243, 28.26%, but that's in the main gaussian so whatever
class Solution:
    # i looks a lot like j, and = looks a lot like == !!!!!!!!!
    # ho boy
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        from collections import deque
        
        height = len(mat)
        width = len(mat[0])
        
        result = [[-1 for _ in range(width)] for _ in range(height)]
        
        q = deque()
        
        for i in range(height):
            for j in range(width):
                if mat[i][j] == 0:
                    q.append((i,j))
                    result[i][j] = 0
        
        while q:
            i,j = q.popleft()
            distance = result[i][j] + 1
            if i > 0 and result[i-1][j] == -1:
                q.append((i-1,j))
                result[i-1][j] = distance
            if i + 1 < height and result[i+1][j] == -1:
                q.append((i+1,j))
                result[i+1][j] = distance
            if j > 0 and result[i][j-1] == -1:
                q.append((i,j-1))
                result[i][j-1] = distance
            if j + 1 < width and result[i][j+1] == -1:
                q.append((i,j+1))
                result[i][j+1] = distance
        
        return result