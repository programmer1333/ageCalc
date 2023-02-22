from datetime import datetime
bYear = int(input("Enter your birth year: "))
cYear = datetime.now().year
print(cYear - bYear)
