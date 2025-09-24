class MyHashSet(object):
    def __init__(self):
        self.hashset = set()

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        if not self.contains(key):
            self.hashset.add(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if self.contains(key):
            self.hashset.remove(key)

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        return key in self.hashset


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(2)
# obj.remove(2)
# print(obj.contains(2))