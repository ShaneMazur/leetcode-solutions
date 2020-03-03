'''
Problem:
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island
is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Ex.
Input:
11110
11010
11000
00000

Output: 1

Input:
11000
11000
00100
00011

Output: 3

'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        r,c = len(grid),len(grid[0])
        searched = set()
        def get_island(x,y):
            if (x,y) not in searched and 0 <= x and x < c and 0 <= y and y < r and grid[y][x] == "1":
                searched.add((x,y))
                get_island(x+1,y)
                get_island(x-1,y)
                get_island(x,y+1)
                get_island(x,y-1)

        pos = (0,0)
        islands = 0
        while len(searched) < c*r:
            # print(pos)
            if pos not in searched:
                if grid[pos[1]][pos[0]] == "0":
                    searched.add(pos)
                else:
                    get_island(pos[0],pos[1])
                    islands += 1
            pos = (0,pos[1]+1) if pos[0]+1 == c else (pos[0]+1,pos[1])

        return islands