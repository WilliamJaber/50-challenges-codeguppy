"""Print numbers from 1 to 10"""

def solution1() -> lst:
    return [n for n in range(1, 11)]

print(solution())



def solution2() -> None:
    n = 0
    while n < 10:
        n += 1
        print(n)

solution2()
