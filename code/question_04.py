"""Print all the multiplication tables with numbers from 1 to 10"""

def solution() -> None:
    for n in range(11):
        multiplicand = n
        for i in range(11):
            multiplier = i
            print(f'{multiplicand} x {multiplier} = {multiplicand * multiplier}')
        print()

solution()
