class TimeMap:

    def __init__(self) -> None:
        self.map: dict[str, list[tuple[int,str]]] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.map:
            self.map[key].append((timestamp, value))
        else:
            self.map[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""

        # binary search to find correct timestamp
        left = 0
        right = len(self.map[key]) - 1
        result = ""

        while (left <= right):
            middle = (left + right) // 2
            currTimestamp, currValue = self.map[key][middle]

            # check left, most recent OR equal to timestamp
            if (currTimestamp <= timestamp):
                result = currValue
                left = middle + 1
            
            # check right
            else:
                right = middle - 1
        
        return result