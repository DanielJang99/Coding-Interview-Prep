# Rotation Point

I opened up a dictionary to a page in the middle and started flipping through, looking for words I didn't know. I put each word I didn't know at increasing indices in a huge list I created in memory. When I reached the end of the dictionary, I started from the beginning and did the same thing until I reached the page I started at.

Now I have a list of words that are mostly alphabetical, except they start somewhere in the middle of the alphabet, reach the end, and then start from the beginning of the alphabet. In other words, this is an alphabetically ordered list that has been "rotated." For example:

```
words = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote',  # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
]
```

**Write a function for finding the index of the "rotation point,"** which is where I started working from the beginning of the dictionary. This list is huge (there are lots of words I don't know) so we want to be efficient here.

To keep things simple, you can assume all words are lowercase. We can get **O(lg n) time.**

# Find Duplicate - Optimize for Space

We have a list of integers, where:

1. The integers are in the range 1..n1..n
2. The list has a length of n+1n+1

It follows that our list has at least one integer which appears at least twice. But it may have several duplicates, and each duplicate may appear more than twice.

**Write a function which finds an integer that appears more than once in our list.** (If there are multiple duplicates, you only need to find one of them.) **Optimize for space!!!**
