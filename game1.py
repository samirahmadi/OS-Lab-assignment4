import random

options=["rock","paper","scissor"]
computer_score=0
user_score=0

for i in range(10):
    computer_choice=random.choice(options)
    user_choice=input("enter option:")

    if user_choice=="paper" and computer_choice=="rock":
       print("user_choice:",computer_choice)
       user_score+=1
       print ("computer_score:",computer_score)

    elif user_choice=="paper" and computer_choice=="scissor":
        print("computer_choice:",computer_choice)
        computer_score+=1
        print ("computer_score:",computer_score)

    elif user_choice=="rock" and computer_choice=="scissor":
        print("user_choice:",computer_choice)
        user_score+=1
        print ("user_score:",user_score)

    elif user_choice=="rock" and computer_choice=="paper":
        print("computer_choice:",computer_choice)
        computer_score+=1
        print ("computer_score:",computer_score)

    elif user_choice=="scissor" and computer_choice=="paper":
        print("user_choice:",computer_choice)
        user_score+=1
        print ("user_score:",user_score)

    elif user_choice=="scissor" and computer_choice=="rock":
        print("computer_choice:",computer_choice)
        computer_score+=1
        print ("computer_score:",computer_score)

    elif user_choice==computer_choice:
        i+=1
        continue
print ("winer:",max(user_score,computer_score))
    



    



