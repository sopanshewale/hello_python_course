import sys
from chessboard import chessboard

x = int(sys.argv[1])
y = int(sys.argv[2])

print ("Knight will be placed at: ", x, y)
b = chessboard()
placed = b.place_knight(x, y)
if placed: 
   print(b)
else: 
   print ("There was error")

print (b.number_of_moves(5, 1))
