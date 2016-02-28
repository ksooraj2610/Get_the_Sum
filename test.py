from random import *
from game import game

p=randint(10,40)		
ob=game(p)
print ob.d.deq

ob.start()
ob.clear()
ob.update()
ob.winner()


ob.master.mainloop( )

