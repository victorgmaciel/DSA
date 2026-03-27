# design a class 
#. 1. inserting a value(no dups)
#   2. removing a value
    # 3. getRandomValue that is already inserted
import random
from sortedcontainers import SortedSet


class Store:
    def __init__(self):
        self.map = SortedSet()

    def insert_value(self, value):
        self.map.add(value)

    def remove_value(self, value):
        if value in self.map:
            self.map.remove(value)
        else:
            print("hey this value is not in the map")
    
    def get_random_value(self):
        if not self.map:
            print("not in the map")
            return None
        
        return random.choice(list(self.map))




store = Store()

store.insert_value(3)
store.insert_value(4)
store.insert_value(1)
store.insert_value(10)

print(store.map)

store.insert_value(19)

print(store.map)

print(store.get_random_value())





