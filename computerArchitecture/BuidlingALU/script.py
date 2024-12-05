
def XOR_gate(a, b):
  if a and not b:
    return True
  elif b and not a:
    return True
  else:
    return False
  
def AND_gate(a, b):
  if a and b:
    return True
  return False



def half_adder(a, b):
  #s = OR_gate(a, b)
  s = XOR_gate(a,b)
  c = AND_gate(a,b)
  return s,c

def full_adder(a, b, c):
  sum_one, c_one = half_adder(a, b)
  s, c_two = half_adder(sum_one, c)
  return s, c_one or c_two


def ALU(a, b, c, opcode):
  s = None
  c = None
  if not opcode:
    s, c = half_adder(a, b)
  elif opcode:
    s,c = full_adder(a, b, c)
  
  return s, c
    


 



print(half_adder(0,0))
print(half_adder(1,0))
print(half_adder(0,1))
print(half_adder(1,1))

print("Division")
print(full_adder(0, 0, 0))
print(full_adder(0, 0, 1))
print(full_adder(0, 1, 0))
print(full_adder(0, 1, 1))
print(full_adder(1, 0, 0))
print(full_adder(1, 0, 1))
print(full_adder(1, 1, 0))
print(full_adder(1, 1, 1))

print("ALU")
print(ALU(0,0,1,0))
print(ALU(0,0,1,1))
print(ALU(1,1,1,0))
print(ALU(1,1,1,1))