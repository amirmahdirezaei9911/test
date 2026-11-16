number = int(input("Please enter the number of repetitions.: "))
number2 = 0
while number2 < number:

    score = float(input("please enter the python score : "))

    if score == 20:
        print("good score")
    elif score >= 17:
        print("Excellent!")
    elif score >= 12:
        print("Passed!")
    else:
        print("Failed!")

    print("--------------------------------------")

    width = int(input("Enter rectangle width: "))
    height = int(input("Enter rectangle height: "))

    for i in range(height):
        for j in range(width):
            print("*", end=" ")
        print()
    
    print("--------------------------------------")

    number2 += 1

print("good bye")    