# check the age is =18
age = int(input("Enter Your Age! :"))
if age <= 0:
    print("Please Enter Valid age ")
if age < 18:
    print("You can not Vote")
elif age == 18:
    print("You Can Vote")
elif age > 18:
    print("You can Vote")
elif age <= 120:
    print("You can Vote")
else:
    print("Please Enter valid age 1 to 120")