from collections import defaultdict

def accountsMerge(accounts):
    """
    :type accounts: List[List[str]]
    :rtype: List[List[str]]
    """

    names = set()

    names_dictionary = defaultdict(set) # maps name to which indexes in bucket have their name

    bucket = [] # holds the emails

    for index, value in enumerate(accounts):
        current_name = value[0]
        names_dictionary[current_name].add(index)
        bucket.append(set(value[1:]))

    for index2, value2 in enumerate(accounts):
        current_name = value2[0]
        for email in value2[1:]:
            for j in names_dictionary[current_name]:
                if j == index2:
                    continue
                if email in bucket[j]:
                    bucket[index2].update(bucket[j])
                    bucket[j] = set()
    
    ans = []

    for index in range(len(accounts)):
        if not bucket[index]:
            continue
        temp = []
        name = accounts[index][0]
        temp.append(name)
        temp.extend(sorted(bucket[index]))
        ans.append(temp)

    return ans