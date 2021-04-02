# Complexity
# Time Complexity: O(1)\mathcal{O}(1)O(1), as we explained in intuition.
# Space Complexity: O(N)\mathcal{O}(N)O(N), where NNN is the size of the moving window.    

class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.queue = deque()
        self.window_sum = 0
        self.cnt = 0

    def next(self, val: int) -> float:
        # size, queue = self.size, self.queue
        self.cnt += 1
        # calculate the new sum by shifting
        self.queue.append(val)
        if self.cnt > self.size:
            tail = self.queue.popleft()
        else:
            tail = 0
        # tail = self.queue.popleft() if self.cnt > self.size else 0
        self.window_sum = self.window_sum - tail + val
        return self.window_sum / min(self.size, self.cnt)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)