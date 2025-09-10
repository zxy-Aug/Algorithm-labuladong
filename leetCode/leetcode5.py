# class Solution:
#     def maxArea(self, height: list[int]) -> int:
#         res = 0
#         for slow in range(len(height)):
#             for fast in range(slow+1, len(height)):
#                 h = min(height[slow], height[fast])
#                 cur_v = (fast - slow) * h
#                 res = max(cur_v, res)
#         return res

class Solution:
    def maxArea(self, height: list[int]) -> int:
        res = 0
        left, right = 0, len(height)-1
        while left < right:
            h = min(height[left], height[right])
            cur_v = (right - left) * h
            res = max(cur_v, res)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return res

s = Solution()
a = [1,8,6,2,5,4,8,3,7]
res = s.maxArea(a)
print(res)