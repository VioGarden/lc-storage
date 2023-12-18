def canCompleteCircuit(gas, cost):
    # if sum of cost < sum of gas: return -1
    # find index of biggest differnce
    
    start_index = 0
    curr = 0
    total = 0
    for i in range(len(gas)):
        total += gas[i] - cost[i]
        curr += gas[i] - cost[i]
        if curr < 0:
            start_index = i + 1
            curr = 0
    
    return start_index if total >= 0 else -1
