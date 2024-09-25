# leetcode 200. Number of Islands
def numIslands(self, grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    num_islands = 0
    visited = set()
    ROW, COL = len(grid), len(grid[0])

    def dfs(r, c):
        if (
            r < 0
            or c < 0
            or r >= ROW
            or c >= COL
            or (r, c) in visited
            or grid[r][c] == "0"
        ):
            return

        visited.add((r, c))
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(ROW):
        for c in range(COL):
            if grid[r][c] == "1" and (r, c) not in visited:
                num_islands += 1
                dfs(r, c)

    return num_islands


#
def maxAreaOfIsland(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    max_area = 0
    visited = set()
    ROW, COL = len(grid), len(grid[0])

    def dfs(r, c, curr_area):
        if (
            r < 0
            or c < 0
            or r >= ROW
            or c >= COL
            or grid[r][c] == 0
            or (r, c) in visited
        ):
            print("exit dfs")
            return
        else:
            visited.add((r, c))
            max_area = max(max_area, curr_area + 1)
            dfs(r + 1, c, curr_area + 1)
            dfs(r - 1, c, curr_area + 1)
            dfs(r, c + 1, curr_area + 1)
            dfs(r, c - 1, curr_area + 1)

    for r in range(ROW):
        for c in range(COL):
            if grid[r][c] == 1 and (r, c) not in visited:
                print("enter dfs at ")
                dfs(r, c, 0)
    return max_area
