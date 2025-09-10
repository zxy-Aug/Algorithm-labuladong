# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         hashmap = {}
#         for i in range(len(nums)):
#             if target - nums[i] not in hashmap:
#                 hashmap[target - nums[i]] = i
#
#         for j in range(len(nums)):
#             if nums[j] in hashmap.keys() and j != hashmap.get(nums[j]):
#                 return [j, hashmap.get(nums[j])]

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i in range(len(nums)):
            v = target - nums[i]
            if v in hashmap:
                return [hashmap[v], i]
            hashmap[nums[i]] = i
        return []

s = Solution()
res = s.twoSum(nums=[2, 7, 11, 15], target=9)
print(res)