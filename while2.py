while True:
    val = input ("Do you want to calculate #")
    if val =="Q" or val=="q":
        break
    a = input("Enter num1 #")
    b = input("Enter num2 #")
    op = input("Type#")

    if op == '+':
        result = int(a) + int(b)

    elif op == '-':
        result = int(a) - int(b)
    elif op == '*':
        result = int(a) * int(b)
    else:
        print("Not defined")

    print(result)
