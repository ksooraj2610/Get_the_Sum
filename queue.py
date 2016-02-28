"""The code has been developed by Dr.Vidhya Balasubramanian as part of the CSE230 Data Structures Course, ASE Coimbatore.
   The code is being constantly improved, so please bring to notice any bugs to dsdaa.amrita@gmail.com
   
"""
class MyQueue():
    
    def __init__(self):
        # this is the queue container called 'queue'
        self.queue = []
        self.siz=0
        # front and back indexes
        self.f = -1
        self.r = -1
        # define the queue size 'max_queue_size' and initialize it
        self.max_queue_size = 50
        for i in range(0,self.max_queue_size):
            self.queue.append(None)

    # define the enqueue operation which inserts the value into the queue, must throw a queue full exception
    def enqueue(self, value):
        if (self.size() == self.max_queue_size):
            print("Overflow")
        else:
            if (self.f<0):
                self.f= self.f+1
                self.r = self.r+1
                self.queue[self.r] = value
            else:
                self.r = (self.r+1)%self.max_queue_size
                self.queue[self.r] = value
            self.siz+=1    
    # returns first elt of the queue if not empty, else throws queue empty
    # exception
    
    def dequeue(self):
        #if (self.f==self.r):
        if (self.size() == 0):
            return "Queue Empty Exception"
        else:
            obj = self.queue[self.f]
            self.queue[self.f] = None                
            self.f = (self.f+1)%self.max_queue_size            
            #if (self.f<self.max_queue_size):
            self.siz-=1
            #else:
            #    self.f = (self.f+1)%self.max_queue_size
            return obj
    
    # returns front element without removing it if the queue is not empty, else throws exception   
    def front(self):
        if (self.size()!=0):
            print ("returning front element")
            return self.queue[self.f]
        return "Queue Empty Exception"
     
    # returns the number of elements currently in queue
    def isEmpty(self):
        if (self.size!=0):
            print ("Queue not empty")
            return False
        return True

    
    # returns True if queue is empty
    def size(self):
        return self.siz
