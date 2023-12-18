def valid(s):
    hashmap = {
        "[" : "]",
        "(" : ")",
        "{" : "}",
    }
    stack = []
    for i in s:
        if i in hashmap:
            stack.append(i)
        else:
            if not stack:
                return False
            x = stack.pop()
            val = hashmap[x] 
            if i != val:
                return False
    return not stack
s = "(]"
print(valid(s))

def calPoints(operations):
    stack = []
    for i in operations:
        if i == '+':
            a = stack[-1]
            b = stack[-2]
            stack.append(a + b)
        elif i == 'D':
            a = stack[-1]
            stack.append(2*a)
        elif i == 'C':
            stack.pop()
        else:
            stack.append(int(i))
    return sum(stack)


ops = ["5","-2","4","C","D","9","+","+"]
print(calPoints(ops))



class MyStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return not self.stack

def genp(n):
    final = []
    curr = []
    
    def rec(outer, inner):
        if outer == inner == n:
            final.append("".join(curr))
            return

        if outer < n:
            curr.append("(")
            rec(outer + 1, inner)
            curr.pop()
        
        if inner < outer:
            curr.append(")")
            rec(outer, inner + 1)
            curr.pop()

    rec(0, 0)
    return final

print(genp(3))

from collections import defaultdict

def findAnagrams(s, p):
    hashmap, final, p_length, s_length = defaultdict(int), [], len(p), len(s)
    if p_length > s_length: 
        return []
    # build hashmap
    for character in p:
        hashmap[character] += 1
    # initial full pass over the window
    for i in range(p_length-1):
        print(i, s[i])
        if s[i] in hashmap: 
            print("--")
            hashmap[s[i]] -= 1
            print(hashmap)
        
    # slide the window with stride 1
    for i in range(-1, s_length - p_length+1):
        if i > -1 and s[i] in hashmap:
            hashmap[s[i]] += 1
        if i+p_length < s_length and s[i+p_length] in hashmap: 
            hashmap[s[i+p_length]] -= 1
            
        # check whether we encountered an anagram
        if all(v == 0 for v in hashmap.values()): 
            final.append(i+1)
            
    return final

s = "cbaebabacd"
p = "abc"
print(findAnagrams(s, p))
