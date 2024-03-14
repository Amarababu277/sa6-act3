def find_maximum(numbers, compare):
    # Initialize maximum with the first element of the list
    max_num = numbers[0]
    
    # Iterate over the list
    for num in numbers:
        # Use the lambda function to compare num with the current maximum
        if compare(num, max_num) > 0:
            max_num = num
    
    return max_num

# Example usage
numbers = [5, 3, 9, 2, 7, 11]
# Define a lambda function to compare two numbers and return the greater one
greater_than = lambda x, y: x - y
# Find the maximum number in the list using the lambda function
maximum = find_maximum(numbers, greater_than)
print("Maximum number in the list:", maximum)
