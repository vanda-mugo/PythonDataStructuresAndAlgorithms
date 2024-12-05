from computerArchitecture.cache.isa import ISA
from computerArchitecture.cache.memory import Memory, MainMemory
from random import randint

class Cache(Memory):
  def __init__(self):
    super().__init__(name="Cache", access_time=0.5)
    self.main_memory = MainMemory()
    self.fifo_indices = [0, 0, 0, 0]
    self.sets = 1 # Set to 1, 2 or 4
    self.fifo_indices = [0, None, None, None]

    # Sets self.fifo_indicies based on 
    # the number of sets in the cache
    if self.sets == 2:
      self.fifo_indices = [0, 2, None, None]
    elif self.sets == 4:
      self.fifo_indices = [0, 1, 2, 3]

    self.data = [
      {"tag": None, "data": ""},
      {"tag": None, "data": ""},
      {"tag": None, "data": ""},
      {"tag": None, "data": ""},
    ]

  def write(self, address, data):
    super().write()
    entry = self.get_entry(address)
    if entry is not None:
      entry["data"] = data
    else:
      self.replace_entry(address, data)
    
    self.main_memory.write(address, data)

  def read(self, address):
    super().read()
    data = None
    entry = self.get_entry(address)
    if entry is not None:
      data = entry["data"]
    else:
      data = self.main_memory.read(address)
      self.replace_entry(address, data)

    return data

  def replace_entry(self, address, data):
    index = 0
    set_number = address % self.sets
    index = self.fifo_policy(set_number)
    self.data[index] = {"tag": address, "data": data}

  def random_policy(self, set_number):
    if self.sets == 1:
      return randint(0, len(self.data)-1)
    elif self.sets == 2:
      return randint(set_number*2, set_number*2+1)
    
    return set_number

  def fifo_policy(self, set_number):
    index = self.fifo_indices[set_number]
    self.fifo_indices[set_number] += 1
    if self.fifo_indices[set_number] == len(self.data)/self.sets+(set_number*int(len(self.data)/self.sets)):
      self.fifo_indices[set_number] = set_number*int(len(self.data)/self.sets)

    return self.fifo_indices[set_number]

  # Returns entry on cache hit
  # Returns None on cache miss
  def get_entry(self, address):
    for entry in self.data:
      if entry["tag"] == address:
          print(f"HIT: ", end="")
          return entry

    print(f"MISS", end="")
    return None

  def get_exec_time(self):
    exec_time = self.exec_time + self.main_memory.get_exec_time()
    return exec_time

if __name__ == "__main__":
  cache_arch = ISA()
  cache_arch.set_memory(Cache())

  # Architecture runs the instructions
  cache_arch.read_instructions("ex9_instructions")

  # This outputs the memory data and code execution time
  exec_time = cache_arch.get_exec_time()
  if exec_time > 0:
    print(f"OUTPUT STRING: {cache_arch.output}")
    print(f"EXECUTION TIME: {exec_time:.2f} nanoseconds")