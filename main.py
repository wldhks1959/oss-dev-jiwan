#동혁이가 발견한 흰색 피스의 개수
# king,queen,rook,knight,bishop,pawn
piece=[]
p_piece=[]
A={'king' : 1 ,
   'queen' : 1 ,
   'rook' : 2 ,
   'knight' : 2 ,
   'bishop' : 2 ,
   'pawn' : 8 ,
   }
A_values=list(A.values())
piece=(list(map(int,input().split())))
for i in range(6):
   if(piece[i]==A_values[i]):
      p_piece.append(0)
   else :
      p_piece.append(A_values[i]-piece[i])
for i in range(6):
   print(p_piece[i], end=" ")