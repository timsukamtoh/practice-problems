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
    fresh = 0
    ROW, COL = len(grid), len(grid[0])
    queue = collections.deque([])

    for r in range(ROW):
        for c in range(COL):
            if grid[r][c] == 2:
                queue.append((r, c))
            if grid[r][c] == 1:
                fresh += 1

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    minutes = 0

    while queue and fresh > 0:
        size = len(queue)
        minutes += 1

        for i in range(size):
            curr = queue.popleft()
            row, col = curr[0], curr[1]

            for direct in directions:
                r = row + direct[0]
                c = col + direct[1]

                if r >= 0 and c >= 0 and r < ROW and c < COL and grid[r][c] == 1:
                    grid[r][c] = 2
                    fresh -= 1

                    queue.append((r, c))

    if fresh == 0:
        return minutes
    else:
        return -1
