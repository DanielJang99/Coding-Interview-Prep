# Recursive String Permutation

Write a recursive function for generating all permutations of an input string. Return them as a set.

Don't worry about time or space complexity—if we wanted efficiency we'd write an iterative version.

To start, assume every character in the input string is unique.

Your function can have loops—it just needs to also be recursive.

# Nth Fibonacci

Write a function fib() that takes an integer nn and returns the nth Fibonacci number.

Let's say our Fibonacci series is 0-indexed and starts with 0. So:

```
fib(0)  # => 0
fib(1)  # => 1
fib(2)  # => 1
fib(3)  # => 2
fib(4)  # => 3
...
```

# Coins

Write a function that, given:

1. an amount of money
2. a list of coin denominations
   computes the number of ways to make the amount of money with coins of the available denominations.

Example: for amount=4 (4¢) and denominations=[1,2,3] (1¢, 2¢ and 3¢), your program would output 4—the number of ways to make 4¢ with those denominations:

1. 1¢, 1¢, 1¢, 1¢
2. 1¢, 1¢, 2¢
3. 1¢, 3¢
4. 2¢, 2¢
