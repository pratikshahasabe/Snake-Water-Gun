import random

def gamewin(comp,you):
    if comp==you:
        return 0
    if comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True
    elif comp=='w':
        if you=='g':
            return False
        elif you=='s':
            return True
    elif comp=='g':
        if you=='s':
            return False
        elif you=='w':
            return True

print("Computer Turn: Snake(s),Water(w),Gun(g) ?")
randno=random.randint(1,3)
if randno==1:
    comp='s'
elif randno==2:
    comp='w'
elif randno==3:
    comp='g'
    
you=input("Your Turn: Snake(s),Water(W),Gun(G) ?")
a= gamewin(comp,you)

print(f"Computer chose: {comp}")
print(f"You chose: {you}")

if a== None:
    print("The game is a tie!")
elif a:
    print('''             ***********************
    
                    You Win!
                    
             ***********************''')
else:
    print("You lose!")
