# Day 1 Problem 1: FizzBuzz
# Write a function that prints numbers 1 to 100, but:
#
# For multiples of 3, print "Fizz" instead
# For multiples of 5, print "Buzz" instead
# For multiples of both 3 and 5, print "FizzBuzz" instead


def test_fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


print(test_fizzbuzz())