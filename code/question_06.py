"""Calculate 10"""

def solution(n: int) -> None:
    if n == 0:
        return 1
    return n * solution(n-1)

print(solution(10))
