from typing import List


def construct2DArray(original: List[int], m: int, n: int) -> List[List[int]]:
    ret = []
    if (m*n == len(original)):
        for i in range(m):
            ret.append(original[i*n:i*n+n])
    return ret

