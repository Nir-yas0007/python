# to check Number is even or odd

a= int(input("Enter the number:"))
if (a%2)==0:
    print(f"{a} is an even number")
else:
print(f"{a} is an odd number")


## sum of list[1,50]

total = 0
for number in range(1, 51):
    total += number

print("Sum of numbers from 1 to 50 is:", total)

# while loop

a=1
total = 0
while  a<=50:
    total += a
    a += 1

print("Sum of numbers from 1 to 50 is:",total )


