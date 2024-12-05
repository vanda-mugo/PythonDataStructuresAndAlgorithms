from stack import Stack

print("\nLet's play Towers of Hanoi!!")

#Create the Stacks
stacks = []
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")

stacks.extend([left_stack, middle_stack, right_stack])
#Set up the Game

num_disks :int = int(input ("\nHow many disks do you want to play with?\n"))

while num_disks < 3:
  num_disks = int(input("Enter a number greater than or equal to 3\n"))


for i in range(num_disks, 0, -1):
  left_stack.push(i)
  """
  Now that we created our initial stacks and set up the disks, let’s calculate the number of optimal moves.

  For towers of hanoi, the number of optimal moves is always 2Number of Disks - 1.

  After the for loop, create a variable, num_optimal_moves, and set it equal to the number of optimal moves.

  Afterwards, print, "\nThe fastest you can solve this game is in {0} moves" {0} corresponds to the num_optimal_moves.
  """

num_optimal_moves = (2 ** num_disks) - 1
print(f"\nThe fastest you can solve this game is in {num_optimal_moves} moves")

#Get User Input
def get_input():
  choices = [item.get_name()[0] for item in stacks]
  while True:
    for i in range(len(stacks)):
      name = stacks[i].get_name()
      letter = choices[i]
      print(f"Enter {letter} for {name}")
    user_input = input(" ")
    if user_input in choices:
      for i in range(len(stacks)):
        if user_input == choices[i]:
          return stacks[i]

        
#Play the Game

num_user_moves = 0

while right_stack.get_size() != num_disks:
  print("\n\n\n...Current Stacks...")
  for item in stacks:
    item.print_items()
  while True:
    print("\nWhich stack do you want to move from?\n")
    from_stack = get_input()
    print("\nWhich stack do you want to move to?\n")
    to_stack = get_input()
    if from_stack.is_empty():
      print(f"\n\nInvalid Move.{from_stack.get_name()} is empty Try Again")
    elif to_stack.is_empty() or to_stack.peek() > from_stack.peek():
      disk = from_stack.pop()
      to_stack.push(disk)
      num_user_moves += 1
      break
    else:
      print(f"\n\nInvalid Move. {from_stack.get_name()} has {from_stack.peek()} top value which is lager than {to_stack.get_name()}'s top value of {to_stack.peek()}Try Again")


print(f"\n\nYou completed the game in {num_user_moves} moves, and the optimal number of moves is {num_optimal_moves}")

      



    

























