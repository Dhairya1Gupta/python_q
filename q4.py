def find(input_tuple):
    if not input_tuple:
        return None, None  # Return None for both largest and smallest if the tuple is empty

    largest = smallest = input_tuple[0]

    for element in input_tuple:
        if element > largest:
            largest = element
        elif element < smallest:
            smallest = element

    return largest, smallest

# Input from the user
user_input = input("Enter elements of the tuple separated by commas: ")
user_tuple = tuple(map(int, user_input.split(',')))

# Call the function with user input
largest, smallest = find(user_tuple)

print("Largest element:", largest)
print("Smallest element:", smallest)
