def func(n):
    if n % 5 == 0 and n % 3 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
    if n != 100:
        func(n+1)
    

func(1)



#check if n is a divisible of 3 or 5 or both and keep going