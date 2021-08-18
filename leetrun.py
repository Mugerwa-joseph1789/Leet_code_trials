#class for objects intending to compare strings
class Iso:
 def __init__(self,w,h):
  self.w=w
  self.h=h

 def test(self):
  if len(self.h)==len(self.w):
   return 2>1 
  else:
   return 1>1 
obj=Iso(w=input("your string :"),h=input("Second: "))
print(obj.test())

#Return longest palindrome/substring in strinG
from itertools import *
class Pali:
 def __init__(self,string):
  self.string=string
 
 def perms(self):
  g=[]
  r=[]
  t=[]
  i=2
  while i<len(self.string):
   g=[''.join(k) for k in permutations(self.string ,i)]
   s=g
   r.append(s)
   i+=1
  print((r))
  for i in r:
   for y in i:
    if i.count(y)>=1 and y not in t and y in self.string and y[:]==y[::-1]:
     t.append(y)
  print()
  print(t)
  a=''
  for i in t:
    if len(i)>=len(a):
     a=i 
  print(a)   
obj=Pali('abcabcbb')
obj.perms()

#Return substring/palindrome in string
from itertools import *
class Pali:
 def __init__(self,string):
  self.string=string
 
 def perms(self):
  g=[]
  r=[]
  t=[]
  i=2
  while i<len(self.string):
   g=[''.join(k) for k in permutations(self.string ,i)]
   s=g
   r.append(s)
   i+=1
  print((r))
  for i in r:
   for y in i:
    if i.count(y)>=1 and y not in t and self.string.count(y)>=1:
     t.append(y)
  print()
  print(t)
  a=''
  for i in t:
    if self.string.count(i)>1 and len(i)>len(a):
     a=i 
  print(a,len(a))   
obj=Pali('abcabcbbd')
obj.perms()

class Tir:
 def __init__(self,string):
  self.string=string
  
 def com(self):
  s=''
  w=[]
  r=list(self.string)
  for i in r:
   s+=i
   if self.string.count(s)>1:
    w.append(s)
  print(w)
  d=''
  for i in w:
   if len(i)>len(d):
      d=i
  print(d)    
co=Tir("abcabcbb")
co.com()

#Calculate Median class
class Med:
 def __init__(self,a1,a2):
  self.a=a1
  self.b=a2
  
 def me(self):
  g=[]
  for i in self.b:
   self.a.append(i)
  self.a.sort() 
  if len(self.a)%2==0:
   c=int(len(self.a)/2)
   print('{} is mediano'.format((self.a[c-1]+self.a[c])/2))
  else:
   d=(len(self.a)/2)+.5
   d=d-1
   print('{} is median '.format((self.a[int(d)])))
de=Med([4,2],[3,1,5])
de.me()

#Generate levels of Pascal's triangle
class Pascal:
 def __init__(self,t):
  self.t=t
  
 def fact(self,y):
  if y==1 or y==0:
   return 1
  else:
   d=y*self.fact(y-1)
   return d
   
 def war(self): 
  n=self.t
  a=self.t*self.fact(n-1) 
  pe=[]
  r=[]
  if n==1:
   print("Pascals has [1] at level 1")
  else:
   v=0
   while v<=n:
    i=0
    while i<=v:
     p=v-i
     o=self.fact(p)
     k=self.fact(i)
     w=((self.fact(v))/(o*k))
     r.append(int(w))
     i+=1
    v+=1
   print(r)
d=Pascal(eval(input("Level of Pascal's needed :")))
d.war()

#Program that gives labels to excel sheets.
class Excel:
 def __init__(self,n):
  self.n=n.upper()
  
 def sh(self):
  s='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  a=[i for i in range(1,27)]
  t=list(s)
  d={}
  for i in range(len(s)):
   d[t[i]]=a[i]
  print(d)
  u=self.n
  p=list(u)
  print(p)
  v=0
  for i in range(len(p)-1):
   v+=(26*d[p[i]])
   print(v)
  v+=d[p[len(p)-1]] 
  print(v,'hh')

c=Excel('abcde')
c.sh()


























