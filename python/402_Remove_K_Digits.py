class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for n in num:
            while stack and stack[-1] > n and k > 0:
                stack.pop()
                k -= 1
            # skip leading "0"
            if not stack and n == '0':
                continue
            stack.append(n)

        # dealing with remaining k
        while k > 0 and stack:
            stack.pop()
            k -= 1
        
        return ''.join(stack) if stack else '0'
