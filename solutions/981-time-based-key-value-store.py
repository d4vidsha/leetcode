from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        l = 0
        r = len(self.store[key]) - 1
        while l <= r:
            m = l + (r - l) // 2
            if self.store[key][m][1] < timestamp:
                res = self.store[key][m][0]
                l = m + 1
            elif self.store[key][m][1] > timestamp:
                r = m - 1
            else:
                res = self.store[key][m][0]
                break
        return res

if __name__ == "__main__":
    obj = TimeMap()
    obj.set("foo", "bar", 1)
    obj.get("foo", 1)
    obj.get("foo", 3)
    obj.set("foo", "bar2", 4)
    obj.get("foo", 4)
    obj.get("foo", 5)
