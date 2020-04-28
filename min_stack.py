"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2"""



class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x: int) -> None:
        """
        push method will add two items each time into the stack
        Item itself and minimum values compariing with the last item 
        So, always last item's 2nd element will have the minimum value for the complete stack
        stack[-1][-1]
        """
        #Checking if the stack is empty
        if len(self.stack):        
            self.stack.append((x, min(x, self.stack[-1][-1])))
        
        # else stmt will cause entry for the 1st item 
        else:
            self.stack.append((x, x))

    def pop(self) -> None:
        #Checking if the stack is empty
        if len(self.stack):
            self.stack.pop()

    def top(self) -> int:
        #Checking if the stack is empty
        if len(self.stack):
            return self.stack[-1][0]

    def getMin(self) -> int:
        #Checking if the stack is empty
        if len(self.stack):
            return self.stack[-1][-1]
