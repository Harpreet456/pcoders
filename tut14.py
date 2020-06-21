"""
list = [["harry",1],["larry",2],["marry",8],["carry",9]]
dict1 = dict(list)
print(dict1)
for i in list:
    print(i)
list1 = [5,6,"harry",7,4]
for i in list1:
    if(str(i).isdigit() and i>=6):
        print(i)
#next quiz
"""
while(True):
    i = int(input("Enter any no:\n" ))
    if(i<=100):
        continue
    print("Congratulations!!, u have entered a no greater than 100")
    break