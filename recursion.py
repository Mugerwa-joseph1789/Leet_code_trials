#class to give principal and intrest of objects
class Investment:
 def __init__(self,principal,interest):
   self.principal=principal
   self.interest=interest
 def value_after(self):
   n=eval(input("Number of years"))
   return (self.principal*((1+self.interest)**n))
 def __str__(self):
   return 'Principal - ${}, Interest rate - ${}'.format(self.principal,self.interest)

#Class for guessing game
from random import *
class R_P_C:
 def __init__(self,rounds):
  self.rounds=rounds
 def wins(self):
  v=['r','p','s']
  for i in range(self.rounds):
   print('Current is :',i)
   k=choice(v)
   p=input('Enter yur guess')
   
   
c=R_P_C(2)
c.wins()   '''
p=[0,00,14,53,2,5]
print(sorted(p))
