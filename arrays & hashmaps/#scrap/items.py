# dictionary.items()  -->  returns [(key, value), (key, value), (key, value)]
# returns key value pairs as tuples in a list format
# ie | for k, v in dictionary.items():


# print(chr(ord("a")))
# print(ord("a"))

# hashSet = {1:2,4:3,2:34,3:5,2:99}
# print(hashSet.values())

# from collections import defaultdict

# hashSet = defaultdict(list)

# hashSet[0].append(3)
# hashSet["fit"].append(4)
# hashSet["b4"].append(66)

# print(len(hashSet))

# x = set()
# x.add(4)
# print(x)

# x = {"the", "one"}
# x.add("hello")
# x.add("the")
# print(x)

# from collections import defaultdict
# x = defaultdict(list)
# x["3"].append(5)
# x["3"].append(6)
# x["3"].append([4,5])
# x["3"].append({4,5})
# print(x)

# strs = "6#violet10#evergarden3#the5#movie"
# i = 8
# j = 10
# print(int(strs[i:j]))



string = "geeks quiz practice code"
# reversing words in a given string
s = string.split()[::-1]
print(s)
