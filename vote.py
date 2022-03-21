age = int(input("Enter Your Age! :"))

if not (age < 0 or age > 120):
    if age >= 18:
        print("Vote")
    elif age < 18:
        print("Not Vote")
else:
    print("1 or 120 ke beechme honi chahiye")
