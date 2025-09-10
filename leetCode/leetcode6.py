class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = self.nSumTaeget(nums, 3, 0, 0)
        return res

    def nSumTaeget(self, nums, n, start, target):
        """
        :param nums: 数组
        :param n: n个数之和
        :param start: 从数组的哪个位置开始
        :param target: n个数之和等于几
        :return: 返回所有符合条件的组合
        """
        sz = len(nums)
        res = []
        if (n < 2) or (start > sz):
            return res
        if n == 2:
            left, right = start, len(nums) - 1
            while left < right:
                v_l, v_r = nums[left], nums[right]
                sum_val = v_l + v_r
                if sum_val < target:
                    while left < right and nums[left] == v_l:
                        left += 1
                elif sum_val > target:
                    while left < right and nums[right] == v_r:
                        right -= 1
                else:
                    res.append([v_l, v_r])
                    while left < right and nums[left] == v_l:
                        left += 1
                    while left < right and nums[right] == v_r:
                        right -= 1
        else:
            for i in range(start, sz):
                if i > start and nums[i] == nums[i-1]:
                    continue
                sub = self.nSumTaeget(nums, n-1, i+1, target-nums[i])
                for arr in sub:
                    arr.append(nums[i])
                    res.append(arr)
        return res

s = Solution()
a = [-1,0,1,2,-1,-4]
r = s.threeSum(a)
print(r)