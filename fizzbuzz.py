'''
Write a short program that prints each number from 1 to 100 on a new line. 

For each multiple of 3, print "Fizz" instead of the number. 

For each multiple of 5, print "Buzz" instead of the number. 

For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.
http://www.compciv.org/guides/python/fundamentals/fizzbuzz-challenge/
'''
def fizzbuzz(num1, num2):
    for i in range(num1, num2):
        if i % 3 is 0 and i % 5 is 0:
            print("FizzBuzz")
        elif i % 3 is 0:
            print("Fizz")
        elif i % 5 is 0:
            print("Buzz")
        else:
            print(i)
fizzbuzz(1, 101)
