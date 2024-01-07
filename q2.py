def replace(input_str):
    vowels = "aeiouAEIOU"

    for vowel in vowels:
        input_str = input_str.replace(vowel, '*')

    return input_str

input_str = input("Enter the input String: ")
output_str = replace(input_str)

print(f"Original String: {input_str}")
print(f"String with Vowels Replaced: {output_str}")
