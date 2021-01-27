# Apple Stocks

Suppose you started trading Apple stocks all day.

First, I wanna know how much money I could have made yesterday if I'd been trading Apple stocks all day.
So I grabbed Apple's stock prices from yesterday and put them in a list called stock_prices, where:

-   The indices are the time (in minutes) past trade opening time, which was 9:30am local time.
-   The values are the price (in US dollars) of one share of Apple stock at that time.

So if the stock cost \$500 at 10:30am, that means stock_prices[60] = 500.

Write an efficient function that takes stock_prices and returns the **best profit I could have made from one purchase and one sale of one share of Apple stock yesterday.**

For example:

```
stock_prices = [10, 7, 5, 8, 11, 9]

get_max_profit(stock_prices)
# this should return 11-5 = 6
```

No "shorting"—you need to buy before you can sell. Also, you can't buy and sell in the same time step—at least 1 minute has to pass.

# Highest Product of 3

Given a list of integers, find the highest product you can get from three of the integers.

The input list_of_ints should always have at least three integers.

# Highest Product of Other Numbers

You have a list of integers, and for each index you want to find the product of every integer except the integer at that index.

Write a function get_products_of_all_ints_except_at_index() that takes a list of integers and returns a list of the products.

For example, given:

```
[1, 7, 3, 4]
# your function will return
[84, 12, 28, 21]
# by calculating
[7 * 3 * 4,  1 * 3 * 4,  1 * 7 * 4,  1 * 7 * 3]
```

Here's the catch: **You can't use division in your solution!**

# In-Place Shuffle

Write a function for doing an in-place ↴ shuffle of a list.

The shuffle must be "uniform," meaning each item in the original list must have the same probability of ending up in each spot in the final list.

Assume that you have a function get_random(floor, ceiling) for getting a random integer that is >= floor and <= ceiling.
