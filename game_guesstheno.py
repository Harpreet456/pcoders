#n=18 hide that no. take i/p from user and tell them whether his no is gtr or lesser. If hits the crct no then
#print u won. take i/p no of guesses and also print how many no of guesses are left
#If all guesses are over then print game over.
#If it wons print no of guesses he took to win.
n=18
guess = int(input("Enter no of gueeses:\n"))

i=0
flag=0
while(i<guess):
    no = int(input("Enter your no:\n"))
    if(no<18):
            print("No which u have entered is lesser than the hidden no")
            i=i+1
            diff=guess-i
            print("No of guesses left:",diff)
    elif(no>18):
            print("No which u have entered is greater than hidden no")
            i=i+1
            diff=guess-i
            print("No of guesses left:",diff)
    elif(no<=10):
            print("Enter gtr no")
            i=i+1
            diff=guess-i
            print("No of guesses left:",diff)
    elif(no>10 and no<=15):
            print("You are closer,Enter gtr no")
            i=i+1
            diff=guess-i
            print("No of guesses left:",diff)
    elif(no>15 and no<18):
            print("You are very close,Enter some gtr no")
            i=i+1
            diff=guess-i
            print("No of guesses left:",diff)
    elif(no==18):
            print("Congratulations!!You WON the game")
            i=i+1
            diff=guess-i
            print("No of guesses u took to won",diff)
            break
print("Sorry,better luck next time")
#flag = flag+1
#if(flag==1):
 #   choice= int(input("Do u want to play again, for play again press 1 otherwise 0"))
#if(choice==1):
  #  continue
#else:
 #   break
