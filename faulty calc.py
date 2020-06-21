#input operator,no,all ans should be correct except 45*3=555,56+9=77,56/6=4
var1 = int(input("Enter first no:\n"))
var2 = int(input('Enter second no:\n'))
op = input("Enter operator +,-,*,/,%\n")
if(var1==45 and var2==3 and op=='*'):
        print("555")
elif(var1==56 and var2==9 and op=='+'):
        print("77")
elif(var1==56 and var2==6 and op=='/'):
        print("4")
else:
        if(op=='+'):
                sum=var1+var2
                print(sum)
        elif(op=='-'):
                sub=var1-var2
                print(sub)
        elif(op=='*'):
                mul=var1*var2
                print(mul)
        elif(op=='/'):
                div=var1/var2
                print(div)
        elif(op=='%'):
                mod=var1%var2
                print(mod)
        else:
                print("Invalid operator")