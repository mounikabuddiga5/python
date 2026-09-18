n = int(input("Enter a number:"))
count = 0
num = n
while n > 0:
    last = n % 10
    count += 1
    n = n // 10
sum = 0
original = sum
while num > 0:
    digit = num % 10
    sum = digit ** count + sum
    num = num // 10
if (sum == original):
    print (" armstrong")
else:
    print("not armstrong")