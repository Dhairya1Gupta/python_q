def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
a=int(input("Enter the number: "))
if is_prime(a):
    print(f"{a} is a prime number.")
else:
    print(f"{a} is not a prime number.")
