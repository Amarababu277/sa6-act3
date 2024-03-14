def intersection(list1, list2):
    # Use filter() function with a lambda function to keep only the elements present in both lists
    common_elements = list(filter(lambda x: x in list2, list1))
    return common_elements

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
intersection_result = intersection(list1, list2)
print("Intersection of the two lists:", intersection_result)
