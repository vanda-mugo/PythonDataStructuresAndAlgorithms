"""
Hash Functions
4 min

A hash function takes a
Preview: Docs Loading link description
string
(or some other type of data) as input and returns an
Preview: Docs Loading link description
array
Preview: Docs Loading link description
index
as output. In order for it to return an array index, our hash map implementation needs to know the size of our array. 
If the array we are saving values into only has 4 slots, our hash map’s hashing
Preview: Docs Loading link description
method
should not return an index bigger than that.

In order for our hash map implementation to guarantee that it returns an index that fits into the underlying array, 
the hash function will first compute a value using some scoring metric: this is the hash value, hash code, or just the hash. 
Our hash map implementation then takes that hash value mod the size of the array. This guarantees that the value returned by 
the hash function can be used as an index into the array we’re using.

It is actually a defining feature of all hash functions that they greatly reduce any possible inputs (any string you can imagine) 
into a much smaller range of potential outputs (an integer smaller than the size of our array). For this reason, hash functions 
are also known as compression functions.

Much like an image that has been shrunk to a lower resolution, the output of a hash function contains less data than the input. 
Because of this, hashing is not a reversible process. With just a hash value it is impossible to know for sure the key that was 
plugged into the hashing function.

How to Write a Hash Function
3 min

You might be thinking at this point that we’ve glossed over a very important aspect of a
Preview: Docs Loading link description
hash table
here. We’ve mentioned that a hash function is necessary, and described some features of what a hash function does, 
but never really given an implementation of a hash function that does not feel like a toy example.

Part of this is because a hash function needs to be simple by design. Performing complex mathematical calculations that our 
hash table needs to compute every time it wants to assign or retrieve a value for a key will significantly damage a hash table’s 
performance for two things that it should be able to do quickly.

Hash functions also need to be able to take whatever types of data we want to use as a key. We only discussed strings, 
a very common use case, but it’s possible to use numbers as hash table keys as well.

A very common hash function for integers, for example, is to perform the modular operation on it to make sure it’s less than the size of the underlying
Preview: Docs Stores elements of various data types in an ordered collection.
array
. If the integer is already small enough to be an
Preview: Docs Loading link description
index
into the array, there’s nothing to be done.

Many hash functions implementations for strings take advantage of the fact that strings are represented internally as numerical data. 
Frequently a hash function will perform a shift of the data bitwise, which is computationally simple for a computer to do but also can 
predictably assign numbers to strings.



Basic Hash Maps
4 min

Now that we have all of the main ingredients for a hash map, let’s put them all together. First, we need some sort of associated data that 
we’re hoping to preserve. Second, we need an array of a fixed size to insert our data into. Lastly, we need a hash function that translates 
the keys of our array into indexes into the array. The storage location at the index given by a hash is called the hash bucket.

Let’s use the following example for our hash map:
Key: Album Name 	Value: Release Year
The Low End Theory 	1991
Midnight Marauders 	1993
Beats, Rhymes and Life 	1996
The Love Movement 	1998

Our map here relates to several A Tribe Called Quest studio albums with the year they were produced in. We’ll need an array of at least size 
4 to contain all of these elements. And a way to turn each album name into an index into that array.

For each album name, find that album’s hash by performing the following calculation:

hash_value = ((# of lowercase 'a's in album name) + (# of number of lowercase 'e's in album name))

And then take that hash and calculate an array index by performing hash_value mod 4. Following these steps we get the following schema:
Album Name 	Hash 	Hash mod 4 	Release Year
The Low End Theory 	2 	2 	1991
Midnight Marauders 	3 	3 	1993
Beats, Rhymes and Life 	5 	1 	1996
The Love Movement 	4 	0 	1998

First, the key is translated into the hash using our hashing function. Then, our hash map performs modulo arithmetic to turn the hash into an array index.

Collisions
1 min

Remember hash functions are designed to compress data from a large number of possible keys to a much smaller range. Because of this compression, 
it’s likely that our hash function might produce the same hash for two different keys. This is known as a hash collision. 
There are several strategies for resolving hash collisions.

The first strategy we’re going to learn about is called separate chaining. The separate chaining strategy avoids collisions by updating 
the underlying data structure. Instead of an
Preview: Docs Loading link description
array
of values that are mapped to by hashes, it could be an array of linked lists!


Separate Chaining
4 min

A hash map with a linked list separate chaining strategy follows a similar flow to the hash maps that have been described so far. 
The user wants to assign a value to a key in the map. The hash map takes the key and transforms it into a hash code. 
The hash code is then converted into an
Preview: Docs Loading link description
index
to an
Preview: Docs Loading link description
array
using the modulus operation. If the value of the array at the hash function’s returned index is empty, a new linked list is created with the 
value as the first element of the linked list. If a linked list already exists at the address, append the value to the linked list given.

This is effective for hash functions that are particularly good at giving unique indices, so the linked lists never get very long. 
But in the worst-case scenario, where the hash function gives all keys the same index, lookup performance is only as good as it would 
be on a linked list. Hash maps are frequently employed because looking up a value (for a given key) is quick. Looking up a value in a 
linked list is much slower than a perfect, collision-free hash map of the same size. A hash map that uses separate chaining with linked 
lists but experiences frequent collisions loses one of its most essential features.


"""
#python implementation of the hash table with separate chaining implemented 


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class SeparateChainingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self,  

 key):
        # Simple hash function: divide by size and take the remainder
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = Node(key, value)
        else:  

            head = self.table[index]
            while head.next is not None:
                head = head.next
            head.next = Node(key, value)

    def search(self, key):
        index = self.hash_function(key)
        head = self.table[index]
        while head is not None:
            if head.key == key:
                return head.value
            head = head.next
        return None

    def delete(self, key):
        index = self.hash_function(key)  

        head = self.table[index]
        prev = None
        while head is not None:
            if head.key == key:
                if prev is None:
                    self.table[index] = head.next
                else:
                    prev.next = head.next
                return
            prev = head
            head = head.next

# Example usage
hash_table = SeparateChainingHashTable(5)
hash_table.insert(1, "apple")
hash_table.insert(6, "banana")
hash_table.insert(11, "cherry")
hash_table.insert(16, "date")
hash_table.insert(21, "elderberry")

print(hash_table.search(6))  # Output: banana
print(hash_table.search(15))  # Output: None (not found)

hash_table.delete(11)
print(hash_table.search(11))  # Output: None (deleted)


"""
Creating the Hash Map Class
7 min

Hash maps are efficient key-value stores. They are capable of assigning and retrieving data in the fastest way possible for a data structure. 
This is because the underlying data structure that they use is an
Preview: Docs Loading link description
array
. A value is stored at an array
Preview: Docs Loading link description
index
determined by plugging the key into a hash function.

In Python we don’t have an array data structure that uses a contiguous block of memory. We are going to simulate an array by creating a list and 
keeping track of the size of the list with an additional integer variable. This will allow us to design something that resembles a hash map. 
This is somewhat elaborate for the actual storage of a key-value pair, but it helps to remember that the purpose of this lesson is to gain a 
deeper understanding of the structure as it is constructed. For real-world use cases in which a key-value store is needed, Python offers a built-in
Preview: Docs Loading link description
hash table
implementation with dictionaries.

Creating the Hashing Function
5 min

The necessary ingredient in the hash map recipe is the hashing function. A hashing function takes a key and returns an
Preview: Docs Loading link description
index
into the underlying
Preview: Docs Loading link description
array
.

Hash functions need to be fast to compute so that access and retrieval can be done fast.

Creating the Compression Function
3 min

Hashing functions return a wide range of integers. In order to transform these values into useful indices for our
Preview: Docs Loading link description
array
we need a compression function. A compression function uses modular arithmetic to calculate an array
Preview: Docs Loading link description
index
for a hash map when given a hash code.

Defining the Setter
5 min

A data structure that is unable to contain data is a sad sight indeed. We need to put together all the other steps we’ve taken: 
plug the key into the hash function, plug the hash code into the compression function, use the
Preview: Docs Loading link description
array
Preview: Docs Loading link description
index
to find the place in the array, and finally set the value of the array to the value we want.


Defining the Getter
3 min

There is a natural expectation after placing an item into a bag that we will later be able to remove the item from that bag. 
Otherwise we have created a hole. Let’s implement retrieval for our hash map.

Creating an Instance
4 min

Since we have the basic functionality of a hash map, let’s create a test instance of one for us to make sure everything works as expected.


Handling Collisions in the Setter
12 min

Our hash and compression functions together can result in collisions. This is when two different keys resolve to the same
Preview: Docs Stores elements of various data types in an ordered collection.
array
Preview: Docs Improves the speed of data retrieval in the database.
index
. In our current implementation, all keys that resolve to the same index are treated as if they are the same key.

Our first step in implementing a collision strategy is updating our .assign() and .retrieve() methods to set the 
value with the key and check the key before retrieving a value.


Open Addressing
5 min

Now we’re going to implement an open addressing system so our hash map can resolve collisions. In open addressing systems, we check the
Preview: Docs Loading link description
array
at the address given by our hashing function. One of three things can happen:

    The address points to an empty cell.
    The cell holds a value for the key we are getting/setting
    The cell holds a value for a different key.

In the first case, this means that the hash map does not have a value for the key and no collision resolution needs to happen. 
Notice that this does not work if we want to be able to delete keys in our hash map. There are strategies for deleting pairs from 
a hash map (see Lazy Deletion) but we will not be investigating these.

In the second case, we’ve found the value for our key-value pair!

In the third case, we need to use our collision addressing strategy to find if our key is somewhere else (it may or may not be) 
so we should recalculate the
Preview: Docs Loading link description
index
of our array.


Saving Keys
3 min

A hash collision resolution strategy like separate chaining involves assigning two keys with the same hash to different parts of 
the underlying data structure. How do we know which values relate back to which keys? If the linked list at the
Preview: Docs Loading link description
array
Preview: Docs Loading link description
index
given by the hash has multiple elements, they would be indistinguishable to someone with just the key.

If we save both the key and the value, then we will be able to check against the saved key when we’re accessing data in a hash map. 
By saving the key with the value, we can avoid situations in which two keys have the same hash code where we might not be able to 
distinguish which value goes with a given key.

Now, when we go to read or write a value for a key we do the following: calculate the hash for the key, find the appropriate index for that hash, 
and begin iterating through our linked list. For each element, if the saved key is the same as our key, return the value. Otherwise, continue 
iterating through the list comparing the keys saved in that list with our key.


Open Addressing: Linear Probing
3 min

Another popular hash collision strategy is called open addressing. In open addressing we stick to the
Preview: Docs Loading link description
array
as our underlying data structure, but we continue looking for a new
Preview: Docs Improves the speed of data retrieval in the database.
index
to save our data if the first result of our hash function has a different key’s data.

A common open
Preview: Docs A method is a small piece of code, usually defined in a class, that can be used outside the class and in other parts of the program.
method
of open addressing is called probing. Probing means continuing to find new array indices in a fixed sequence until an empty index is found.

Suppose we want to associate famous horses with their owners. We want our first key, “Bucephalus”, to store our first value, “Alexander the Great”. 
Our hash function returns an array index 3 and so we save “Alexander the Great”, along with our key “Bucephalus”, into the array at index 3.

After that, we want to store “Seabiscuit”s owner “Charles Howard”. Unfortunately “Seabiscuit” also has a hash value of 3. Our probing method adds 
one to the hash value and tells us to continue looking at index 4. Since index 4 is open we store “Charles Howard” into the array at index 4. Because 
“Seabiscuit” has a hash of 3 but “Charles Howard” is located at index 4, we must also save “Seabiscuit” into the array at that index.

When we attempt to look up “Seabiscuit” in our Horse Owner’s Hash Map, we first check the array at index 3. Upon noticing that our key (Seabiscuit) 
is different from the key sitting in index 3 (Bucephalus), we realize that this can’t be the value we were looking for at all. Only by continuing to 
the next index do we check the key and notice that at index 4 our key matches the key saved into the index 4 bucket. Realizing that index 4 has the 
key “Seabiscuit” means we can retrieve the information at that location, Seabiscuit’s owner’s name: Charles Howard.


Open Addressing in the Setter
15 min

Now lets use our open addressing scheme in the setter for our HashMap.


Open Addressing in the Getter
10 min

With everything in our setter taken care of, we want to make sure that when we retrieve our value we’re retrieving the correct value.


"""

class HashMap:
  def __init__(self, array_size):
    self.array_size = array_size
    self.array = [None for item in range(array_size)]

  def hash(self, key, count_collisions=0):
    key_bytes = key.encode()
    hash_code = sum(key_bytes)
    return hash_code + count_collisions

  def compressor(self, hash_code):
    return hash_code % self.array_size

  def assign(self, key, value):
    array_index = self.compressor(self.hash(key))
    current_array_value = self.array[array_index]

    if current_array_value is None:
      self.array[array_index] = [key, value]
      return

    if current_array_value[0] == key:
      self.array[array_index] = [key, value]
      return

    # Collision!

    number_collisions = 1

    while(current_array_value[0] != key):
      new_hash_code = self.hash(key, number_collisions)
      new_array_index = self.compressor(new_hash_code)
      current_array_value = self.array[new_array_index]

      if current_array_value is None:
        self.array[new_array_index] = [key, value]
        return

      if current_array_value[0] == key:
        self.array[new_array_index] = [key, value]
        return

      number_collisions += 1

    return

  def retrieve(self, key):
    array_index = self.compressor(self.hash(key))
    possible_return_value = self.array[array_index]

    if possible_return_value is None:
        return None

    if possible_return_value[0] == key:
        return possible_return_value[1]

    # possible_return_value holds different key
    if possible_return_value[0] != key:
      retrieval_collisions = 1
      while possible_return_value[0] != key:
        new_hash_code = self.hash(key, retrieval_collisions)
        retrieving_array_index = self.compressor(new_hash_code)
        possible_return_value = self.array[retrieving_array_index]

        if possible_return_value is None:
          return None
        if possible_return_value[0] != key:
          retrieval_collisions += 1
        if key == possible_return_value[0]:
          return possible_return_value[1]



    return
