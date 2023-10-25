""" a = int(input("Enter your number: "))
print(a+3)
 But if user Enters a string or alphanumeric value it will show Error
& the program will halt.But we don't want that.We want our program to run continuously
Therefore, we use Try & Except METHOD.This will print error but our program
 will run till it is finished """

try:
    num = int(input("Enter your number: "))
    print(num)
except Exception as e:
    print("Opps!!Some Error Occured...", e) 



