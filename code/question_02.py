"""Print the odd numbers less than 100"""

def solution() -> lst:
    return [n for n in range(1, 101) if n%2 != 0]

print(solution())
