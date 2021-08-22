def fizz_buzz(max):
    numbers = []

    for i in range(0, max):
        if(i % 4 == 0 or i % 6 == 0) and not (i % 4 == 0 and i % 6 == 0):
            numbers.append(i)

            i += 1
            print(numbers)
print(fizz_buzz(20))