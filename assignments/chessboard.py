'''
Chessboard class to solve:
 [1] Knight Tour Problem 
 [2] 8-Queen Problem 
 [3] Demonstrate the use of Backtracking problem solving technique
'''

class chessboard(object):
    def __init__(self):
         self.board = [
                        [0, 0, 0, 0, 0, 0, 0, 0],  
                        [0, 0, 0, 0, 0, 0, 0, 0],  
                        [0, 0, 0, 0, 0, 0, 0, 0],  
                        [0, 0, 0, 0, 0, 0, 0, 0],  
                        [0, 0, 0, 0, 0, 0, 0, 0],  
                        [0, 0, 0, 0, 0, 0, 0, 0],  
                        [0, 0, 0, 0, 0, 0, 0, 0],  
                        [0, 0, 0, 0, 0, 0, 0, 0] 
                      ]
         self.knight = 0
         self.tour = {} 



    def place_knight(self, row, col):
         if row < 0 or row > 7 or col <0 or col > 7:
            print ("Wrong Move")
            return False 
         if self.board[row][col] != 0:
            print ("Wrong Move - Knight already placed there")
            return False   
      
         self.knight +=1 
         self.board[row][col] = self.knight
         self.tour[self.knight] = [row, col]
         return True 

    def current_position(self):
        if len(self.tour) == 0:
            return None
        return self.tour[self.knight] 

    def next_possible_moves(self):
       c = self.tour[self.knight] # handle empty 
       moves = []
       moves.append([c[0]+2, c[1]+1]) 
       moves.append([c[0]+2, c[1]-1]) 
       moves.append([c[0]+1, c[1]-2]) 
       moves.append([c[0]-1, c[1]-2]) 
       moves.append([c[0]-2, c[1]-1]) 
       moves.append([c[0]-2, c[1]+1]) 
       moves.append([c[0]-1, c[1]+2]) 
       moves.append([c[0]+1, c[1]+2]) 
       return moves

  
    def remove_knight(self):
        pass  
         
    def __repr__(self):
         rep = ''
         for row in self.board:
               rep = rep + '\n'
               for c in row:
                   rep = rep + ' ' + str(c)
         #How about printing path too
         line = '\n' + '-' * 80 + '\n'
         rep = rep + line 
         for i in range(1, self.knight+1):
             rep = rep + ' ' + "({},{})".format(self.tour[i][0], self.tour[i][1])
         return rep 


