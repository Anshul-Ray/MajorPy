n = int(input("Enter a number:"))

sed = 0
sod = 0

while n > 0:
    r = n % 10
    if r % 2 == 0:
        sed = sed + r
    else:
        sod = sod + r
    n = int(n / 10)

print("Sum of even digits:", sed)
print("Sum of odd digits:", sod)