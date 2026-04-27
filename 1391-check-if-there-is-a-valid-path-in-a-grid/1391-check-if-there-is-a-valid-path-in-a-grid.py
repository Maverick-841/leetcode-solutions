from collections import deque

class Solution:
    def hasValidPath(self, grid):
        m, n = len(grid), len(grid[0])
        
        # Directions: (dx, dy)
        dirs = {
            1: [(0, -1), (0, 1)],     # left, right
            2: [(-1, 0), (1, 0)],     # up, down
            3: [(0, -1), (1, 0)],     # left, down
            4: [(0, 1), (1, 0)],      # right, down
            5: [(0, -1), (-1, 0)],    # left, up
            6: [(0, 1), (-1, 0)]      # right, up
        }
        
        # Reverse direction check
        def is_connected(from_dir, to_cell):
            return (-from_dir[0], -from_dir[1]) in dirs[to_cell]
        
        visited = set()
        queue = deque([(0, 0)])
        visited.add((0, 0))
        
        while queue:
            x, y = queue.popleft()
            
            if (x, y) == (m-1, n-1):
                return True
            
            for dx, dy in dirs[grid[x][y]]:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < m and 0 <= ny < n:
                    if (nx, ny) not in visited and is_connected((dx, dy), grid[nx][ny]):
                        visited.add((nx, ny))
                        queue.append((nx, ny))
        
        return False