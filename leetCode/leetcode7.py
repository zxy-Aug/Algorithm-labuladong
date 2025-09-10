class Solution:
    def trap(self, height: list[int]) -> int:
        sz = len(height)
        res = 0
        l_max = [0] * sz
        r_max = [0] * sz
        l_max[0] = height[0]
        r_max[sz-1] = height[sz-1]
        for i in range(1, sz-1):
            l_max[i] = max(height[i], l_max[i-1])
        for i in range(sz-2, 0, -1):
            r_max[i] = max(height[i], r_max[i+1])
        for i in range(1, sz-1):
            res += min(l_max[i], r_max[i]) - height[i]

        return res

s = Solution()
a = [4,2,0,3,2,5]
r = s.trap(a)
print(r)