"""
Prepend and append to a string

Alex has picked out the gemstone that caught his friend’s fancy. He needs to wrap this fragile 
gemstone in wrapping paper before shipping it off to her. For our purpose, we will represent 
each layer of wrapping paper as "<>", so a pearl wrapped in 3 layers would be "<<<Pearl>>>". 
Let’s define a recursive function that wraps up a specified string in n layers of wrapping paper.

    Create a result variable and assign it to an empty string "".
    The base case checks if n is less than or equal to 0, in which case the string is returned.
    To wrap up the string, put the recursive step in-between two iterative statements:
        Concatenate result with "<".
        Concatenate result with the recursive call with decremented input n-1.
        Concatenate result with ">".
    Return result.


Let’s go over the following solution:

def wrap_string(str, n):
  result = ""
  if n <= 0:
    return str
  result += "<"
  result += wrap_string(str, n-1)
  result += ">"

  return result

Like the first challenge, we will use a variable called result to store the output string.

In the base case, we check if n <= 0, in which case we simply return the unwrapped str.

The recursive step happens between two iterative statements. < is prepended to result before 
the recursive call, and > is appended to result after the recursive call. In the middle, 
wrap_string() is called with n-1 to bring the input one step closer to the base case. 
The return value of this recursive call is concatenated to result as well.

Using this approach, result will be wrapped layer by layer due to the order of the call 
stack returns. For example, when we call wrap_string("Pearl", 3), the call stack will return 
in this order: Pearl -> <Pearl> -> <<Pearl>> -> <<<Pearl>>>.

"""


# define wrap_string() here

def wrap_string(str, n):
  result = ""
  if n <= 0:
    return str
  else:
    result += "<" 
    result += wrap_string(str, n-1)
    result += ">"
    return result
  return result

  



# Test code - do not edit
wrapped = wrap_string("Pearl", 3)
print(wrapped)