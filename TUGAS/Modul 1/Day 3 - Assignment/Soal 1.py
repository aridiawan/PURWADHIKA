'''
## Question-1

This exercise continues our use of the modulo operator to determine if numbers are divisible by 3, 5, or both 3 and 5. 
Divisible by n, means that it can be divided by a number n with no remainder. For example, 10 is divisible by 5, 
but 11 is not divisible by 5.

Write a simple program with a single integer variable named `upTo`. For the numbers 1 up to and including `upTo`, 
the function prints one of four things:

- Prints `Fizz` if the number is only divisible by 3.
- Prints `FizzBuzz` if the number is divisible by 3 and 5.
- Prints `Buzz` if the number is only divisible by 5.
- Prints the number if the number is neither divisible by 3 nor 5.

Instead of printing each string or number on a separate line, print them without newlines. For
example, your solution is correct if calling `upTo = 35` produces the following output:

1. 1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz Fizz 22
23 Fizz Buzz 26 Fizz 28 29 FizzBuzz 31 32 Fizz 34 Buzz
'''
if __name__ == '__main__':
    # ANSWER

    upTo = int(input('Input your max number:'))

    result = ''

    for i in range(1,upTo+1):
        if i % 3 == 0 and i % 5 == 0:
            result += 'FizzBuzz '
        elif i % 3 == 0:
            result += 'Fizz '
        elif i % 5 == 0:
            result += 'Buzz '
        else: 
            result += f'{i} '

    print(result)