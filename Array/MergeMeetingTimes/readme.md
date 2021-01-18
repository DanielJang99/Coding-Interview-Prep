## Merge Meeting Times

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
