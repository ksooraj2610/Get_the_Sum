from game import game	
import os
os.system('clear')
print
print
print "\t\t\t\t\t\t\tGET THE SUM (If You Can....)"
print
print
p1=raw_input("Enter the Name of Player 1 : ")
print
p2=raw_input("Enter the Name of Player 2 : ")
print
print
print
print
print "  Rules:"
print
print "\t (i) There will be a target Sum that has to be achieved to win this game."
print "\t (ii) Both players will be having 5 numbered balls each in their respective boxes."
print "\t (iii) If the sum of those gets added up to the target number,then the player wins ."
print "\t (iv) Else that player has to pick one ball from the pipe and discard the unnecessary ball so that 5 balls will be remaining."
print "\t (v) If the player achieves the target sum , he will be the winner else keep going on until anyone wins the game."
print "\t (vi) Be careful at your calculations."
print "\t (vii) Each time when you drop a ball your sum will be updated in the window for your convenience"
print "\t (viii) Good Luck...."
print
print
print
print
print
print
raw_input("\tPress any key to start the game....") 
ob=game(p1,p2)
ob.play()
os.system("clear")
