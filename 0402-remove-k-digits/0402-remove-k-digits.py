class Solution(object):
    def removeKdigits(self, num, k):
        stack = []
        for nu in num:
            while k and stack and stack[-1] > nu:
                stack.pop()
                k -= 1
            stack.append(nu)

        while k > 0:
            stack.pop()
            k -= 1
        result = "".join(stack).lstrip("0")
        return result if result else "0"
