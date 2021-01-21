# Inflight Entertainment

Users on longer flights like to start a second movie right when their first one ends, but they complain that the plane usually lands before they can see the ending. So you're building a feature for choosing two movies whose total runtimes will equal the exact flight length.

Write a function that takes an integer flight_length (in minutes) and a list of integers movie_lengths (in minutes) and returns a boolean indicating whether there are two numbers in movie_lengths whose sum equals flight_length.

When building your function:

-   Assume your users will watch exactly two movies
-   Don't make your users watch the same movie twice
-   Optimize for runtime over memory

# Permutation Palindrome

Write a function that checks whether any permutation of an input string is a palindrome, a string that's the same when read forward and backward (e.g: civic, mom, anna, kayak, racecar)

You can assume the input string only contains lowercase letters.

Examples:

-   "civic" should return True
-   "ivicc" should return True
-   "civil" should return False
-   "livci" should return False

Remember that the challenge is to find wheter any _permutation_ of the string is a palindrome, hence "ivicc" should also return True.

# Word Cloud Data

The task is to build a word cloud, an infographic where the size of a word corresponds to how often it appears in the body of text.
Write code that takes a long string and builds its word cloud data in a dictionary ↴ , where the keys are words and the values are the number of times the words occurred.

Think about **capitalized words**. For example, look at these sentences:

```
'After beating the eggs, Dana read the next step:'
'Add milk and eggs, then add flour and sugar.'
```

What do we want to do with "After", "Dana", and "add"? In this example, your final dictionary should include one "Add" or "add" with a value of 2. Make reasonable (not necessarily perfect) decisions about cases like "After" and "Dana".

Assume the input will only contain words and standard punctuation.
