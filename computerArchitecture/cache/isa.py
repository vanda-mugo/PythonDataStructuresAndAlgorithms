from computerArchitecture.cache.memory import Memory
from time import time

# Register class used for register
# data storage in the ISA() class
class Register(Memory):
  def __init__(self):
    Memory.__init__(self, name="Register", access_time=0.1)
    self.data = {"r0": None, "r1": None}
  
  # Read data to register address
  def read(self, address):
    super().read(output=False)
    return self.data[address]

  # Write data to register address
  def write(self, address, data):
    super().write(output=False)
    self.data[address] = data
  
  # Return total execution time
  def get_exec_time(self):
    return self.exec_time

# Memory simulation architecture class
class ISA():
  def __init__(self):
    self.memory = None
    self.registers = Register()
    self.instructions = { 
      "lb": self.load_b, 
      "sb": self.store,
      "li": self.load_i,
      "j": self.jump,
    }
    self.output = ""

  # Assign memory class for the
  # archicture for reading and writing
  def set_memory(self, memory):
    self.memory = memory

  # Go through lines of instruction file 
  def read_instructions(self, file):
    if self.memory is not None:
      print(f"ISA memory: {self.memory.name}")
      start = time()
      with open(file) as codefile:
        code = codefile.readlines()
        lines = [line.strip() for line in code if line.strip() != '']
        for line in lines:
          self.parse_line(line)
      return time() - start
    else:
      print("Architecture has found no memory")
      return None
  # Parse line and send arguments
  # to the correct instruction
  def parse_line(self, line):
    tokens = line.split(' ')
    inst = tokens[0]
    if inst == "lb" or inst == "sb":
      print(f"{line}", end="")
    arg1 = tokens[1]
    if len(tokens) == 2 and inst == "li":
      arg2 = " "
      self.instructions[inst](arg1, arg2)
    elif len(tokens) > 2:
      arg2 = tokens[2]
      self.instructions[inst](arg1, arg2)
    else:
      self.instructions[inst](arg1)

  # load data to register from 
  # memory address
  def load_b(self, arg1, arg2):
    address = int(self.registers.read(arg2))
    data = self.memory.read(address)
    self.registers.write(arg1, data)
    if data is not None:
      print(data)

  # store data in register from
  # memory address
  def store(self, arg1, arg2):
    data = self.registers.read(arg1)
    address = int(self.registers.read(arg2))
    self.memory.write(address, data)
    if data is not None:
      print(data)

  # load number in register
  def load_i(self, arg1, arg2):
    self.registers.write(arg1, arg2)

  # jump instruction used to create
  # simulation output
  def jump(self, arg1):
    if arg1 == "100":
      data = self.registers.read('r0')
      if data is not None:
        self.output += data
      else:
        print("- NO DATA")
    else:
      print("Jump address not recognized.")

  # return the cumulative execution time
  # of the registers and memory
  def get_exec_time(self):
    exec_time = self.registers.get_exec_time()
    if self.memory is not None:
      exec_time += self.memory.get_exec_time()
    
    return exec_time