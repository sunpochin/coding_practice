# Complexity Analysis
# Time Complexity: O(1). 
# #The lookup and update of the hashtable takes a constant time.
# Space Complexity: O(M) where M is the size of 
# all incoming messages. Over the time, the hashtable would have an entry for each unique message that has appeared.


class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hmap = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        prev = self.hmap.get(message)
        if None == prev or (timestamp - self.hmap.get(message) ) >= 10:
            self.hmap[message] = timestamp
            return True
        else:
            return False
        

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
