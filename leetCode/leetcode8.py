# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         left, right = 0, 0
#         window = {}
#         count = 0
#         while right < len(s):
#             c = s[right]
#             right += 1
#             window[c] = window.get(c, 0) + 1
#             sz = len(window)
#             for i in window.keys():
#                 if window[i] == 0:
#                     sz -= 1
#
#             # 判断左侧窗口是否要收缩
#             while any(window[i] > 1 for i in window.keys()):
#                 d = s[left]
#                 left += 1
#                 window[d] -= 1
#                 if window[d] == 0:
#                     sz -= 1
#             count = max(count, sz)
#         return count

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        windows = {}
        left = 0
        right = 0
        res = 0
        while right < len(s):
            c = s[right]
            right += 1
            windows[c] = windows.get(c, 0) + 1

            while windows[c] > 1:
                d = s[left]
                left += 1
                windows[d] = windows.get(d, 0) - 1
            # 在左右窗口更新结束后进行结果的更新
            res = max(res, right - left)
        return res

s = Solution()
res = s.lengthOfLongestSubstring("pwwkew")
print(res)