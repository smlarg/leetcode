# okay rank didn't even change overnight, so
# 21med, 58.0%

grid = [[2,1,1],[1,1,0],[0,1,1]]
[[2,1,1],[0,1,1],[1,0,1]]
[[0,2]]
[[2,0,0,1],[1,0,2,1],[1,0,1,0],[1,1,1,1]]

#104ms, 17.78%, 91.38% memory but that's low variance anyway
class SolutionDict:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        
        fresh_stack = []
        rotten_stack = []
        
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 1:
                    fresh_stack.append((i,j))
                    continue
                if grid[i][j] == 2:
                    rotten_stack.append((i,j))
        
        rotting_time = {}
        for i,j in fresh_stack:
            rotting_time[(i,j)] = height*width + 1
        
        while rotten_stack:
            i,j = rotten_stack.pop()
            check = [(i+x,j+y, 1) for x,y in [(1,0), (-1,0), (0,1) ,(0,-1)]]
            while check:
                k,l,r = check.pop()
                if not(0<=k<height and 0<=l<width) or (not grid[k][l] == 1) or rotting_time[(k,l)] <= r: continue
                rotting_time[(k,l)] = r
                check += [(k+x,l+y, r+1) for x,y in [(1,0), (-1,0), (0,1) ,(0,-1)]]
        
        m = 0
        for orange in rotting_time:
            if rotting_time[orange] == height*width + 1 : return -1
            m = max(m,rotting_time[orange])
        
        return m


#63ms, 77.36%, and memory decreased .08% to 91.30%, so okay then
class SolutionArray:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        
        fresh_stack = []
        rotten_stack = []
        
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 1:
                    fresh_stack.append((i,j))
                    continue
                if grid[i][j] == 2:
                    rotten_stack.append((i,j))
        
        # replace this with a dict, index by fresh_stack, to save space
        #   I guess it doesn't?
        rotting_time = [[height*width+1 for _ in range(width)] for _ in range(height)]
        
        while rotten_stack:
            i,j = rotten_stack.pop()
            check = [(i+x,j+y, 1) for x,y in [(1,0), (-1,0), (0,1) ,(0,-1)]]
            while check:
                k,l,r = check.pop()
                if not(0<=k<height and 0<=l<width) or (not grid[k][l] == 1) or rotting_time[k][l] <= r: continue
                rotting_time[k][l] = r
                check += [(k+x,l+y, r+1) for x,y in [(1,0), (-1,0), (0,1) ,(0,-1)]]
        
        
        m = 0
        while fresh_stack:
            i,j = fresh_stack.pop()
            if rotting_time[i][j] == height*width+1: return -1
            m = max(m, rotting_time[i][j])
        
        return m