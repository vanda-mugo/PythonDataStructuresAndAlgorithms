"""
Recursion is made possible with call stacks and execution context. It requires a function invoking itself with different arguments 
note by this is made possible by the class stack
recall that stacks operate in a lifo basis 
languages then make this poossible by the call stack and the execution context 

execution context can be thought of as the specific values we plug into a function call. this is the state which a function call is executed.
eg including details like 
local variables , parameters return address and call stack 

in terms of call stack note that each time a function is called (whether recursively or not ) an execution context (or stack frame ) is created 
and pushed onto the stack . When the function returns its context is popped off the stack. A new execution context also called a 'stack frame'
is created and placed on top of teh call stack for each recursive call.

this context keeps track of the current state (eg local variables, parameters )
it also points in the function where the next instruction will execute  when it returns 
when base case is reached , the recursive calls start to return and the stack frames are popped off the stack in reverse order (lifo)




recursion has two fundamental aspects 

the base case and the recursive step 


The base case dictates whether the function will recurse, or call itself. Without a base case, it’s the iterative equivalent to writing an infinite loop. 
Because we’re using a call stack to track the function calls, your computer will throw an error due to a stack overflow if the base case is not sufficient.
In an iterative function, this is handled by a loop construct that decrements or increments the counting variable which moves the counter closer to a boolean condition, 
terminating the loop. 

In a recursive function, the “counting variable” equivalent is the argument to the recursive call. If we’re counting down to 0, for example, 
our base case would be the function call that receives 0 as an argument. 
We might design a recursive step that takes the argument passed in, decrements it by one, and calls the function again with the decremented argument. 
In this way, we would be moving towards 0 as our base case.

Analyzing the Big O
Preview: Docs Runtime is the period of time during which a program is running.
runtime
of a recursive function is very similar to analyzing an iterative function. Substitute iterations of a loop with recursive calls. 

For example, if we loop through once for each element printing the value, we have a O(N) or linear runtime. Similarly, 
if we have a single recursive call for each element in the original function call, we have a O(N) or linear runtime.

"""


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

factorial(3)


"""
For factorial(3), an execution context is created and pushed onto the stack.
This then calls factorial(2), and another execution context is pushed onto the stack.
factorial(2) calls factorial(1), and the final context is pushed onto the stack.
Once the base case (factorial(1)) is reached, it returns 1 and starts popping the contexts off the stack, completing each previous call in reverse order.


you can think of it like this 

first call stack frame to be placed on the call stack factorial(3) and it will return 3 * factorial(2)

factorial(2) is now placed in the call stack and returns  2 * factorial(1)

since factorial(1 ) basically gets to the base case then it returns 1 from the factorial(1 ) call and this is now passed onto the 
call stack for the second frame in the stack 

factorial(2) was returning 2 * factorial(1) hence return 2 * 1  hence 2

and factorial 3 was returning 3 *factorial(2) = 3 * 2  = 6


Key Points:

    Stack frames grow with each recursive call.
    Once the base case is reached, the stack unwinds, and each function's execution context is popped off the stack.
"""
