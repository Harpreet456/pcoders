# i=0
n = int(input("Enter the value of n:\n"))
a = int(input("Enter 1 or 0:\n"))

c= bool(a)
# print(c)
if(c== True):
    i=0
    while (i < n):
        j = 0
        while (j <= i):
            print("*", end="\t")
            j = j + 1
        print(end="\n")
        i = i + 1
else:
    i = n
    while (i >= 1):
        j = 0
        while (j < i):
            print("*", end="\t")
            j = j + 1
        print(end="\n")
        i = i - 1