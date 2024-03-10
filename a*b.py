 1 def cal(A,B):
  2     # A*B
  3     # = A+A*(B-1)
  4     if(B == 1):
  5         return A
  6     else:
  7         return A + cal(A, B-1)
  8 print("This program cna calculate A times B")
  9 A=int(input("A: "))
 10 B=int(input("B: "))
 11 print(cal(A,B))

