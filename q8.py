def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        while n > 1:
            result *= n
            n -= 1
        return result
numbers = list(map(int, input("Enter a list of numbers separated by space: ").split()))

for num in numbers:
    print(f"Factorial of {num}: {factorial(num)}")
