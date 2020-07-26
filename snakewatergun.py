import random
print("WELCOME TO SNAKE,WATER,GUN GAME:-)")
user_pt=0
comp_pt=0
for i in range(1,11):
    lst = ["Snake","Water","Gun"]
    comp = random.choice(lst)
    user = input("Enter your choice i.e\nSnake\nWater\nGun\n")
    if(comp==user):
        print("NO WIN,NO LOSE")
        user_pt+=0
        comp_pt+=0
    elif(comp=='Snake' and user == 'Water'):
        print("Computer gets 1 pt")
        user_pt+=0
        comp_pt+=1
    elif(comp=='Snake' and user == 'Gun'):
        print("User gets 1 pt")
        user_pt+=1
        comp_pt+=0
    elif(comp=='Water' and user == 'Gun'):
        print("Computer gets 1 pt")
        user_pt+=0
        comp_pt+=1
    elif(comp=='Water' and user=='Snake'):
        print("User gets 1 pt")
        user_pt+=1
        comp_pt+=0
    elif(comp=='Gun' and user=='Water'):
        print("User gets 1 pt")
        user_pt+=1
        comp_pt+=0
    elif(comp=='Gun' and user == 'Snake'):
        print("Computer gets 1 pt")
        user_pt+=0
        comp_pt+=1
if(user_pt>comp_pt):
    print("CONGRATULATIONS:-) USER WINS")
    print("Score of user",user_pt)
    print("Score of computer",comp_pt)
elif(comp_pt>user_pt):
    print("CONGRATULATIONS:-) COMPUTER WINS")
    print("Score of user", user_pt)
    print("Score of computer", comp_pt)
else:
    print("NOBODY WINS:-( GAME TIES")
    print("Score of user", user_pt)
    print("Score of computer", comp_pt)