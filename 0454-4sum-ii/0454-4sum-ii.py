class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        count_ab = {}

        # Step 1: Store sums of nums1 and nums2
        for a in nums1:
            for b in nums2:
                s = a + b
                count_ab[s] = count_ab.get(s, 0) + 1

        # Step 2: Check sums of nums3 and nums4
        result = 0
        for c in nums3:
            for d in nums4:
                target = -(c + d)
                if target in count_ab:
                    result += count_ab[target]

        return result