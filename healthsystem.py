print(":) Welcome to our Health Management System :)")
i = int(input("Enter 1 for log and 2 for retrieve:\n"))
if(i==1):
    n = int(input("Enter 1 for foodlocking and 2 for exercise:\n"))
    if(n==1):
         client = int(input("Enter which client data you want to log for food:\n1.Harry\n2.Rohan\n3.Hammad\n"))
         if(client==1):
            def getdate():
                import datetime
                return datetime.datetime.now()


            def foodlock(c):
                f = open("food.txt", "a")
                print("Write your data:",c)
                f.write(input())
                print("Successfully written")
                # print(f.readline())
                f.close()

            print(getdate())
            foodlock("Harry")
         if(client == 2):
            def getdate():
                import datetime
                return datetime.datetime.now()


            def foodlock(c):
                f = open("food1.txt", "a")
                print("Write your data:", c)
                f.write(input())
                print("Successfully written")
                # print(f.readline())
                f.close()


            print(getdate())
            foodlock("Rohan")
         if(client==3):
            def getdate():
                import datetime
                return datetime.datetime.now()


            def foodlock(c):
                f = open("food2.txt", "a")
                print("Write your data:", c)
                f.write(input())
                print("Successfully written")
                # print(f.readline())
                f.close()
            print(getdate())
            foodlock("Hammad")
    else:
        client = int(input("Enter which client data you want to log for exercise:\n1.Harry\n2.Rohan\n3.Hammad\n"))
        if (client == 1):
            def getdate():
                import datetime
                return datetime.datetime.now()


            def exercise(c):
                f = open("exe.txt", "a")
                print("Write your data:", c)
                f.write(input())
                print("Successfully written")
                # print(f.readline())
                f.close()


            print(getdate())
            exercise("Harry")
        if (client == 2):
            def getdate():
                import datetime
                return datetime.datetime.now()


            def exercise(c):
                f = open("exe1.txt", "a")
                print("Write your data:", c)
                f.write(input())
                print("Successfully written")
                # print(f.readline())
                f.close()


            print(getdate())
            exercise("Rohan")
        if (client == 3):
            def getdate():
                import datetime
                return datetime.datetime.now()


            def exercise(c):
                f = open("exe2.txt", "a")
                print("Write your data:", c)
                f.write(input())
                print("Successfully written")
                # print(f.readline())
                f.close()


            print(getdate())
            exercise("Hammad")

else:
    client = int(input("What data you want to retrieve:\n1.Food\n2.Exercise\n"))
    if(client==1):
        n = int(input("Which client data you want to retrieve for food\n1.Harry\n2.Rohan\n3.Hammad\n"
                      ))
        if(n==1):
            def getdate():
                import datetime
                return datetime.datetime.now()
            def retr(c):
                f = open("food.txt","r")
                content = f.read()
                print("Food retrieval of"+c+"\n")
                print(content)
                f.close()

            print(getdate())
            retr("Harry")
        elif (n == 2):
            def getdate():
                import datetime
                return datetime.datetime.now()


            def retr(c):
                f = open("food1.txt", "r")
                content = f.read()
                print("Food retrieval of"+c+"\n")
                print(content)
                f.close()


            print(getdate())
            retr("Rohan")
        else:
            def getdate():
                import datetime
                return datetime.datetime.now()


            def retr(c):
                f = open("food2.txt", "r")
                content = f.read()
                print("Food retrieal of "+c+"\n")
                print(content)
                f.close()


            print(getdate())
            retr("Hammad")
    else:
        n = int(input("Which client data you want to retrieve for exercise\n1.Harry\n2.Rohan\n3.Hammad\n"
                      ))
        if (n == 1):
            def getdate():
                import datetime
                return datetime.datetime.now()


            def retr(c):
                f = open("exe.txt", "r")
                content = f.read()
                print("Exercise retrieval of" + c + "\n")
                print(content)
                f.close()


            print(getdate())
            retr("Harry")
        elif (n == 2):
            def getdate():
                import datetime
                return datetime.datetime.now()


            def retr(c):
                f = open("exe1.txt", "r")
                content = f.read()
                print("Exercise retrieval of" + c + "\n")
                print(content)
                f.close()


            print(getdate())
            retr("Rohan")
        else:
            def getdate():
                import datetime
                return datetime.datetime.now()


            def retr(c):
                f = open("exe2.txt", "r")
                content = f.read()
                print("Exercise retrieal of " + c + "\n")
                print(content)
                f.close()


            print(getdate())
            retr("Hammad")