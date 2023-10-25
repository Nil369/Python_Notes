a = int(input("Enter a number: "))

match a:
     case 1:
      print("Case is 1")
     case 2:
      print("Case is 2")
     case 9:
      print("Case is 9")
     case 12:
      print("Case is 12")

     case _:
      print("No match found")

# Write a python program to print a table of number which lies between 1 and 10

table = int(input("Enter the number from 1 to 10: "))

match table:
        case 1:
            for i in range(1, 11):
                print(f"{table} X {i} = {table*i}")
        case 2:
            for i in range(1, 11):
                print(f"{table} X {i} = {table*i}")
        case 3:
            for i in range(1, 11):
                print(f"{table} X {i} = {table*i}")
        case 4:
            for i in range(1, 11):
                print(f"{table} X {i} = {table*i}")
        case 5:
            for i in range(1, 11):
                print(f"{table} X {i} = {table*i}")
        case 6:
            for i in range(1, 11):
                print(f"{table} X {i} = {table*i}")
        case 7:
            for i in range(1, 11):
                print(f"{table} X {i} = {table*i}")
        case 8:
            for i in range(1, 11):
                print(f"{table} X {i} = {table*i}")
        case 9:
            for i in range(1, 11):
                print(f"{table} X {i} = {table*i}")
        case 10:
            for i in range(1, 11):
                print(f"{table} X {i} = {table*i}")
        case _:
            print('Match not found. Please enter the number between 1 to 10 ')



