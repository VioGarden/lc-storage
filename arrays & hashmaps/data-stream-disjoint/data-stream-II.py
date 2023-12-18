class SummaryRanges(object):
    def __init__(self):
        self.intervals = []

    def addNum(self, val):
        left, right = 0, len(self.intervals) - 1
        while left <= right:
            mid = (left + right) // 2
            curr = self.intervals[mid]
            if curr[0] <= val <= curr[1]: 
                return
            elif val < curr[0]:
                right = mid - 1
            else:
                left = mid + 1
        pos = left
        self.intervals.insert(pos, [val, val])
        if pos + 1 < len(self.intervals) and val + 1 == self.intervals[pos+1][0]:
            self.intervals[pos][1] = self.intervals[pos+1][1]
            del self.intervals[pos+1]
        if pos - 1 >= 0 and val - 1 == self.intervals[pos-1][1]:
            self.intervals[pos-1][1] = self.intervals[pos][1]
            del self.intervals[pos]

    def getIntervals(self):
        return self.intervals