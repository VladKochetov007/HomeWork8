def natural_gen(max_n: int | None = None):
    # sum of digits greater than previous number
    n = 0
    number = 1
    if max_n is None:
        max_n = float('inf')
    while n <= max_n:
        n += 1
        yield number
        term = number + 1
        while not is_greater_by_number(term, number):
            term += 1
        number = term

def is_greater_by_digits(number_digits: int, number: int) -> bool:
    return sum(int(digit) for digit in str(number_digits)) > sum(int(digit) for digit in str(number))

def is_greater_by_number(number_digits: int, number: int) -> bool:
    return sum(int(digit) for digit in str(number_digits)) > number

for i in natural_gen(100):
    print(i)