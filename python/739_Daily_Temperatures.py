class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        
        for idx, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                smaller_idx = stack.pop()
                answer[smaller_idx] = idx - smaller_idx
            stack.append(idx)
        
        return answer
