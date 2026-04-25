import bisect

class Solution(object):
    def maxDistance(self, side, points, k):

        def convert(x, y):
            if y == 0:
                return x
            elif x == side:
                return side + y
            elif y == side:
                return 3 * side - x
            else:
                return 4 * side - y

        pos = sorted(convert(x, y) for x, y in points)
        n = len(pos)
        per = 4 * side

        # duplicate for circular
        pos = pos + [x + per for x in pos]

        def can(d):
            for i in range(n):
                count = 1
                last = pos[i]
                idx = i

                while count < k:
                    # jump using binary search
                    nxt = bisect.bisect_left(pos, last + d, idx + 1, i + n)
                    if nxt == i + n:
                        break
                    last = pos[nxt]
                    idx = nxt
                    count += 1

                if count == k:
                    # circular check
                    if last - pos[i] <= per - d:
                        return True
            return False

        left, right = 0, per
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            if can(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans