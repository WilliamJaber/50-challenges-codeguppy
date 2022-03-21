"""Create a function that will convert from Fahrenheit to Celsius"""

def solution():
    temp_degree = int(input('\nInsert temperature:\n> '))
    result_in_C = (temp_degree - 32) * 5/9
    return (f'\n{temp_degree}°F equals to {result_in_C:.2f}°C')

print(solution())