import random
z = input("enter the operators")
oper_list = z.split(", ")
file = open("test_paper.txt", "w")
b = int(input("how many questions you want? : "))
def changer(n1, n2):
    if n1< n2:
        n3 = n2
        n2 = n1
        n1 = n3
    return n1, n2
for d in range(b):
    x = random.randint(100, 999)
    y = random.randint(100, 999)
    for m in oper_list:
        if m == "+" or m == "-" or m == "x" or m == "%":
            continue
        else:
            oper_list = ["x", "%", "+", "-"]
            print("you have not entered a valid operator so doing randomly")
    oper = random.choice(oper_list)
    if oper == "%" or oper == "-":
        x, y = changer(x, y)
    file.write("    ")
    file.write(str(x))
    file.write("\n")
    file.write(oper)
    file.write("   ")
    file.write(str(y))
    file.write("\n---------")
    file.write("\n---------\n\n")
    
    print("  ", x)
    print(oper, "", y)
    print("-----------")
    print("""-----------
    """)
