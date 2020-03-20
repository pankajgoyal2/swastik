def add(x, y):
   return x + y

def subtract(x, y):
   return x - y

def multiply(x, y):
   return x * y

def divide(x, y):
   return x / y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = int(input("Enter choice(1/2/3/4):"))

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

#print("s.show")
#print("h.hide")
#print("invalid.show")

#choise2 = input("formula or not: ")

if choice == 1:
   # if choise2 == "h":
    print(add(num1, num2))
    
   # print(num1,"+",num2,"=", add(num1,num2))

elif choice == 2:
    #if choise2 == "h":
    print(subtract(num1, num2))
    
    #print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == 3:
    #if choise2 == "h":
    print(multiply(num1, num2))
    
    #print(num1,"x",num2,"=", multiply(num1,num2))

elif choice == 4:
    #if choise2 == "h":
    print(divide(num1, num2))
    #print(num1,"%",num2,"=", divide(num1,num2))
else:
   print("Invalid input")
