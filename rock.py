from operator import truediv
import random
def play():
    comp=random.choice(['r','p','s'])
    user=input("ENter r for rock,, s for scissors and p for paper")
    if user==comp:
        return 'TIE'
    if iswin(user,comp):
        return 'WON'
    else:
        return 'LOST'
def iswin(p1,p2):
    if(p1=='r' and p2=='s') or (p1=='s' and p2=='p') or (p1=='p' and p2=='r'):
        return True
    else:
        return False
print(play())




