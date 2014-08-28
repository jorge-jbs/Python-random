number = raw_input()

count = 0
a, b = 0, 1

while b <= int(number):
    a, b = b, a+b

    count = count + 1

print('The position of your number is the number ', count)