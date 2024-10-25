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


# leetcode:
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
