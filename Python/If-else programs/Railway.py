# 13. Railway Ticket Booking Input: 
# ● Age ● Gender ● Ticket class 
# Conditions:
# ● Senior citizen discount 
# ● Female discount 
# ● AC class extra charge Print final fare. 


age=int(input("Enter your age : "))
gender=input("Enter your gender : ").lower()
Ticket_Class=input("Enter your ticket  class : ").upper()

ticket=50
discount=0
if(age>=50):
    discount=ticket*5/100
    ticket-=discount
    print("For Senior Citizen ticket price : ",ticket)

if(gender=="female"):
    discount=ticket*2/100
    ticket-=discount
    print("For Female Ticket price : ",ticket)

if(Ticket_Class=="AC"):
    ticket+=100
    print("For  Ac Ticket : ",ticket)

