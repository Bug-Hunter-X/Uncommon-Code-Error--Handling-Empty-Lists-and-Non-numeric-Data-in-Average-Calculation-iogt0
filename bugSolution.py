def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        raise ValueError("The list contains no numeric values.")
    return sum(numeric_numbers) / len(numeric_numbers)

my_list = []
try:
    average = calculate_average(my_list)
    print(f"The average is: {average}")
except ValueError as e:
    print(f"Error: {e}")

my_list = [1, 2, 'a', 4]
try:
    average = calculate_average(my_list)
    print(f"The average is: {average}")
except ValueError as e:
    print(f"Error: {e}")
