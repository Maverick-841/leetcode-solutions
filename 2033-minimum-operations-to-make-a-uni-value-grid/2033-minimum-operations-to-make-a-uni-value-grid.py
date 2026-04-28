class Solution:
    def minOperations(self, grid, x):
        arr = []
        
        # Flatten grid
        for row in grid:
            for num in row:
                arr.append(num)
        
        # Check feasibility
        rem = arr[0] % x
        for num in arr:
            if num % x != rem:
                return -1
        
        # Sort
        arr.sort()
        
        # Choose median
        median = arr[len(arr) // 2]
        
        # Count operations
        ops = 0
        for num in arr:
            ops += abs(num - median) // x
        
        return ops