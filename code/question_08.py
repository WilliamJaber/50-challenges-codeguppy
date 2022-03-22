"""Create a function that will convert from Celsius to Fahrenheit"""

def solution() -> Any:
    temp_degree = int(input('\nInsert temperature:\n> '))
    result_in_F = (temp_degree * 9/5) + 32
    return (f'\n{temp_degree}°C equals to {result_in_F:.2f}°F')

print(solution())
