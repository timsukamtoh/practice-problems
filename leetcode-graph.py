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


# leetcode 695. Max Area of Island
def maxAreaOfIsland(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    max_area = 0
    visited = set()
    ROW, COL = len(grid), len(grid[0])

    def dfs(r, c):
        if (
            r < 0
            or c < 0
            or r >= ROW
            or c >= COL
            or grid[r][c] == 0
            or (r, c) in visited
        ):
            return 0

        visited.add((r, c))

        area = 1

        area += dfs(r + 1, c)
        area += dfs(r - 1, c)
        area += dfs(r, c + 1)
        area += dfs(r, c - 1)

        return area

    for r in range(ROW):
        for c in range(COL):
            if grid[r][c] == 1 and (r, c) not in visited:
                max_area = max(max_area, dfs(r, c))

    return max_area


# leetcode 133. Clone Graph
def cloneGraph(self, node):
    """
    :type node: Node
    :rtype: Node
    """
    if not node:
        return node

    nodes = {}
    visited = set()
    queue = collections.deque([node])

    while queue:
        n = queue.popleft()

        if n in visited:
            continue
        visited.add(n)

        if n not in nodes:
            nodes[n] = Node(n.val)

        for neigh in n.neighbors:
            if neigh not in nodes:
                nodes[neigh] = Node(neigh.val)
            nodes[n].neighbors.append(nodes[neigh])
            queue.append(neigh)

    return nodes[node]


# leetcode: Islands and Treasure / Walls and Gates
def islandsAndTreasure(self, grid: List[List[int]]) -> None:

    ROW, COL = len(grid), len(grid[0])

    def dfs(r: int, c: int, step: int) -> None:
        if r < 0 or c < 0 or r >= ROW or c >= COL or grid[r][c] < step:
            return

        grid[r][c] = step
        dfs(r + 1, c, step + 1)
        dfs(r - 1, c, step + 1)
        dfs(r, c + 1, step + 1)
        dfs(r, c - 1, step + 1)

    for r in range(ROW):
        for c in range(COL):
            if grid[r][c] == 0:
                dfs(r, c, 0)


# leetcode 994: Rotting Oranges
def orangesRotting(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    freshcount = 0
    ROW, COL = len(grid), len(grid[0])
    queue = collections.deque([])

    for r in range(ROW):
        for c in range(COL):
            if grid[r][c] == 2:
                queue.append((r, c))
            if grid[r][c] == 1:
                freshcount += 1

    minutes = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue and freshcount > 0:
        minutes += 1

        for i in range(len(queue)):
            curr = queue.popleft()

        for direct in directions:
            r = curr[0] + direct[0]
            c = curr[1] + direct[1]
            if r >= 0 and c >= 0 and r < ROW and c < COL and grid[r][c] == 1:
                grid[r][c] = 2
                freshcount -= 1

                queue.append((r, c))

    if freshcount == 0:
        return minutes
    else:
        return -1


# leetcode 417: Pacific Atlantic Water Flow
def pacificAtlantic(self, heights):
    """
    :type heights: List[List[int]]
    :rtype: List[List[int]]
    """
    result = []
    ROW, COL = len(heights), len(heights[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def dfs_a(r, c):
        if r < 0 or c < 0:
            return True
        else:
            for direct in directions:
                curr = heights[r][c]
                row, col = r + direct[0], c + direct[1]
                if row < ROW and col < COL and curr >= heights[row][col]:
                    return dfs_a(row, col)
        return False

    def dfs_p(r, c):
        if r > 0 or c > 0:
            return True
        else:
            for direct in directions:
                curr = heights[r][c]
                row, col = r + direct[0], c + direct[1]
                if row >= 0 and col >= 0 and curr >= heights[row][col]:
                    return dfs_a(row, col)
        return False

    for r in range(ROW):
        for c in range(COL):
            if dfs_a(r, c) and dfs_p(r, c):
                result.append([r, c])

    return result
