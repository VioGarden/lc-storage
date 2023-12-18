from collections import Counter

def permuteUnique(nums):
    final = []
    def backtrack(arr, hashmap):
        if len(arr) == len(nums):
            final.append(arr[:])
        else:
            for i in hashmap:
                if hashmap[i] > 0:
                    arr.append(i)
                    hashmap[i] -= 1
                    backtrack(arr, hashmap)
                    arr.pop()
                    hashmap[i] += 1

    backtrack([], Counter(nums))
    # Counter {element: count, element2: count...}
    return final