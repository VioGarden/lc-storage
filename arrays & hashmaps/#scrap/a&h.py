def isSubsequence(s, t):
    if not s:
        return True
    if not t:
        return False
    tpoint = 0
    spoint = 0
    while tpoint < len(t):
        if t[tpoint] == s[spoint]:
            spoint += 1
        if spoint >= len(s):
            return True
        tpoint += 1
    return False

def lengthOfLastWord(s):
    lists = s.split()
    if not lists:
        return 0
    return len(lists[-1])

def longestCommonPrefix(strs):
    prefix = ""
    smallest = min(strs)
    valid = True
    i = 0
    while i < len(smallest):
        letter = smallest[i]
        for j in strs:
            if j[i] != letter:
                valid = False
        if valid == False:
            break
        prefix += letter
        i += 1
    return prefix

print(longestCommonPrefix(["dog","racecar","car"]))

def pascals(n):
    final = []
    final.append([1])
    if n == 1:
        return final
    final.append([1,1])
    if n == 2:
        return final
    n -= 2
    start = [1, 1]
    while n > 0:
        start = [1] + start + [1]
        new = []
        for i in range(len(start) - 1):
            curr = start[i] + start[i + 1]
            new.append(curr)
        new[0] = 1
        new[-1] = 1
        start = new
        n -= 1
        final.append(new)
    return final
    
print(pascals(5))

def removeElement(nums, val):
    left = 0
    right = len(nums) - 1
    k = 0
    while left < right:
        while nums[right] == val:
            nums[right] = '_'
            right -= 1
            k += 1
        if nums[left] == val:
            nums[left], nums[right] = nums[right], nums[left]
            nums[right] = '_'
            right -= 1
            k += 1
        left += 1
    print(len(nums) - right - 1)
    return k

nums = [0,1,2,2,3,0,4,2]
val = 2
print(removeElement(nums, val))
print(nums)


def numUniqueEmails(emails):
    s = set()
    for i in emails:
        final = ""
        count = 0
        for j in i:
            if j == '@' or j == '+':
                break
            if j != '.':
                final += j
            count += 1
        while i[count] != '@':
            count += 1
        final += i[count:]
        if final not in s:
            s.add(final)
    return len(s)

emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
print(numUniqueEmails(emails)) 

def canplace(pots, count):
    spaces = 0
    for i in range(len(pots)):
        left = i - 1
        right = i + 1
        if i == 0:
            left = i
        if i == len(pots) - 1:
            right = i
        
        if pots[left] == 0 and pots[right] == 0:
            pots[i] = 1
            spaces += 1
    return spaces >= count

flowerbed = [1,0,0,0,0,0,1]
n = 2
print(canplace(flowerbed, n))

        
def majorityElement(nums):
    hashmap = {}
    for i in nums:
        hashmap[i] = 1 + hashmap.get(i, 0)

    one, two = 0, 0
    for key, val in hashmap.items():
        if val > two:
            two = val
            one = key
    return one


nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))

def nextGreaterElement(n1, n2):
    hashmap = {}
    for i in range(len(n2)):
        # curr is next element in n2
        curr = i + 1
        # val to compare
        val = n2[i]
        while curr < len(n2) and val > n2[curr]:
            curr += 1
        if curr == len(n2):
            temp = -1
        else:
            temp = n2[curr]
        # key: element in nums2 | val: next greatest
        hashmap[n2[i]] = temp
    print(hashmap)

    final = []
    for i in n1:
        value = hashmap[i]
        final.append(value)

    return final


nums1 = [2,4]
nums2 = [1,2,3,4]
print(nextGreaterElement(nums1, nums2))


def findPivotIndex(nums):
    left = 0
    right = 0
    for i in range(1, len(nums)):
        right += nums[i]
    i = 0
    while i < len(nums) - 1:
        if left == right:
            return i
        i += 1
        left += nums[i - 1]
        right -= nums[i]
    if left == right:
        return i
    return -1 

nums = [2, -1, 1]
print(findPivotIndex(nums))


from collections import defaultdict
def word(pattern, s):
    hashmap = defaultdict(list)
    for i in range(len(pattern)):
        hashmap[pattern[i]].append(i)
    
    words = s.split()
    identicals = list(hashmap.values())
    for i in identicals:
        comparison = words[i[0]]
        for j in i:
            if words[j] != comparison:
                return False
    return True

pattern = "aaaa"
s = "dog cat cat dog"
print(word(pattern, s))


def sortColors(nums):
    right = len(nums) - 1
    left = right - 1
    curr = 0
    while curr <= left:
        if nums[curr] == 2:
            nums[curr], nums[right] = nums[right], nums[curr]
            right -= 1
            left -= 1
        elif nums[curr] == 0:
            curr += 1
        else:
            nums[curr], nums[left] = nums[left], nums[curr]
            left -= 1
    return
nums = [2,0,2,1,1,2,2,0]
sortColors(nums)
print(nums)


def brick(wall):
    rows = len(wall)
    if sum(wall[0]) == 1:
        return rows
    hashmap = {}

    for piece in wall:
        i = 0
        for j in range(len(piece) - 1):
            i += piece[j]
            hashmap[i] = 1 + hashmap.get(i, 0)
    red = list(hashmap.values())

    start = rows - red[0]
    for r in red:
        start = min(start, rows - r)
    return start

wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
print(brick(wall))

def maxProfit(prices):
    if not prices:
        return 0
    i = 1
    profit = 0
    curr = prices[0]
    while i < len(prices):
        if prices[i] < curr:
            curr = prices[i]
        else:
            gained = prices[i] - curr
            profit += gained
            curr = prices[i]
        i += 1
    return profit

prices = []
print(maxProfit(prices))

def maxProfit(prices):
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += (prices[i] - prices[i - 1])
    return profit

from collections import defaultdict
def countPalindromicSubsequence(s):
    hashmap = defaultdict(list)
    for i in range(len(s)):
        hashmap[s[i]].append(i)
    possible = list(hashmap.values())
    total = 0
    for j in possible:
        if len(j) > 1:
            small = min(j)
            large = max(j)
            sss = set()
            for k in range(small + 1, large):
                sss.add(s[k])
            total += len(sss)
    return total

s = "aaaaabaaab"
print(countPalindromicSubsequence(s))


def firstMissingPositive(nums):
    lowest_pos = min(nums)
    highest_pos = max(nums)
    if highest_pos < 1:
        return 1
    if lowest_pos > 1:
        return 1
    
    lowest_pos = highest_pos
    for i in nums:
        if i < 1:
            continue
        if i < lowest_pos:
            lowest_pos = i
    nums = set(nums)
    while (lowest_pos + 1) in nums:
        lowest_pos += 1
    
    return (lowest_pos + 1)

nums = [1,2,3,4,7,8,9,11,12]
print(firstMissingPositive(nums))

def findAnagrams(s, p):
    hashmap = {}
    for i in p:
        hashmap[i] = 1 + hashmap.get(i, 0)
    
    final = []
    for j in range(len(s) - len(p) + 1):
        hashmap2 = {}
        for k in range(len(p)):
            index = j + k
            hashmap2[s[index]] = 1 + hashmap2.get(s[index], 0)
        if hashmap == hashmap2:
            final.append(j)
    return final

s = "abab"
p = "ab"
print(findAnagrams(s, p))

def dna(s):
    s1 = set()
    final = set()
    x = len(s) - 10 + 1
    for i in range(x):
        snippet = s[i:i+10]
        if snippet in s1:
            if snippet not in final:
                final.add(snippet)
        s1.add(snippet)
    b = list(final)
    return b

a = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print(dna(a))

def strStr(haystack, needle):
    x = len(haystack) - len(needle) + 1
    for i in range(x):
        temp = haystack[i: i + len(needle)]
        if needle == temp:
            return i
    return -1

haystack = "leetcode"
needle = "leeto"
print(strStr(haystack, needle))