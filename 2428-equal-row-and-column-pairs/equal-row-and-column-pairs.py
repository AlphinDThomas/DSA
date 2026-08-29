class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        gridstrs = []

        for i in grid:
            substring = ""
            for j in i :
                substring+=str(j) + ","
            gridstrs.append(substring)
        print(gridstrs)
        transpose = []

        for j in range(len(grid[0])):
            row = []
            for i in range(len(grid)):
                row.append(grid[i][j])
            transpose.append(row)
        print(transpose)

        transposestrs = []
        for i in transpose:
            substring = ""
            for j in i:
                substring+=str(j) + ","
            transposestrs.append(substring)
        print(transposestrs)

        count = 0
        for i in range(len(transposestrs)):
            for j in range(len(transposestrs)):
                if (gridstrs[i]) == (transposestrs[j]):
                    count+=1
        return count