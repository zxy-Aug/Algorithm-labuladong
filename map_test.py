# a = {"1": 0, "2": 2, "3": 1}
# for i in a.keys():
#     print(i)
# p = 1
# print(a)
# a[4] = []
# for i in range(1, 5):
#     a[4].append(i)
# result = []
# for a_ in a.values():
#     result.append(a_)
# print(result)
# print(a.values())
# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# def encode(str):
#     a = [0] * 26
#     for s in str:
#         delta = ord(s) - ord('a')
#         a[delta] += 1
#     return ''.join(map(chr, a))
#
# hashmap = {}
# for s in strs:
#     code = encode(s)
#     if code not in hashmap:
#         hashmap[code] = []
#     hashmap[code].append(s)
#
# res = []
# for i in hashmap.values():
#     res.append(i)
# print(res)
# a = [[1,2,3], [0,9,9], [0,1]]
# for arr in a:
#     print(arr)
# strs = "cmsocms"
# print(strs[4])
# print(len(strs))
s = "banana"
s.sort(key=lambda x:x[1])