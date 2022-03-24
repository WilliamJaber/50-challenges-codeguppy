"""Calculate the sum of even numbers greater than 10 and less than 30"""

def solution() -> int:
    return sum([n for n in range(10, 30) if n%2 == 0])

print(solution())
