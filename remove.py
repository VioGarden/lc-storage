f = open("thing.txt")

test = f.read()
f.close()

words = test.split()
# print(words)

AB = """
"""

def remove(thing):
    words2 = thing.split()
    for i in words2:
        if i in words[:]:
            words.remove(i)
        else:
            print(i, "aaa")

remove(AB)

hi = " ".join([i for i in words])

f = open("thing.txt", "w")
f.write(hi)
f.close()



