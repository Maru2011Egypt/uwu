x = int(input("Please enter the first number "))
y = int(input("Please enter the second number "))
mode = (input("Please enter A for addition, S for subtraction, M for multiplication and D for division"))
if mode == "A":
    print (x+y)
elif mode == "S":
    print (x-y)
elif mode == "M":
    print (x*y)
elif mode == "D":
    print (x/y)
else:
    print("Please select a correct mode")
    
