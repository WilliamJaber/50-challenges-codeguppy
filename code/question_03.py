"""Print the multiplication table with 7"""

def solution(num):
    for i in range(11):
        multiplier = i
        print(f'{num} x {multiplier} = {num * multiplier}')

solution(7)
