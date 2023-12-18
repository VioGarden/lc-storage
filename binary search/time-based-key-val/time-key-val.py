class TimeMap(object):

    def __init__(self):
        self.store = {} # key : list of [val, timestamp]

    def set(self, key, value, timestamp):
        if key not in self.store: # if key does not exist in store
            self.store[key] = []
        self.store[key].append([value, timestamp]) # append a pair of values
        

    def get(self, key, timestamp):
        result = "" # if key doesn't exist, return empty string
        values = self.store.get(key, [])  # pulling from hasmap, get all items of the key, and if none, replace an empty list
        left, right = 0, len(values) - 1 # initialize pointerts
        while left <= right: # while they don't cross
            m = (left + right)//2 # mid index
            if values[m][1] <= timestamp: # if for the values[m][1] | m : index | 1 is second index of m, which is the timestamp
                result = values[m][0] # result is the value if found (if value is before inputted time)
                left = m + 1 # change left pointer
            else: # if timestamp is to small, nothing will be found
                right = m - 1 # change right pointer
        return result
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)