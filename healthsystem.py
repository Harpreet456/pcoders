#Health Management System
# i = int(input("Enter 1 for lock and 2 for retrieve:\n"))
# if(i==1):
#     n = int(input("Enter 1 for foodlocking and 2 for exercise:\n"))
    # if(n==1):
    #     # client = int(input("Enter which client data you want to lock for food:\n 1.Harry\n2.Rohan\n3.Hammad\n"))
        # if(client==1):
        #     f = open("foodlock.txt","w")
        #     f.write()
        #     f.close()


def getdate():
    import datetime
    return datetime.datetime.now()
def foodlock(c):
    f = open("food.txt","r+")
    f.write("chicken,roti")
    print("Foodlock of",c)
    print(f.readline())

# cname = input("Enter which one of the client data you want to lock harry,rohan,hammad\n")
print(getdate())
foodlock("Harry")