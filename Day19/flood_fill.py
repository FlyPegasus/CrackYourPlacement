from queue import Queue
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        c = image[sr][sc]
        def trav(i, j, color):
            nonlocal image
            nonlocal c
            if i < 0 or i >= len(image) or j < 0 or j >= len(image[i]) or image[i][j] != c or image[i][j] == color:
                return
            #print(i, j)
            image[i][j] = color
            trav(i + 1, j, color)
            trav(i, j + 1, color)
            trav(i - 1, j, color)
            trav(i, j - 1, color)
        trav(sr, sc, color)
        return image