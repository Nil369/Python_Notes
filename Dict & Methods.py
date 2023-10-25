# DIFFERENCE BETWEEN DICTIONARY & SETS:
"""a = {}
b = set()
print(a, type(a))
print(b, type(b))"""

# ===================================================================
dict1 = {"good": "Something Pleasant", "fetch": "To bring", "1": "The number 1"}
marks = {"Harshit": 69, "Harry": 96, "Akash": 99}

print(dict1["good"])
print(marks["Akash"])

# Dictionary Methods:
marks["Priyanka"] = 34
print(marks)

print(marks.get("Priyanka Chopra"))
# print(marks("Priyanka")) # This will not give error
# print(marks("Priyanka Chopra")) # But This will show ERROR as Priyanka Chopra is not defined in dict.
print(marks.get("Priyanka Chopra")) # This will save you from Error
print(marks.keys())
print(marks.values())
print(marks.items())

