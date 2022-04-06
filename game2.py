import random

computer1=["🤚🏻","✋🏻"]
computer2=["🤚🏻","✋🏻"]
i=0
c1=0
c2=0
us=0
while i<5:

    user=input("please enter 🤚🏻 , ✋🏻 :")

    chancecomputer1=random.choice(computer1)
    chancecomputer2=random.choice(computer2)

    if user==chancecomputer1:
        if chancecomputer2!=user:
            c2=c2+1
            print("computer2:"+chancecomputer2)
            print(c2)
            i=i+1
        else:
            i=i+1
            continue

    elif user==chancecomputer2:
        if chancecomputer1!=user:
            c1=c1+1
            print("computer1:"+chancecomputer1)
            print(c1)
            i=i+1
        else:
            i=i+1
            continue

    if chancecomputer2==chancecomputer1:
        if user!=chancecomputer2:
            us=us+1
            print("user:"+user)
            print(us)
            i=i+1
        else:
            i=i+1
            continue
        
print("computer1:"+str(c1),"computer2:"+str(c2),"user:"+str(us))
print("winer:",max(c1,c2,us))