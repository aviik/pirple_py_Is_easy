def isPrima(c):
    """Function to check if the number is prime"""
    prime = True
    if c<2:
        prime = False
    else:
        for k in range(2, int(c/2)+1):
            if c % k == 0:
                prime = False
    return prime


def fizzy():
    for n in range(1, 101):
        if isPrima(n):
            print("Prime")
        elif n%3 == 0 and n%5 == 0:
            print("FizzBuzz")
        elif n%3 == 0:
            print("Fizz")
        elif n%5 == 0:
            print("Buzz")
        else:
            print(n)

fizzy()
