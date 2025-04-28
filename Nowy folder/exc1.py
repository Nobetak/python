def fizz_buzz(input):
    if (input % 3 == 0 | input % 5 == 0):
        return "fizz buzz"
    if input % 3 == 0:
        return "fizz"
    if input % 5 == 0:
        return "buzz"
    else:
        return input


print(fizz_buzz(15))
