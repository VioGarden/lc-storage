from collections import deque

def bagOfTokensScore(tokens, power):
    tokens.sort()
    if not tokens or power < tokens[0]:
        return 0
    tokens_deque = deque(tokens)
    ans = 0
    highest = 0
    while tokens_deque:
        if power >= tokens_deque[0]:
            curr = tokens_deque.popleft()
            power -= curr
            ans += 1
            highest = max(highest, ans)
        else:
            curr = tokens_deque.pop()
            ans -= 1
            power += curr
    return highest