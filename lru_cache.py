"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4

"""



from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        
        self.capacity = capacity
        self.cache = OrderedDict()
        
    
    def get(self , key):
        
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]
            
    
    def put(self,key,value):
        # in case of put every time we have to make an entry of it 
        # and make that as recent / first element
        # if the size() if greter than capacity then we have to pop the 1st item
        
        self.cache[key] = value
        self.cache.move_to_end(key)
        
        # now will check the size of it is within the limit then it's ok otherwise will pop the 1st item
        if len(self.cache) > self.capacity:
            # last=True, LIFO; last=False, FIFO. We want to remove in FIFO fashion.
            self.cache.popitem(last=False)
        
            
            