"""
The Knapsack Problem

Recursive and dynamic programming approaches to the classic knapsack problem in Python.

Imagine that you’re a thief breaking into a house. There are so many valuables to 
steal - diamonds, gold, jewelry, and more! But remember, you’re just one person who can only carry so much. 
Each item has a weight and value, and your goal is to maximize the total value of items while remaining within the weight limit of your knapsack. 
This is called the knapsack problem and is commonly used in programming interviews. We will solve this problem in two ways: recursively, 
and using dynamic programming. 

The Problem

The first step to solving this problem is to understand the parameters involved. You will be given:

    the total amount of weight you can carry (weight_cap)
    the weights of all of the items in an array (weights)
    the values of all of the items in an array (values)

Your function should return the maximum value that you will be able to carry.
An Example

Let’s say that you have a knapsack that can only carry 5 pounds, and the house you’re robbing has three items that you want to steal:

    A ring that weighs 1 pound with a value of $250
    Earrings that weigh 3 pounds with a value of $300
    A necklace that weighs 5 pounds with a value of $500

This information can be summarized as follows:

weight_cap = 5 
weights = [1, 3, 5]
values = [250, 300, 500]

You have four possible ways to fill your knapsack:

    Take only the ring, giving you $250
    Take only the earrings, giving you $300
    Take only the necklace, giving you $500
    Take the ring and the earrings, giving you $550

Since the ring and the earrings have a combined weight of 4 pounds, taking both gives you the maximum value while staying 
within your weight capacity. Now that you’re familiar with the problem, let’s take a look at two different approaches to solving it!


The Recursive Solution

The brute force solution to this problem is to look at every subset of the items that has a total weight less than weight_cap. 
Then you simply take the maximum of those subsets, giving you the optimized subset with the highest value possible.

You will need an additional parameter, i, that tells us where we are in the list of items. With each step, we will break the problem down 
into subproblems, and compare them to find the maximum value. There are three possibilities for every call of the function:

    weight_cap or i are zero, meaning the knapsack can hold no weight, or there are no more items to look at. In either case, we return 0.
    The weight of the item we’re looking at exceeds weight_cap, in which case we just move on, calling the function on the next item.
    If neither of the above are true, that means we have to consider whether or not the item we are at (i) should be included in the optimal solution.

Steps 1 and 2 from above can be solved as follows:

def recursive_knapsack(weight_cap, weights, values, i):
  # base condition
  if weight_cap == 0 or i == 0:
    return 0
  # recursive solution
  elif weights[i - 1] > weight_cap:
    return recursive_knapsack(weight_cap, weights, values, i - 1)

For step 3, we need to look at both situations and determine if we want to include this item in our optimized solution or not. 


While this recursive solution works, it has a big O runtime of O(2^n). In the worst case, each step would require us to evaluate two subproblems, 
sometimes repeatedly, as there’s overlap between subproblems. We can drastically improve on this runtime by using dynamic programming.

"""

def recursive_knapsack(weight_cap, weights, values, i):
  if weight_cap == 0 or i == 0:
    return 0
  elif weights[i - 1] > weight_cap:
    return recursive_knapsack(weight_cap, weights, values, i - 1)
  else:
    include_item = values[i - 1] + recursive_knapsack(weight_cap - weights[i - 1], weights, values, i - 1)

    exclude_item = recursive_knapsack(weight_cap, weights, values, i - 1)

    return max(include_item, exclude_item)




"""

lets analyze what would happen had this been called with ]
# Example values and weights
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
weight_cap = 5



1st call in 
Initial Call: recursive_knapsack(5, [2, 3, 4, 5], [3, 4, 5, 6], 4)

weight_cap = 5, i = 4 (considering item 4 with weight 5 and value 6)

include item 4 == 6 + recursive_knapsack(0, [2, 3, 4, 5], [3, 4, 5, 6], 3)

this results = 6 + 0


exclude : recursive_knapsack(5, [2, 3, 4, 5], [3, 4, 5, 6], 3) == 7

max 6, 7 == 7

2nd call 
recursive_knapsack(0, [2, 3, 4, 5], [3, 4, 5, 6], 3)
in this call teh return is 0




3rd call
recursive_knapsack(5, [2, 3, 4, 5], [3, 4, 5, 6], 3)

weight_cap = 5, i = 3 (considering item 3 with weight 4 and value 5)

The weight of item 3 (4) is less than weight_cap, so we calculate:

recursive_knapsack(5, [2, 3, 4, 5], [3, 4, 5, 6], 3)

include = 5 + recursive(1, [2,3,4,5], [3,4,5,6], 2)

include results 5 + 0


exclude = 
recursive_call = recursive_knapsack(5, [2,3,4,5],[3,4,5,6], 2) ==7
results in 7

max(7, 5) == 7




4rth call
initial call
recursive(1, [2,3,4,5], [3,4,5,6], 2) == 0

return 
recursive(1, [2,3,4,5], [3,4,5,6], 1)  == 0


5th call 
recursive(1, [2,3,4,5], [3,4,5,6], 1)  == 0

return 
recursive(1, [2,3,4,5], [3,4,5,6], 0)


6th call

recursive(1, [2,3,4,5], [3,4,5,6], 0)==0
retuns 

7th call 
recursive(1, [2,3,4,5], [3,4,5,6], 0) == 0


8th call 

recursive_knapsack(5, [2,3,4,5],[3,4,5,6], 2)

include = 4 + recursive_knapsack(2, [2,3,4,5],[3,4,5,6], 1)

the include results in  
4 + 3  ==  7


exclude of 5th call 

recursive_knapsack(5, [2,3,4,5],[3,4,5,6], 1) == 3

max(7, 3) == 7



9th call 

recursive_knapsack(2, [2,3,4,5],[3,4,5,6], 1)

include = 3 + recursive_knapsack(0, [2,3,4,5],[3,4,5,6], 0)

include results = 3 + 0


exclude = recursive_knapsack(2, [2,3,4,5],[3,4,5,6], 0) = 3

max is 3


10th call 

recursive_knapsack(0, [2,3,4,5],[3,4,5,6], 0) == 0


11th call 

recursive_knapsack(2, [2,3,4,5],[3,4,5,6], 0) == 0




12th call from 5th call
recursive_knapsack(5, [2,3,4,5],[3,4,5,6], 1)
include = 3 + recursive_knapsack(3, [2,3,4,5],[3,4,5,6], 0)
results 3 + 0


exclude = recursive_knapsack(5, [2,3,4,5],[3,4,5,6], 0) == 0

max is 3



13th call from 9th call

recursive_knapsack(3, [2,3,4,5],[3,4,5,6], 0) == 0
"""


def knapsack(loot, weight_limit):
  grid = [[0 for col in range(weight_limit + 1)] for row in range(len(loot) + 1)]

  # this initializes a 2d list or a matrix where the number of rows will be equal to the number of different weights or the length of loot+1
  # the number of columns is equal to the weight_limit + 1 
  for row, item in enumerate(loot):
    # iterating through per se every weight where by we are shifting the row + 1 since the first row is reserved for 0 where no weight is considered
    # so with this first loop what we are doing is iterating through every row
    row = row + 1
    for col in range(weight_limit + 1):
      # now we shall iterate thought every column in the row 
      # we shall assign the row index to be the weight cap of that row moving from 0 to the weight_cap + 1 
      # which will mean that last column weight limit will be the weight_limit
      weight_capacity = col
      # to check if the item in this row we are iterating can fit within the current column

      if item.weight <= weight_capacity:
        # extraction of weight and value of current item
        item_value = item.value        
        item_weight = item.weight

        """
        This gets the best solution found so far without the current item, at the remaining capacity after including the current item. 
        This means, from the previous row, we look up the maximum value obtained with a reduced capacity (weight_capacity - item_weight).
        """
        # the previous_best_less_item_weight refers to the best solution for the remaining weight capacity after subtracting the current weight
        previous_best_less_item_weight = grid[row - 1][weight_capacity - item_weight]
        # capacity value with item basically is the best value obtained from including the current items value 
        capacity_value_with_item = item_value + previous_best_less_item_weight

        # this is teh value obtained from exluding the current item which is the value from the previous row(best value achieved from the previous row)
        capacity_value_without_item = grid[row - 1][col]

        # max basically compares two of this values 

        grid[row][col] = max(capacity_value_with_item, capacity_value_without_item)
      else:
        grid[row][col] = grid[row - 1][col]
   
  return grid[-1][-1]






def dynamic_knapsack(weight_cap, weights, values):
  rows = len(weights) + 1
  cols = weight_cap + 1
  # Set up 2D array
  # note by in this matrix the rows are made up of the number of items + 1 in the weights 
  # the columns are made up of weight_cap + 1
  # in this case even though you have created the rows as empty lists, the columns are yet to be initialised 
  matrix = [ [0 for y in range(cols)] for x in range(rows) ]
  # Iterate through every row
  for index in range(rows):
    # Initialize columns for this row
    matrix[index] = [ 0 for y in range(cols) ]
    #note the output of this will be like lets say the index is at 0 and weight cap is 4
    """
    [
      [, 0, 0, 0, 0, 0]
    ]"""
    if index == 0:
      continue
    item_weight = weights[index - 1]
    item_value = values[index - 1]
    # Iterate through every column
    for weight in range(cols):
      # Write your code here
      weight_limit = weight
      # the first column will be equal to 0
      if item_weight <= weight_limit:
        previous_best_value = matrix[index - 1][weight_limit - item_weight]
        inclusion_value = item_value + previous_best_value

        declusion_value = matrix[index - 1][weight]
        matrix[index][weight] = max(inclusion_value, declusion_value)
      else:
        matrix[index][weight] = matrix[index - 1][weight]



  # Return the value of the bottom right of matrix
  return matrix[rows-1][weight_cap]

# Use this to test your function:
weight_cap = 150
weights = [31, 10, 20, 19, 4, 3, 6, 15, 3, 5, 6, 7, 8]
values = [70, 20, 39, 37, 7, 5, 10, 6, 7, 8, 9, 10, 11]
print(dynamic_knapsack(weight_cap, weights, values))



# the dynamic knapsack has a runtime of O(n * weight_cap)


# note by the recursive has a runtime of  O(2**n)

