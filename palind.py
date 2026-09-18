n = int(input("Enter a number:"))
num = n
rev = 0
while n > 0:
    last = n % 10
    rev = rev * 10 + last
    n = n // 10
if(num == rev):
    print(num,"is a palindrome!")
else:
    print(num,"is not a palindrome!")