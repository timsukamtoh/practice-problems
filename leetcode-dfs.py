# leetcode 200. Number of Islands
def numIslands(self, grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    islands = 0
    visited = set()
    ROW, COL = len(grid), len(grid[0])

    def dfs(r, c):
        if (
            r < 0
            or c < 0
            or r >= ROW
            or c >= COL
            or grid[r][c] == "0"
            or (r, c) in visited
        ):
            return
        else:
            visited.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

    for r in range(ROW):
        for c in range(COL):
            if grid[r][c] == "1" and (r, c) not in visited:
                islands += 1
                dfs(r, c)

    return islands
