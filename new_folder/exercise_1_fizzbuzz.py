def fizzbuzz(n):         
    x = n%3
    y = n%5
    if x == 0 and y == 0:
        return "FizzBuzz"
    elif  x == 0:
        return "Fizz"
    elif y == 0:
        return "Buzz"
    else:
        return n

for i in range(1,21):
    print(fizzbuzz(i))

