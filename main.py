# *args = parameters that will all arguments into a tuple
#         so function can accept a varying amount of arguments
#################################################################

def add(*arg):
    adds = 0
    # print(type(arg))
    # print(type(adds))
    for i in arg:
        adds += i
    print("The result of addition: ", adds)

def sub(*arg):
    subs = 0
    for i in arg:
        subs -= i
    print("The result of subtraction: ", subs)

def mul(*arg):
    muls = arg[0]
    for i in arg:
        if muls == arg[0]:
            muls *= i + 1
        else:
            muls *= i
    print("The result of multiplication: ", muls)

def div(*arg):
    divs = arg[0]
    for i in arg:
        if divs == arg[0]:
            divs /= i + 1
        else:
            divs /= i
    print("The result of division: ", divs)

#################################################################

print("\n== Basic Math Operation with *args ==")
print("D. Display number")
print("1. Addition [+]")
print("2. Subtraction [-]")
print("3. Multiplication [*]")
print("4. Division [/]")
print("E. Exit")
choice = input("Choice: ")

while choice != 'E' and choice != 'e':
    if choice == 'D' or choice == 'd':
        print("\nDisplay number")
        print("1,2,3,4,5")

    elif choice == '1':
        print("\nAddition")
        add(1,2,3,4,5)

    elif choice == '2':
        print("\nSubtraction")
        sub(1,2,3,4,5)

    elif choice == '3':
        print("\nMultiplication")
        mul(1,2,3,4,5)

    elif choice == '4':
        print("\nDivision")
        div(1,2,3,4,5)

    else:
        print("\nInvalid input")

    print("\n== Basic Math Operation with *args ==")
    print("D. Display number")
    print("1. Addition [+]")
    print("2. Subtraction [-]")
    print("3. Multiplication [*]")
    print("4. Division [/]")
    print("E. Exit")
    choice = input("Choice: ")

if choice == 'e' or choice == 'E':
    print("\n== Exit Program ==")