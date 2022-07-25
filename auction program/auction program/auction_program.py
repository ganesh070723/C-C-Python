
from os import system
#HINT: You can call clear() to clear the output in the console.
bid={}

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
  
  
print(logo)

continuee = True
while continuee==True:
  name=input("enter the name of the bider : ")
  ammount=int(input("ammount $"))
  bid[name]= ammount
  add_bidders=input("if there any biders ? type yes or no : ")
  if add_bidders=='yes':
    
    print(logo)
    continuee=True
  else:
     highest=0
     winner=''
     for a in bid:
       
       if bid[a]>highest:
         highest=bid[a]
         winner=a
     print(f"The winner is {winner} and his/her bid is {highest}")
     continuee=False