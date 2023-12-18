from collections import defaultdict

class SnapshotArray:

    def __init__(self, length: int):
        self.arr = defaultdict(list)
        self.snap_count = 0
        

    def set(self, index: int, val: int) -> None:
        if self.arr[index] and self.arr[index][-1][0] == self.snap_count:
            self.arr[index][-1][1] = val
            return
        self.arr[index].append([self.snap_count, val])

    def snap(self) -> int:
        self.snap_count += 1
        return self.snap_count - 1
        

    def get(self, index: int, snap_id: int) -> int:
        arr = self.arr[index]
        left, right, ans = 0, len(arr) - 1, -1
        while left <= right:
            mid = (left + right)//2
            if arr[mid][0] <= snap_id:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        if ans == -1:
            return 0
        return arr[ans][1]
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)