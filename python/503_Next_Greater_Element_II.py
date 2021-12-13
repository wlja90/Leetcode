# method 01 
# class Solution:
#     def nextGreaterElements(self, nums: List[int]) -> List[int]:
#         new_nums = nums + nums
#         stack = []
#         results = [-1] * len(new_nums)
        
#         for idx, n in enumerate(new_nums):
#             while stack and stack[-1][1] < n:
#                 smaller_idx, smaller_n = stack.pop()
#                 results[smaller_idx] = n 
#             stack.append((idx, n))
            
#         return results[:len(nums)]
        
        
        
# method 02
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        results = [-1] * len(nums)
        stack = []
        loop = 1
        
        while loop < 3:
            for idx, n in enumerate(nums):
                while stack and stack[-1][1] < n:
                    smaller_idx, smaller_n = stack.pop()
                    results[smaller_idx] = n
                stack.append((idx, n))
            loop += 1
        
        return results
