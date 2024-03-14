def exponential_mapping(numbers, n):
    # Use map() function with a lambda function to raise each number to the power of n
    result = list(map(lambda x: x ** n, numbers))
    return result

# Example usage
numbers = [1, 2, 3, 4, 5]
n = 3
exponential_result = exponential_mapping(numbers, n)
print("Exponential mapping result:", exponential_result)
