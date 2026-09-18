sum = 0
num = int(input("Enter a number:"))
org = num
for i in range(1,num):
    if num % i == 0 :
        sum += i
if org == sum :
    print(num,"is perfect number")
else:
    print(num,"is not a perfect number")
