import random
user=input("enter your choice")
computer=["rock","scissor","paper"]
computer_out=random.choice(computer)
if(user==computer_out):
    print("both choice is same,so tie")
elif(user=="rock"):
    if(computer_out=="paper"):
        print("paper smash the rock,computer wins")
    else:
        print("user lose")
elif(user=="scissor"):
    if(computer_out=="paper"):
        print("scissor cuts paper, user wins")
    else:
        print("computer lose")
elif(user=="rock"):
    if(computer_out=="scissor"):
        print("rock smash the scissor,user wins")
    else:
        print("computer lose")
