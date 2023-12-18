class SummaryRanges(object):

    def __init__(self):
        self.nums = []

    def addNum(self, value):
        self.nums.append(value)
        

    def getIntervals(self):
        final = []
        dup_set = set(self.nums)
        while dup_set:
            lowest = min(dup_set)
            dup_set.remove(lowest)
            highest = lowest
            while dup_set and (highest + 1) in dup_set:
                dup_set.remove(highest + 1)
                highest += 1
            final.append([lowest, highest])

        return final