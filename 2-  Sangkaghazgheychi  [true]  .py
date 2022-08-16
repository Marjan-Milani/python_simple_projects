import random
x=input("Enter Rock/Paper/Scissor:")
print("your choice is",x)
p=random.randint(0,2)
if p==0:
    print("Pc's choice is Rock")
if p==1:
    print("Pc's choice is Paper")
if p==2:
    print("Pc's choice is Scissor")
if (x=="Rock") and p==0 or (x=="Paper") and p==1 or (x=="Scissor") and p==2:
    print("Draw")
if(x=="Rock") and p==2 or (x=="Paper") and p==0 or (x=="Scissor") and p==1:
    print("You are winner")
if(x=="Rock") and p==1 or (x=="Paper") and p==2 or (x=="Scissor") and p==0:
    print("pc is winner")
