f=open("poem.txt","r")
print(f.read())

def count_words(f):
    try:
        with open(f, 'r') as file:
            content = file.read()
            words = content.split()

            to_count = sum(1 for word in words if word.lower() == 'to')
            the_count = sum(1 for word in words if word.lower() == 'the')

            print("'to' count:", to_count)
            print("'the' count:", the_count)

    except FileNotFoundError:
        print("File not found.")

count_words('poem.txt')

