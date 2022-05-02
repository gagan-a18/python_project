import random
from re import X

def cguess(x):
    print("\n")
    low=0
    high=x
    feedback=''
    while feedback!='c' and low!=high:
        random_n = random.randint(low,high)
        print(f'Guessed number by computer is {random_n}')
        f=input(f'''This is the feedback I was talking about,Is {random_n} guessed by computer too high(h),too low(l) or correct(c)\n''')
        if f =='h':
            high=random_n-1
            print(f'Input given was {f}\n')
        elif f =='l':
            low=random_n+1
            print(f'Input given was {f}\n')
        else:
            break
    if low==high:
        low=0
        print("Computer could not guess the number")
    else:
        print(f'guessed {random_n} correctly ')
'''rand=random.randint(1,100)
print(f"A little secret in here,computer does'nt know that secret number\n")
print(f'Secret number is {rand}')'''
cguess(100)
