class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        values = dict()
        result = 0

        for row in grid:
            key = tuple(row)
            if key in values:
                values[key] += 1
            else:
                values[key] = 1
        for c in range(len(grid)):
            key = tuple(grid[r][c] for r in range(len(grid)))
            if key in values:
                result += values[key]
        return result
            
