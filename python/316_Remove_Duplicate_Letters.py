from collections import Counter
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = Counter(s)
        seen = set()
        stack = []
        
        for letter in s:
            counter[letter] -= 1
            
            if letter in seen:
                continue
            
            while stack and stack[-1] > letter and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            
            stack.append(letter)
            seen.add(letter)
            
        return "".join(stack)
