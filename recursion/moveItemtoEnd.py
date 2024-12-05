"""
Move items to the end of a list

As you know by now, a List in Python is used to store multiple items in a single variable. 
Unfortunately, the order of items might not always be the one we want. The following problem 
represents a scenario where a list needs to be reorganized.

Alex is a gemstone collector who recently placed an order for an assortment of ambers, jades, 
pearls, and sapphires. When he opened the delivery package, Alex found that his list of gemstones 
was mixed up.

Alex is particularly fond of a certain type of gemstone and wants to move them to the end of his 
gallery display. Let’s design a recursive algorithm to help Alex set up his gallery:

    Define a function that takes in two arguments: a list and a string. The string will represent 
    the value we are looking for in the list.
    Create a result variable and assign it to an empty list []. This variable will store the final 
        result.
    Address the base case: if the given list is empty, return an empty list.
    The recursive step can go either of two ways:
        If the first item in the list matches the value we are looking for, set the value of result to 
        a recursive call in which the first argument is our list of values minus the first element and 
        the second argument is the value we are looking for. Then append the first item of the list to 
        result.
        Else, append the first item of the list to result. Then set the value of result to a recursive 
        call in which the first argument is our list of values minus the first element and the second 
        argument is the value we are looking for.
    Finally, return result.
"""




# define move_to_end() here
def move_to_end(lst : list, val : str):
  result = []
  if not lst:
    return []

  if lst[0] == val:
    # what this essentially does is that 
    # in the case that the value is equal to first element then the function is called  with a different values and it has to return before the result is appended
    result += move_to_end(lst[1:], val)
    result.append(lst[0])

  else:
    result.append(lst[0])
    result += move_to_end(lst[1:], val)

  return result

  

# Test code - do not edit
gemstones = ["Amber", "Sapphire", "Amber", "Jade"]
print(move_to_end(gemstones, "Amber"))



"""
lets breakdown what is happening here 

Example Execution: move_to_end(gemstones, "Amber")

Here, gemstones = ["Amber", "Sapphire", "Amber", "Jade"] and val = "Amber". We will look at how the stack frames are created and popped.

    Initial Call:

    python

move_to_end(["Amber", "Sapphire", "Amber", "Jade"], "Amber")

    First element: "Amber"
    The condition if lst[0] == val is True.
    Recursively call:

    python

    move_to_end(["Sapphire", "Amber", "Jade"], "Amber")

Second Call:

python

move_to_end(["Sapphire", "Amber", "Jade"], "Amber")

    First element: "Sapphire"
    The condition if lst[0] == val is False.
    Add "Sapphire" to the result and recursively call:

    python

    move_to_end(["Amber", "Jade"], "Amber")

Third Call:

python

move_to_end(["Amber", "Jade"], "Amber")

    First element: "Amber"
    The condition if lst[0] == val is True.
    Recursively call:

    python

    move_to_end(["Jade"], "Amber")

Fourth Call:

python

move_to_end(["Jade"], "Amber")

    First element: "Jade"
    The condition if lst[0] == val is False.
    Add "Jade" to the result and recursively call:

    python

    move_to_end([], "Amber")

Fifth Call (Base Case):

python

move_to_end([], "Amber")

    The list is empty, so return an empty list:

    python

        return []

Call Stack Unwinding

Now, let’s trace back the stack as it unwinds, starting from the base case.

    Unwinding the Fourth Call:

    python

move_to_end(["Jade"], "Amber")

    The recursive call move_to_end([]) returned [].
    The result becomes ["Jade"].
    Return ["Jade"] to the third call.

Unwinding the Third Call:

python

move_to_end(["Amber", "Jade"], "Amber")

    The recursive call move_to_end(["Jade"], "Amber") returned ["Jade"].
    Add "Amber" to the end of the result: ["Jade", "Amber"].
    Return ["Jade", "Amber"] to the second call.

Unwinding the Second Call:

python

move_to_end(["Sapphire", "Amber", "Jade"], "Amber")

    The recursive call move_to_end(["Amber", "Jade"], "Amber") returned ["Jade", "Amber"].
    Add "Sapphire" to the result: ["Sapphire", "Jade", "Amber"].
    Return ["Sapphire", "Jade", "Amber"] to the initial call.

Unwinding the Initial Call:

python

    move_to_end(["Amber", "Sapphire", "Amber", "Jade"], "Amber")

        The recursive call move_to_end(["Sapphire", "Amber", "Jade"], "Amber") returned ["Sapphire", "Jade", "Amber"].
        Add "Amber" to the end of the result: ["Sapphire", "Jade", "Amber", "Amber"].
        Return the final result ["Sapphire", "Jade", "Amber", "Amber"].

Summary of Stack Frames:

    Each recursive call creates a new stack frame with its own copy of lst and val.
    When the base case is reached (empty list), the recursion stops, and the stack frames start to pop off.
    As the stack unwinds, each function call either appends the current element (lst[0]) or moves it to the end (if it's val).
    The stack unwinding follows a Last In, First Out (LIFO) order, with the most recent recursive call being resolved first.

The final result, after all the stack frames are popped and the list is fully built, is ["Sapphire", "Jade", "Amber", "Amber"].





"""