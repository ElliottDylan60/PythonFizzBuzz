def FizzBuzz():
    Input = float(input("Number:"))

    if Input % 3 == 0 and Input % 5 == 0:
        print("FizzBuzz")
    elif Input % 3 == 0:
        print("Fizz")
    elif Input % 5 == 0:
        print("Buzz")
    else:
        print("not divisible by 3 or 5")
    FizzBuzz()
FizzBuzz()