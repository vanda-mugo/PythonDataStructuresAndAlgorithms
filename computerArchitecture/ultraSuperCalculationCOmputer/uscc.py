#-------------------------------------------
# USCC Headquarter's Instruction Set Architecture
#  System Design:
#   - Four function calculator
#   - Can only operate on numbers stored in registers
#   - Processor receives binary data as 32-bit strings
#   - Returns results to the terminal
#   - Can operate on 10-bit numbers (0 thru 1023)
#   - Results can be negative (5 - 10 = -5)
#  Instruction format:
#   - 32 bit's in length
#   - Binary data will come to the CPU as a string
#   - Registers (32 total on CPU, 0-indexed)
#      - 0 thru 21:  Available for number storage
#        - 0: Constant 0
#      - 22 thru 31: Available for history storage
# +=======+=======+=======+=======+=======+=======+=======+=======+
# | 0: 0  | 1:    | 2:    | 3:    | 4:    | 5:    | 6:    | 7:    |
# +-------+-------+-------+-------+-------+-------+-------+-------+
# | 8:    | 9:    |10:    |11:    |12:    |13:    |14:    |15:    |
# +-------+-------+-------+-------+-------+-------+-------+-------+
# |16:    |17:    |18:    |19:    |20:    |21:    |22: H0 |23: H1 |
# +-------+-------+-------+-------+-------+-------+-------+-------+
# |24: H2 |25: H3 |26: H4 |27: H5 |28: H6 |29: H7 |30: H8 |31: H9 |
# +=======+=======+=======+=======+=======+=======+=======+=======+
#   - Bits 0-5 are OPCODEs
#     - use variable 'opcode' in program
#   - Bits 6-10 & 11-15 are source register locations
#     - use variables 'source_one' and 'source_two' in program
#   - Bits 16-25 are reserved for adding a new value to the registers
#     - use variable 'store' in program
#   - Bits 26-31 are functions
#     - use variable 'function_code' in program
# +--------+----------+-------------------------------------+
# | OPCODE | FUNCTION | Definition                          |
# | 000000 |  100000  | Add two numbers from registers      |
# | 000000 |  100010  | Subtract two numbers from registers |
# | 000000 |  011000  | Multiply two numbers from registers |
# | 000000 |  011010  | Divide two numbers from registers   |
# | 000001 |  000000  | Store value to next register        |
# | 100001 |  000000  | Return previous calculation         |
# +--------+----------+-------------------------------------+

# Your code below here:

class UltraSuperCalculator:
  def __init__(self,name) -> None:
    self.name = name 
    self.number_registers = [0 for i in range(22) ]
    self.history_registers = [0 for i in range(10)]
    self.number_index = 1
    self.history_index = 0
    self.temp_history_index = 0
    self.user_display = ""
    self.update_display(f"Welcome to {self.name} calculator")


    return None


  def update_display(self, to_update):
    self.user_display = to_update
    print(self.user_display)


  def store_value_to_register(self, value_to_store):
    if self.number_index > 21:
      self.number_index = 1
    self.number_registers[self.number_index] = int(value_to_store, 2)
    print(f" value of {int(value_to_store, 2)} stored in index{self.number_index} in number_registers ")
    self.number_index += 1

  def load_value_from_register(self, register_address):
    index = int(register_address, 2)
    int_value = int(self.number_registers[index])
    return int_value

  def store_to_history_register(self, result_to_store):
    if self.history_index > 9:
      self.history_index = 0
    self.history_registers[self.history_index] = bin(result_to_store)#[2:]
    self.history_index += 1
    self.temp_history_index = self.history_index

  def add(self, address_num1, address_num2):
    num1 = self.load_value_from_register(address_num1)
    num2 = self.load_value_from_register(address_num2)
    calculated_value = num1 + num2
    return calculated_value

  def multiply(self, address_num1, address_num2):
    num1 = self.load_value_from_register(address_num1)
    num2 = self.load_value_from_register(address_num2)
    calculated_value = num1 * num2
    return calculated_value

  def subtract(self, address_num1, address_num2):
    num1 = self.load_value_from_register(address_num1)
    num2 = self.load_value_from_register(address_num2)
    calculated_value = num1 - num2
    return calculated_value
  
  def divide(self, address_num1, address_num2):
    num1 = self.load_value_from_register(address_num1)
    num2 = self.load_value_from_register(address_num2)
    calculated_value = 0
    if num2 == 0:
      print(f"Division by 0 error: {num1}/{num2}.")
    else:
      calculated_value = int(num1/num2)
    
    return calculated_value

  
  def get_last_calculation(self):
    self.temp_history_index -= 1
    last_value = f"The last calculated value was: {int(self.history_registers[self.temp_history_index], 2)}"
    self.update_display(last_value)
  
  def binary_reader(self, instruction):
    if len(instruction) == 32:
      opcode = instruction[:6]
      source_one = instruction[6:11]
      source_two = instruction[11:16]
      store = instruction[16:26]
      function_code = instruction[26:]
      if opcode == "000001":
        self.store_value_to_register(store)
        return
      elif opcode == '100001':
        self.get_last_calculation()
        return 
      elif opcode != '000000':
        self.update_display("Invalid OPCODE") 
        return 
      result = 0
      if function_code == "100000":
        # addition 
        result = self.add(source_one, source_two)
      elif function_code == '100010':
        # subtract
        result = self.subtract(source_one, source_two)
      elif function_code == '011000':
        #multiply
        result = self.multiply(source_one, source_two)
      elif function_code == '011010':
        #divide
        result = self.divide(source_one, source_two)
      else:
        print("Incorrect function code passed ")
        return 
      self.store_to_history_register(result)
      self.update_display(f"result of the calculation is: {result}")
      
    else:
      self.update_display("Invalid Instruction Length")
      return





calc1 = UltraSuperCalculator("Vanda")
calc1.binary_reader("00000100000000000000000101000000")
calc1.binary_reader("00000100000000000000001010000000")

# Adds/Subtracts/Multiplies/Divides 5 and 10 from registers
calc1.binary_reader("00000000001000100000000000100000")
calc1.binary_reader("00000000001000100000000000100010")
calc1.binary_reader("00000000001000100000000000011000")
calc1.binary_reader("00000000001000100000000000011010")

# Gets the last three calculations
calc1.binary_reader("10000100000000000000000000000000")
calc1.binary_reader("10000100000000000000000000000000")
calc1.binary_reader("10000100000000000000000000000000")

































