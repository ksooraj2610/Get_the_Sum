"""The code has been developed by Dr.Vidhya Balasubramanian as part of the CSE230 Data Structures Course, ASE Coimbatore.
   The code is being constantly improved, so please bring to notice any bugs to dsdaa.amrita@gmail.com
   
"""
class MyStack():
    
    def __init__(self):
        self.stack = []
        # this is the stack container called 'stack'
        self.max_stack_size = 25
        for i in range(self.max_stack_size):
            self.stack.append("none")
        # define the stack size 'max_stack_size' and initialize it
        self.t = -1
        #print self.stack

    # define the push operation which  pushes the value into the stack, must throw a stack full exception
    def push(self, value):
        if (self.size() == self.max_stack_size):
            print ("Stack Full Exception")
        else:
            self.t= self.t+1
            self.stack[self.t] = value
        return
        

    # returns top element of stack if not empty, else throws stack empty exception
    def pop(self):
        if (self.size() == 0):
            print ("Stack Empty Exception")
            return
        else:
            toret = self.stack[self.t]
            self.stack[self.t] = None
            self.t = self.t-1
            return toret
        
        
    # returns top element without removing it if the stack is not empty, else throws exception   
    def top(self):
        if (self.size() == 0):
            print ("Stack Empty Exception")
            return
        else:
            return self.stack[self.t]
        

    # returns True if stack is empty   
    def isEmpty(self):
        return  (self.t<0)
        
    # returns the number of elements currently in stack 
    def size(self):
        return self.t+1


