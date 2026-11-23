#توابع +و-و*و/و

def plus(a, b):
    return a + b

def negative(a, b):
    return a - b

def multiply(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "*************Cannot divide by zero!*************"
    return a / b

print("---------- calculator --------")
print("-----------operator:----------")
print("  + == plus")
print("  - == negative")
print("  * == multiply")
print("  / == division")
print("  end == exit")
print("\n-------------------------------")

#ورودی ها و شرط ها 

while True:
        
        o = input("\nEnter operator (+, -, *, /):")

        if o not in ("+", "-", "*", "/" , "end"):
            print("************Invalid operator!*************")
            continue    
        if o == "end":
            print("\n--------------good bye!-------------")
            break

        a = float(input(" Enter first number : "))
        b = float(input(" Enter second number: "))

        if o == "+":
            result = plus(a, b)
        elif o == "-":
            result = negative(a, b)
        elif o == "*":
            result = multiply(a, b)
        else:
            result = division(a, b)

        print("\nResult:", result)

#amir mhadi rezaei