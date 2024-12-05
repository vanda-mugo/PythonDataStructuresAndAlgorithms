from linked_list import Node, LinkedList
from blossom_lib import flower_definitions

class HashMap:
  def __init__(self, size):
    self.array_size = size
    self.array = [LinkedList() for i in range(self.array_size)]

  def hash(self, key : str):
    hash_code = key.encode()
    return sum(hash_code)

  def compress(self, hash_code):
    return hash_code % self.array_size 

  def assign(self, key, value):
    hash_code = self.hash(key)
    array_index = self.compress(hash_code)
    payload = Node([key,value])
    # note that this is a linked list we are talking about 

    list_at_array = self.array[array_index] 
    # in short here we are iterating through the linked list
    # This is possible since the LinkedList class defined implements an iterator 
    for item in list_at_array:
      if item[0] == key:
        item[1] = value 

    # in this case the for loop is done and we havent found our key in the items stored within the nodes 
    # based on the insert method what happens is that the 
    # insert iterates to the last element of in the linked list if its not empty, if the linked list is empty then it will be the head node set as payload 
    
    list_at_array.insert(payload)

    
  def retrieve(self, key):
    array_index = self.compress(self.hash(key))
    list_at_index = self.array[array_index]
    
    # now note that the list_at_index represents a linked list 
    for item in list_at_index:
      if item[0] == key:
        return item[1]
    return None



blossom = HashMap(len(flower_definitions))

for flower in flower_definitions:
  blossom.assign(flower[0], flower[1])

print(blossom.retrieve('daisy'))
print(blossom.retrieve('begonia'))

