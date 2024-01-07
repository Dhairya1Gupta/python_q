f=open("example.txt","r")
print(f.read())
f.close()
def count_chars(f):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

    try:
        with open(f, 'r') as file:
            content = file.read()

            vowel_count = sum(1 for char in content if char in vowels)
            consonant_count = sum(1 for char in content if char in consonants)
            uppercase_count = sum(1 for char in content if char.isupper())
            lowercase_count = sum(1 for char in content if char.islower())

            print("Vowels:", vowel_count)
            print("Consonants:", consonant_count)
            print("Uppercase letters:", uppercase_count)
            print("Lowercase letters:", lowercase_count)

    except FileNotFoundError:
        print("File not found.")
count_chars('example.txt')
