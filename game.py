from Tkinter import *
from tkMessageBox import *
from random import *
from stackArray import MyStack
from deque import deque
from queue import MyQueue

class game:
	
	def __init__(self,n1,n2):
		self.master = Tk()
		self.master.wm_title("Get the Sum....")
		self.master.geometry('2000x1000')
		self.frame = Frame(self.master)
		self.rect=Canvas(self.master,bg='blue',width=2000, height=1000)
		self.n1=n1
		self.n2=n2
		
	def play(self):
		self.start()
		
	def entry(self,p):
		if p==1:
			n=self.d.remove_at_front()
			self.p1.push(n)
			print
			
		if p==2:
			n=self.d.remove_at_last()
			self.p2.push(n)
			print

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
				self.e1.delete(0, 'end')
				return 0
							
		if t==2:
			temp=MyStack()
			flag=0
			for i in range(0,self.p2.size()):
				if self.p2.top()==e:
					a=self.p2.pop()
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
				self.e2.delete(0, 'end')
				return 0


	def win(self):
		if self.sum1==self.p:
			return 1
				
		if self.sum2==self.p:
			return 2	
	
	def start(self):
		filename1 = PhotoImage(file = "1.png")
		filename2 = PhotoImage(file = "2.PNG")
		self.rect.create_image(200, 400, image=filename1)
		self.rect.create_image(980, 400, image=filename2)
		self.rect.pack(expand = YES, fill = BOTH)
#		self.rect.destroy()
		value=randint(10,30)
		self.turn=0
		self.countp=0
		self.countd=0
		self.val=value
#		self.rect.grid()
		
#		for i in range(0,200):
#			Label(self.frame, text="").grid(row=i,column=i)
		for i in range(0,200):
			Label(self.rect, text="",bg='blue').grid(row=i,column=i)
		
		Label(self.rect, text=value,font=(None,15),bg='white').grid(row=8,column=60)
		self.rect.grid()	
		self.rect.create_rectangle(178,442,212,586,fill='white')
		self.rect.create_rectangle(966,442,1002,586,fill='white')
		self.rect.create_rectangle(360,280,800,320,fill='white')
		self.rect.grid()
		self.rect.grid()

		self.e1 = Entry(self.rect)
		self.e1.grid(row=31, column=28)
		Button(self.rect, text='Pick',bg='orange',width=16,command=self.pick1).grid(row=30, column=28)
		Button(self.rect, text='Drop',bg='green',width=16,command=self.drop1).grid(row=32, column=28)
		Label(self.rect,text=self.n1,font=(None,15),bg='blue',fg='yellow').grid(row=34,column=28)
		
		self.e2 = Entry(self.rect)
		self.e2.grid(row=31, column=95)
		Button(self.rect, text='Pick',bg='orange',width=16,command=self.pick2).grid(row=30, column=95)
		Button(self.rect, text='Drop',bg='green',width=16,command=self.drop2).grid(row=32, column=95)
		Label(self.rect,text=self.n2,font=(None,15),bg='blue',fg='yellow').grid(row=34,column=95)
		
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

		for i in range(0,5):
			self.d.slices()
			b1=self.d.remove_at_front()
			self.p1.push(b1)
			self.sum1+=b1
			b2=self.d.remove_at_last()
			self.p2.push(b2)
			self.sum2+=b2
		
		Label(self.rect,text=self.sum1,font=(None,12),bg='blue',fg='white').grid(row=35,column=28,pady=5)
		Label(self.rect,text=self.sum2,font=(None,12),bg='blue',fg='white').grid(row=35,column=95,pady=5)
	
		self.clear()
		self.update()
		self.winner()
		self.rect.mainloop()
			
	def check_empty(self):
		#print self.d.deq
		if self.d.empty()==True:
			for i in range(0,self.q.size()):
				self.d.insert_at_front(self.q.dequeue())
			self.d.slices()
			self.d.shuffle()
			self.update()

	def clear(self):
		for i in range(28,22,-1):
			Label(self.rect,text='   ',font = (None,12),bg='white').grid(row=i,column=28)
		for i in range(28,22,-1):
			Label(self.rect,text='   ',font = (None,12),bg='white').grid(row=i,column=95)
		for i in range(53, 68):
			Label(self.rect,text='    ',font = (None,15),bg='white').grid(row=15,column=i)

	def update(self):
		for i,j in zip(self.p1.stack[0:self.p1.size()],range(28,22,-1)):
			Label(self.rect,text=i,font = (None,12),bg='white').grid(row=j,column=28)
		for i,j in zip(self.p2.stack[0:self.p2.size()],range(28,22,-1)):
			Label(self.rect,text=i,font = (None,12),bg='white').grid(row=j,column=95)
		for i, j in zip(self.d.deq[0:self.d.size()], range(53, 68)):
			Label(self.rect,text=str(i)+' ',font = (None,15),bg='white').grid(row=15,column=j)
		
	def winner(self):
		if self.win()==1:
			a="Congrats.. "+ self.n1 + " has won"
			showinfo('Game Over',a)
			self.rect.quit()

		if self.win()==2:
			a="Congrats.. "+ self.n2 + " has won"
			showinfo('Game Over',a)
			self.rect.quit()
			
	def pick1(self):
		if self.turn % 2==0:
			if self.countp % 2==0 and self.countd % 2==0:
				self.entry(1)
				self.sum1+=self.p1.top()
				self.clear()
				self.update()
				self.check_empty()
				self.countp+=1
				
			elif self.countp % 2 !=0 and self.countd % 2==0: 
				showwarning(self.n1, "You have already picked a ball.... ")					
		else:
			b="It's "+self.n2+"'s Turn"
			showwarning('Oops..',b)
			
	def drop1(self):
		if self.turn % 2 ==0:
			if self.countp % 2!=0 and self.countd % 2==0:
				if self.e1.get().isdigit()==True:
					no=int(self.e1.get())
					self.e1.delete(0, 'end')
					val=self.search(no,1)
					self.sum1-=val
					Label(self.rect,text="   ",font=(None,12),bg='blue',fg='white').grid(row=35,column=28,pady=7)
					Label(self.rect,text=self.sum1,font=(None,12),bg='blue',fg='white').grid(row=35,column=28,pady=7)
					if no==val:
						self.q.enqueue(val)
						#print self.q.queue	
						self.clear()
						self.update()
						self.winner()
						self.countd+=1
				else:
					showwarning('Attention!!!', "You have to enter an integer. ")		
					self.e1.delete(0, 'end')
					
			elif self.countp % 2==0	and self.countd % 2==0 :
				showwarning('Sorry....', "You have to pick a ball first before dropping one. ")
				self.e1.delete(0, 'end')
		
			if self.countp % 2!=0 and self.countd % 2!=0:
				self.turn+=1
		
		else:
			b="It's "+self.n2+"'s Turn"
			showwarning('Oops..',b)
			self.e1.delete(0, 'end')		
		self.e1.delete(0, 'end')
		self.e2.delete(0, 'end')	
	
	def pick2(self):
		if self.turn % 2!=0:
			if self.countp % 2!=0 and self.countd % 2!=0:
				self.entry(2)
				self.sum2+=self.p2.top()
				self.clear()
				self.update()
				self.check_empty()
				self.countp+=1
				
			elif self.countp % 2 ==0 and self.countd % 2!=0: 
				showwarning(self.n2, "You have already picked a ball.... ")					
		else:
			b="It's "+self.n1+"'s Turn"
			showwarning('Oops..',b)	
	
	def drop2(self):
		if self.turn % 2 ==1:
			if self.countp % 2==0 and self.countd % 2!=0:
				if self.e2.get().isdigit()==True:
					no=int(self.e2.get())
					self.e2.delete(0, 'end')	
					val=self.search(no,2)
					self.sum2-=val
					Label(self.rect,text="   ",font=(None,12),bg='blue',fg='white').grid(row=35,column=95,pady=7)
					Label(self.rect,text=self.sum2,font=(None,12),bg='blue',fg='white').grid(row=35,column=95,pady=7)
					if no==val:
						self.q.enqueue(val)
						#print self.q.queue
						self.clear()
						self.update()
						self.winner()
						self.countd+=1
				else:
					showwarning('Attention!!!', "You have to enter an integer. ")		
					self.e2.delete(0, 'end')		
					
			elif self.countp % 2!=0	and self.countd % 2!=0 :
				showwarning('Sorry....', "You have to pick a ball first before dropping one. ")
				self.e2.delete(0, 'end')
		
			if self.countp % 2==0 and self.countd % 2==0:
				self.turn+=1
		
		else:
			b="It's "+self.n1+"'s Turn"
			showwarning('Oops..', b)
			self.e2.delete(0, 'end')
		self.e1.delete(0, 'end')
		self.e2.delete(0, 'end')
