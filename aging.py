birth_year = int(input("Enter your birth year: "))
current_year = 2026
age = current_year - birth_year
print(f"You are {age} years old.")
if age < 18:
    print("You are a child.")
elif age < 40:
    print("You are a young adult.")
elif age < 60:
    print("You are middle-aged.")
else:
    print("You are a senior.")
