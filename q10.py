n = list(map(int, input("Enter a list of numbers separated by space: ").split()))
s=0
for i in n:
    if i%2==0:
        x=i*10
        s=s+x
    else:
        i=i+1
print(s)
