from collections import deque

class Solution:
    def predictPartyVictory(self, senate):

        n = len(senate)

        queueR = [i for i in range(len(senate)) if senate[i]=='R']
        queueD = [j for j in range(len(senate)) if senate[j]=='D']

        queueD = deque(queueD)
        queueR = deque(queueR)

        while queueR and queueD:
            qr = queueR.popleft()
            qd = queueD.popleft()

            if qr < qd:
                queueR.append(n + qr)
            else:
                queueD.append(n + qd)

        return "Radiant" if queueR else "Dire"