inp_str=input("enter number for find table:")

try:
    x=int(inp_str)
    for i in range(1,11):
     print(x*i)
except ValueError as e:
    print("Enter valid number")

      


