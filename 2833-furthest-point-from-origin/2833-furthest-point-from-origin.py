class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        x,y,z = 0,0,0
        for i in moves:
            if i == "R":
                x += 1
            elif i == "L":
                y += 1
            else:
                z += 1
        return abs(x - y) + z