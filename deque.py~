from stackArray import MyStack
import random

class deque:
	
	def __init__(self):
		self.deque=MyStack()
		self.temp=MyStack()
		self.deq=self.deque.stack
		
	def size(self):
		return self.deque.size()	
		
	def empty(self):
		return self.deque.isEmpty()
	
	def full(self):
		if (self.deque.size() == self.deque.max_stack_size):
			print ("Stack Full Exception")
			return True
		return False
			
	def insert_at_front(self,value):
		if self.full()!=True:
			for i in range(0,self.deque.size()):
				self.temp.push(self.deque.top())
				self.deque.pop()
			self.temp.push(value)
			for i in range(0,self.temp.size()):
				self.deque.push(self.temp.top())
				self.temp.pop()
			self.deq=self.deque.stack
		else:
			print "Deque Full"
		#print self.deque.stack
	
	def insert_at_last(self,value):
		if self.full()==False:
			self.deque.push(value)
			self.deq=self.deque.stack
		else:
			print "Deque Full"
		#print self.deque.stack
	
	def remove_at_front(self):
		if self.empty()==0:
			for i in range(0,self.deque.size()):
				self.temp.push(self.deque.top())
				self.deque.pop()
			a=self.temp.pop()
			for i in range(0,self.temp.size()):
				self.deque.push(self.temp.top())
				self.temp.pop()
				self.deq=self.deque.stack
			return a
		else:
			print "Deque Empty"	
		#print self.deque.stack
			
	def remove_at_last(self):
		if self.empty()==0:
			a=self.deque.pop()
			self.deq=self.deque.stack
			return a
		else:
			print "Deque Empty"							
		#print self.deque.stack
		
	def shuffle(self):
		random.shuffle(self.deque.stack)
		self.deq=self.deque.stack
		
	def slices(self):
		self.deque.stack=self.deque.stack[0:self.deque.size()]
		self.deq=self.deque.stack	
