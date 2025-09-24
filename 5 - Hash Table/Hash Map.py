class MyHashMap(object):
    def __init__(self):
        self.hashmap = dict()

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.hashmap[key] = value

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.hashmap:
            return self.hashmap[key]
        return -1

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key in self.hashmap:
            self.hashmap.pop(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put('name', 'jean')
# print(obj.get('name'))
# obj.remove('name')
# print(obj.get('name'))
