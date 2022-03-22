"""Calculate the average of the numbers in an array of numbers"""

points = [100, 500, 300]

def solution(array: list) -> int:
    return sum(array) / len(array)

print(solution(points))
