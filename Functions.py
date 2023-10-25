def greethello(name, ending):
    print("Hello,",name)
    print("Hello")
    print("Hello")
    print("Hello")
    print("Hello")
    print(ending)

def lettergenerator(name, date):
    st = f"Hi mam, \nThis is{name} and I will not come to school on {date}"
    print(st)

def average(a,b):
     return (a+b)/2

print("This will execute 1st")
greethello("Akash ", "Thank you") # Because greethello is defined & registered as a function
greethello("Shivam ", "Thank you")

lettergenerator(" Akash", "26/07/34")
print("done")

print(average(5, 25))