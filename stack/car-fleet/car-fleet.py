def carFleet(target, position, speed):
    pair = [[pos, spd] for pos, spd in zip(position, speed)] # pair is 2-D list of [pos, spd]
    stack = [] # init stack
    pair = sorted(pair) # sort pair (by pos)
    pair = pair[::-1] # reverse (so further biggest is first (biggest pos is closest to target))
    for pos, spd in pair: 
        stack.append((target - pos)/spd) # append to stack the time for closest to reach target (decimal div)
        if len(stack) >= 2 and stack[-1] <= stack[-2]: # stack must have at least 2, if deeper down stack greater than newest, pop
            stack.pop()
    return len(stack) # length of stack will be number of fleets



target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]

print(carFleet(target, position, speed))