from collections import deque
# time limit exceeded
class Solution(object):
    def predictPartyVictory(self, senate):

        n = len(senate) - 1

        queueR, queueD = deque(), deque()
        for i in range(len(senate)):
            if senate[i] == "R":
                queueR.append(i)
            else:
                queueD.append(i)
        
        while queueR and queueD:
            qr = queueR.popleft()
            qd = queueD.popleft()
            n += 1
            if qr < qd:
                queueR.append(n)
            else:
                queueD.append(n)

        if queueR:
            return "Radiant"
        return "Dire"