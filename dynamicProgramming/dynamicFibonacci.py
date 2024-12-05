"""
Create a memoized fibonacci() function. This function should return the nth Fibonacci number.

Note: To avoid an infinite loop, either handle the edge case of negative numbers in your function, 
or don’t call it using negative numbers.
"""
memo = {}

def fibonacci(num):
  answer = None
  # Write your code here
  if num <= 1:
    return num

  if num in memo:
    return memo[num]
  else:
    memo[num] = fibonacci(num - 1) + fibonacci(num - 2)
    return memo[num]



# Test your code with calls here:
print(fibonacci(20))
print(fibonacci(200))