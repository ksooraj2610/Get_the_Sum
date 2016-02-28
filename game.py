from Tkinter import *
from tkMessageBox import *
import os
from stackArray import MyStack
from deque import deque
from queue import MyQueue

class game:

	def __init__(self,value):
		self.val=value
		self.master = Tk()
		self.master.wm_title("Get the Sum....")
		self.master.geometry('2000x1000')
		self.frame = Frame(self.master)
		self.rect=Canvas(self.master,width=2000, height=1000)
		Label(self.rect, text=value,font=(None,15)).grid(row=8,column=60)

		for i in range(0,200):
			Label(self.frame, text="").grid(row=i,column=i)
		for i in range(0,200):
			Label(self.rect, text="").grid(row=i,column=i)
	
		self.rect.grid()	
		self.rect.create_rectangle(176,430,212,586)
		self.rect.create_rectangle(964,430,1002,586)
		self.rect.create_rectangle(360,280,800,320)
		self.rect.grid()
		self.rect.grid()

		self.e1 = Entry(self.rect)
		self.e1.grid(row=31, column=28)
		Button(self.rect, text='Pick',width=16,command=self.pick1).grid(row=30, column=28)
		Button(self.rect, text='Drop',width=16,command=self.drop1).grid(row=32, column=28)
		self.e2 = Entry(self.rect)
		self.e2.grid(row=31, column=95)
		Button(self.rect, text='Pick',width=16,command=self.pick2).grid(row=30, column=95)
		Button(self.rect, text='Drop',width=16,command=self.drop2).grid(row=32, column=95)

		self.p=value
		self.d=deque()
		s=[8,4,2,1,0]
		self.p1=MyStack()
		self.p2=MyStack()
		self.q=MyQueue()
		for j in range(0,5):	
			for i in s:
				self.d.insert_at_last(i)
		self.d.slices()
		self.d.shuffle()
		self.sum1=0
		self.sum2=0
			
	def entry(self,p):
		if p==1:
			n=self.d.remove_at_front()
			self.p1.push(n)
#			print self.d.deq
#			print self.p1.stack[0:self.p1.size()]
			print
			
		if p==2:
			n=self.d.remove_at_last()
			self.p2.push(n)
#			print self.d.deq
#			print self.p2.stack[0:self.p2.size()]
			print
			
	def useless(self,p,no):
		if p==1:
			print 
			n=self.search(no,1)
			if n==no:
				return n
			else:
				return 0	

		
		if p==2:
			print
			n=self.search(no,2)
			if n==no:
				return n
			else:
				return 0

		
	def search(self,e,t):
		if t==1:
			temp=MyStack()
			flag=0
			for i in range(0,self.p1.size()):
				if self.p1.top()==e:
					a=self.p1.pop()
					flag=1
					break
				else:
					temp.push(self.p1.pop())
			for j in range(0,temp.size()):
				self.p1.push(temp.pop())
			if flag==1:
				return a
			else:
				showwarning('Sorry', 'The entered number is not available in your box....')
				return False
							
		if t==2:
			temp=MyStack()
			flag=0
			for i in range(0,self.p2.size()):
				if self.p2.top()==e:
					a=self.p2.pop()
#					print a
					flag=1
					break
				else:
					temp.push(self.p2.pop())
			for j in range(0,temp.size()):
				self.p2.push(temp.pop())
			if flag==1:
				return a
			else:
				showwarning('Sorry', 'The entered number is not available in your box....')
				return False


	def win(self):
		if self.sum1==self.p:
			return 1
				
		if self.sum2==self.p:
			return 2	
	
	def start(self):	
		for i in range(0,5):
			self.d.slices()
			b1=self.d.remove_at_front()
			self.p1.push(b1)
			self.sum1+=b1
			b2=self.d.remove_at_last()
			self.p2.push(b2)
			self.sum2+=b2
			
	def check_empty(self):
		print self.d.deq
		if self.d.empty()==True:
			for i in range(0,self.q.size()):
				self.d.insert_at_front(self.q.dequeue())
			self.d.slices()
			self.d.shuffle()
			self.update()

	def clear(self):
		for i in range(27,21,-1):
			Label(self.rect,text='   ',font = (None,12)).grid(row=i,column=28)
		for i in range(27,21,-1):
			Label(self.rect,text='   ',font = (None,12)).grid(row=i,column=95)
		for i in range(53, 68):
			Label(self.rect,text='    ',font = (None,15)).grid(row=15,column=i)

	def update(self):
		for i,j in zip(self.p1.stack[0:self.p1.size()],range(27,21,-1)):
			Label(self.rect,text=i,font = (None,12)).grid(row=j,column=28)
		for i,j in zip(self.p2.stack[0:self.p2.size()],range(27,21,-1)):
			Label(self.rect,text=i,font = (None,12)).grid(row=j,column=95)
		for i, j in zip(self.d.deq[0:self.d.size()], range(53, 68)):
			Label(self.rect,text=str(i)+' ',font = (None,15)).grid(row=15,column=j)
		
	def winner(self):
		if self.win()==1:
			showinfo('Game Over','Player 1 has won')

		if self.win()==2:
			showinfo('Game Over','Player 2 has won')

	def pick1(self):
		self.entry(1)
		self.sum1+=self.p1.top()
		self.clear()
		self.update()
		self.check_empty()
	
	def drop1(self):
		no=int(self.e1.get())
		val=self.useless(1,no)
		self.sum1-=val
		if no==val:
			self.q.enqueue(val)
		print self.q.queue	
		self.clear()
		self.update()
		self.winner()

	
	def pick2(self):
		self.entry(2)
		self.sum2+=self.p2.top()
		self.clear()
		self.update()
		self.check_empty()
	
	def drop2(self):
		no=int(self.e2.get())	
		val=self.useless(2,no)
		self.sum2-=val
		if no==val:
			self.q.enqueue(val)
		print self.q.queue
		self.clear()
		self.update()
		self.winner()
