# Merge Meeting Times

Write a function merge_ranges() that takes a list of multiple meeting time ranges and returns a list of condensed ranges. Each meeting is stored as a tuple of integers (start_time, end_time).

For example, given:

```
  [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
```

the function would return:

```
  [(0, 1), (3, 8), (9, 12)]
```

**Do not assume the meetings are in order.** The meeting times are coming from multiple teams.

**Write a solution that's efficient even when we can't put a nice upper bound on the numbers representing our time ranges.** The spirit of the challenge is to merge meetings where start_time and end_time don't have an upper bound.

# Reverse String in Place

Write a function that takes a list of characters and reverses the letters in place.

# Merge Sorted Arrays

We are given two lists of integers sorted numerically already. Write a function to merge the lists of integers into one sorted list.

For example:

```
my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

# Prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
print(merge_lists(my_list, alices_list))
```

# Reverse Words

Write a function reverse_words() that takes a message as a list of characters and reverses the order of the words **in place**.

For example:

```
message = [ 'c', 'a', 'k', 'e', ' ',
            'p', 'o', 'u', 'n', 'd', ' ',
            's', 't', 'e', 'a', 'l' ]

reverse_words(message)

# Prints: 'steal pound cake'
print(''.join(message))
```

When writing your function, assume the message contains only letters and spaces, and all words are separated by one space.
