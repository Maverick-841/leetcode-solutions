class Solution(object):
    def prefixesDivBy5(self, nums):
        result = []
        num  = 0
        for bits in nums:
            num = (num * 2 + bits) % 5
            if num == 0:
                result.append(True)
            else:
                result.append(False)
        return result        