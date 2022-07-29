image = [[1,1,1],[1,1,0],[1,0,1]]
sr, sc, color = 1,1,2

class Solution:
    # 82ms, 87.22%, memory low variance but still 89.92%
    def floodFillFirstShotOutOfTheBox(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        width = len(image)
        height = len(image[0])
        
        initial_color = image[sr][sc]
        
        stack = [[sr,sc]]
        
        if initial_color == color:
            stack = None
        
        while stack:
            current_pixel = stack.pop()
            cp = current_pixel
            if image[cp[0]][cp[1]] == initial_color:
                image[cp[0]][cp[1]] = color
                if cp[0] > 0:
                    stack.append([cp[0]-1,cp[1]])
                if cp[0] < width-1:
                    stack.append([cp[0]+1,cp[1]])
                if cp[1] > 0:
                    stack.append([cp[0],cp[1]-1])
                if cp[1] < height -1:
                    stack.append([cp[0],cp[1]+1])
        
        return image