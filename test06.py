# 재귀함수 ( recursive function )
import sys
sys.setrecursionlimit(10**8)
# 1부터 X까지의 합
def recur(x):
    if x == 1:
        return 1
    return x + recur(x - 1)

# 1부터 X까지의 곱 ( 팩토리얼 )
def factor(x):
    if x == 1:
        return 1
    return x * factor(x - 1)

