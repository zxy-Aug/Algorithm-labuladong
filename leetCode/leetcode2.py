class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hashmap = {}
        for s in strs:
            code = self.encode(s)
            if code not in hashmap:
                hashmap[code] = []
            hashmap[code].append(s)

        res = []
        for i in hashmap.values():
            res.append(i)
        return res
    def encode(self, str: str) -> str:
        count = [0] * 26
        for s in str:
            delta = ord(s) - ord('a')
            count[delta] += 1
        return ''.join(map(chr, count))

solution = Solution()
result = solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(result)