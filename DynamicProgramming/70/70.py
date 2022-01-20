memo = {
    0 : 0, 
    1: 1, 
    2: 2 
}
def climbStairs(n: int) -> int:
    if n in memo.keys():
        return memo[n]
    val = climbStairs(n-1)+climbStairs(n-2)
    memo[n] = val
    return val

