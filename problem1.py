sum_of_digits = lambda num: sum(int(digit) for digit in str(num))

# Test the lambda function
number = 12345
result = sum_of_digits(number)
print(result) # Output will be 15