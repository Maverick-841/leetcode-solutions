class Solution(object):
    def findMinArrowShots(self, points):
        if not points:
            return 0

        # Step 1: Sort by ending coordinate
        points.sort(key=lambda x: x[1])

        arrows = 1
        end = points[0][1]

        # Step 2: Traverse
        for i in range(1, len(points)):
            if points[i][0] > end:
                arrows += 1
                end = points[i][1]

        return arrows