class Solution:

    def valid(self, i, j, m, n) : 

        return 0 <=i < m and 0 <= j < n

    def maxAreaOfIslandBFSvisitedSet(self, grid: List[List[int]]) -> int:

        island_count = 0
        max_area = 0

        m = len(grid)

        n = len(grid[0])

        area = 0

        for i in range(m) :

            for j in range(n) : 

                if grid[i][j] == 1 :

                    # Island is found

                    island_count += 1

                    area = 0

                    queue = deque()

                    visited = set()

                    queue.append((i,j))

                    grid[i][j] = 0

                    visited.add((i,j))

                    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

                    while queue : 

                        i, j = queue.popleft()

                        for dx, dy in directions : 

                            x, y = i + dx, j + dy

                            if self.valid(x,y, m, n) and  (x,y) not in visited and grid[x][y] == 1 :

                                queue.append((x, y))

                                visited.add((x,y))

                        grid[i][j] = 0

                        area += 1

                max_area = max(area, max_area)                         
                                        
        return max_area 

    def maxAreaOfIslandNoSet(self, grid: List[List[int]]) -> int:

        island_count = 0
        max_area = 0

        m = len(grid)

        n = len(grid[0])

        area = 0

        for i in range(m) :

            for j in range(n) : 

                if grid[i][j] == 1 :

                    # Island is found

                    island_count += 1

                    area = 0

                    queue = deque()

                    # visited = set()

                    queue.append((i,j))

                    grid[i][j] = 0

                    # visited.add((i,j))

                    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

                    while queue : 

                        i, j = queue.popleft()

                        for dx, dy in directions : 

                            x, y = i + dx, j + dy

                            # if self.valid(x,y, m, n) and  (x,y) not in visited and grid[x][y] == 1 :

                            if self.valid(x,y, m, n) and grid[x][y] == 1 :

                                queue.append((x, y))
                                grid[x][y] = 0

                                # visited.add((x,y))

                        # grid[p][q] = 0

                        area += 1

                max_area = max(area, max_area)                         
                                        
        return max_area 

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        # return self.maxAreaOfIslandBFSvisitedSet(grid)

        return self.maxAreaOfIslandNoSet(grid)
