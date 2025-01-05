
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        visited = set()
        for x in range(cols):
            for y in range(rows):
                if matrix[y][x] != 0 or (x, y) in visited:
                    continue
                for i in range(rows):
                    if matrix[i][x] != 0:
                        matrix[i][x] = 0
                        visited.add((x, i))
                for i in range(cols):
                    if matrix[y][i] != 0:
                        matrix[y][i] = 0
                        visited.add((i, y))
