# class Solution:
#     def longestConsecutive(self, nums: list[int]) -> int:
#         dict = {}
#         nums.sort()
#         count = 0
#         for i in range(len(nums)-1):
#             if nums[i+1] - nums[i] == 0:
#                 count += 1
#                 continue
#             elif nums[i+1] - nums[i] == 1:
#                 continue
#             return i+1-count
#         return len(nums) - count
#
# solution = Solution()
# nums = [9,1,4,7,3,-1,0,5,8,-1,6]
# a = solution.longestConsecutive(nums)
# print(nums)
# print(a)

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        set_nums = set(nums)
        res = 0
        for num in set_nums:
            # 查找连续序列的第一个元素
            if num-1 in set_nums:
                continue

            # 从第一个元素往后面遍历，并进行计数
            cur_num = num
            count = 1
            while cur_num + 1 in set_nums:
                cur_num += 1
                count += 1

            res = max(count, res)
        return res

solution = Solution()
nums = [9,1,4,7,3,-1,0,5,8,-1,6]
a = solution.longestConsecutive(nums)
print(nums)
print(a)