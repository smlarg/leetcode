#Rank 1,029,876
# 20 medium, 57.1%

#329ms, 87.51%, 16.3Mb, 90.59%
# I'm sure at least the memory is just system flutter, but, relaxing
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        height = len(grid)
        width = len(grid[0])

        visited = [[False for _ in range(width)] for _ in range(height)]

        result = 0
        for i in range(height):
            for j in range(width):
                if visited[i][j]: continue
                visited[i][j] = True
                if grid[i][j] == "1":
                    result+=1
                    check = [(i+x,j+y) for x,y in [(1,0), (-1,0), (0,1) ,(0,-1)]]
                    while check:
                        k,l = check.pop()
                        if not(0<=k<height and 0<=l<width) or visited[k][l]: continue
                        visited[k][l] = True
                        if grid[k][l] == "1":
                            check += [(k+x,l+y) for x,y in [(1,0), (-1,0), (0,1) ,(0,-1)]]
        
        return result