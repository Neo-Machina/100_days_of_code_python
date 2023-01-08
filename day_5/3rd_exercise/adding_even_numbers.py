# You are going to write a program that calculates the sum of all the even numbers from 1 to 100.
# Thus, the first even number would be 2 and the last one is 100

sum = 0
for number in range(1, 101):
    if number % 2 == 0:
        sum += number
print(sum)