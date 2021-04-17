#BASIC CALC
'''
num1 = float(input("Enter your first num:"))
num2 = float(input("Enter your second num:"))
print("===============================")
print("summation result:",num1+num2)
print("subtraction result:",num1-num2)
print("multip. result: ",num1*num2)
print("division result:",num1/num2)
print("===============================")'''
#######################################################
#BASIC CALC WITH IF-ELSE

print(""" 
[1]-sum
[2]-sub 
[3]-multi
[4]-devi
[0]-EXiT      """)

enter = input("Choose:")
if enter == "1":
        x = input("First num:")
        x = float(x)
        y = input("Second num:")
        y = float(y)
        print("Result:",x+y)

elif enter == "2":
        x = input("First num:")
        x = float(x)
        y = input("Second num:")
        y = float(y)
        print("Result:",x-y)

elif enter == "3":
        x = input("First num:")
        x = float(x)
        y = input("Second num:")
        y = float(y)
        print("Result:",x*y)

elif enter == "4":
        x = input("First num:")
        x = float(x)
        y = input("Second num:")
        y = float(y)
        print("Result:",x/y)

elif enter == "0":
        print("exiting")
        quit()

else:
        print("Syntax ERROR!")
