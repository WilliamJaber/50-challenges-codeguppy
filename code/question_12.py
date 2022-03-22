"""Create a function that receives an array of numbers as argument and returns
    an array containing only the positive numbers"""

num = [86, -57, 45, -30, 23, -12]

def solution(num: list) -> list:
    return [pn for pn in num if pn > 0]

print(solution(num))
