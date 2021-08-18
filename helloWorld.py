#Program to turn a number to base20 numbers
def rec(n):
  d=[]
  p=n//20
  c=n%20
  d.append(c)
  while(1):
   if p<20:
    d.insert(0,p)
    break
   d.insert(0,p%20) 
   p=p//20
  u=[]
  m=''
  f=0
  a={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19}
  u=list(a.items())  
  for o in d:  
    for i in u:
      if i[1]==o:
       m+=i[0]
  print(m)      
n=eval(input('Your number,n '))
rec(n)  

#function finds the digital root of a number
def dig_root(n):
  d=0
  p=0
  r=str(n)
  while(1):
    p=0
    for i in r:
       p+=int(i)    
    d=len(str(p))
    if d==1:
      break
    else:  
      r=str(p)
  print(p)     
dig_root(458931)

#function to generate the factorial of a number
def fact(x):
    if(x==1):
      return 1
    else:
      a=x*fact(x-1)
      return a
#function does binomial expansion
def binom(n,k):
  c=n-k
  a=fact(n)
  b=fact(k)
  d=fact(c)
  print(a/(b*c))
binom(8,4)

#function tells if a number has a zero at the start
def digi(n):
  d=str(n)
  i=0
  if d[i]==0:
   print("Not valid")
  else:
      print(n)
          

#Program returns occurrencies of a given element in a string      
def findo(stri,g):
    h=[]
    if g not in stri:
     return h
    else:
     for i in range(len(stri)):
      if stri[i]==g:
       h.append(i)
     print(h)     
findo('appale','a')

#Program to calculate the root of any number...default return is squareroot
def root(x,n=2):
 print(x**(1/n))
root(8,3)         

#Program to Automatically generate Sudoku'''
from random import randint
def Sud():
 l=[[0 for i in range(9)] for j in range(9)]
 m=[0 for i in range(9)]
 w=[0 for i in range(9)]
 e=[0 for i in range(9)]
 t=[0 for i in range(9)]
 p=[0 for i in range(9)]
 s=[0 for i in range(9)]
 x=[0 for i in range(9)]
 y=[0 for i in range(9)]
 r=[0 for i in range(9)]
 f=[]
 M=[0 for i in range(9)]
 A=[]
 j=0
 i=0
 a=0
 b=0
 c=0
 d=0
 g=0
 h=0
 n=0
 z=0
 q=0
 v=0
 for u in range(9):
   for p in range(9):
     print(l[u][p],end=" ")
   print() 
 print('----------------_______________--------------') 
 while i<9:
   while j<9:
    if i<3 and j<3:#Share memory location
     m[a]=l[i][j]
     a+=1      
    elif i<3 and j<6: 
     w[b]=l[i][j]
     b+=1  
    elif i<3 and j<9:
     e[c]=l[i][j]
     c+=1 
    elif i<6 and j<3:
     t[d]=l[i][j]
     d+=1    
    elif i<6 and j<6:
     p[g]=l[i][j] 
     g+=1 
    elif i<6 and j<9:
     s[h]=l[i][j]
     h+=1    
    elif i<9 and j<3:
     u[z]=l[i][j]
     z+=1  
    elif i<9 and j<6:
     y[q]=l[i][j]
     q+=1  
    else: 
     r[v]=l[i][j]
     v+=1  
    j+=1
   i+=1  
 while j<9:
  for i in range(9):
   M[i]=l[i][j] 
  f.append(M)
  j+=1
 j=0 
 while j<9:
  for i in range(9):
   M[i]=l[j][i] 
  A.append(M)
  j+=1 
 i=0
 while i<9:
  for j in range(9):
   k=randint(1,9)
   print(i,j,m,k) 
   if i<3 and j<3 and m.count(k)<=1 and k not in A[j] and k not in f[i]:
     l[i][j]=k
   elif i<3 and j<6 and w.count(k)<=1 and k not in A[j]and k not in f[i]:
     l[i][j]=k 
   elif i<3 and j<9 and e.count(k)<=1 and k not in A[j] and k not in f[i]:
     l[i][j]=k
   elif i<6 and j<3 and t.count(k)<=1 and k not in A[j] and k not in f[i]:
     l[i][j]=k    
   elif i<6 and j<6 and p.count(k)<=1 and k not in A[j] and k not in f[i]:
     l[i][j]=k     
   elif i<6 and j<9 and s.count(k)<=1 and k not in A[j] and k not in f[i]:
     l[i][j]=k    
   elif i<9 and j<3 and x.count(k)<=1 and k not in A[j] and k not in f[i]:
     l[i][j]=k    
   elif i<9 and j<6 and y.count(k)<=1 and k not in A[j] and k not in f[i]:
     l[i][j]=k     
   elif i<9 and j<9 and r.count(k)<=1 and k not in A[j] and k not in f[i]:
     l[i][j]=k
   else:
    i-=1
   
  i+=1  
 

 for i in range(9):
  for j in range(9):
    print(l[u][p],end=" ")
  print() 
       
Sud()






























