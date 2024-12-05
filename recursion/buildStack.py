"""

The best way to understand recursion is with lots of practice! At first, this
Preview: Docs Loading link description
method
of solving a problem can seem unfamiliar but by the end of this lesson, we’ll have implemented a variety 
of algorithms using a recursive approach.

Before we dive into recursion, let’s replicate what’s happening in the call stack with an iterative 
function.

The call stack is abstracted away from us in Python, but we can recreate it to understand how 
recursive calls build up and resolve.

Let’s write a function that sums every number from 1 to the given input.


Execution contexts are a mapping between variable names and their values within the function during execution. We can use a list for our call stack and a
Preview: Docs Loading link description
dictionary
for each execution context.

Define a sum_to_one() function that has n as the sole parameter.

Inside the function body:

    declare the variable result and set it to 1.
    declare the variable call_stack and set it to an empty list.

Use multiple return to return both of these values: result, call_stack


"""

# define your sum_to_one() function above the function call
# execution context are mapping between variable name and their values within 
# the function during execution 


def sum_to_one(n):
  result = 1
  call_stack = []
  
  while n != 1:
    execution_context = {"n_value": n}
    call_stack.append(execution_context)
    n -= 1
    print(call_stack)
  print("BASE CASE REACHED")

  while len(call_stack) > 0:
    return_value = call_stack[-1]
    call_stack.pop()
    print(call_stack)
    print("adding {} to result".format(return_value["n_value"]) )
    result += return_value["n_value"]
  
  return result, call_stack

print(sum_to_one(4))


"""
output 

Output-only Terminal
Output:

[{'n_value': 4}]
[{'n_value': 4}, {'n_value': 3}]
[{'n_value': 4}, {'n_value': 3}, {'n_value': 2}]
BASE CASE REACHED
[{'n_value': 4}, {'n_value': 3}]
adding 2 to result
[{'n_value': 4}]
adding 3 to result
[]
adding 4 to result
(10, [])
"""

"""
if you were to print the output it would be 

(1, [{'n_value': 4}, {'n_value': 3}, {'n_value': 2}])


after adding the second while loop 

(10, [])


"""

# Define sum_to_one() below...
def sum_to_one(n):
  if n == 1:
    return 1
  print("Recursing with input: {}".format(n))
  return n + sum_to_one(n - 1 )

# uncomment when you're ready to test
print(sum_to_one(7))



# for factorial

# Define factorial() below:
def factorial(n):
  if n == 1:
    return 1

  return n * factorial(n - 1)


print(factorial(1200000))



def fibonacci(n):
  if n == 1:
    return 1
  if n == 0:
    return 0
  print(f"fibonacci called with value {n -1} and {n-2}")
  return fibonacci(n-1) + fibonacci(n-2)




fibonacci(5)
# set the appropriate runtime:
# 1, logN, N, N^2, 2^N, N!
fibonacci_runtime = "2^N"

