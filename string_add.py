def add(numbers):
    separated_numbers = numbers.split(',')
    numbers_sum = 0
    for number in separated_numbers:
        if number.isdigit():
            numbers_sum += int(number)
        else:
            return -1
    return numbers_sum
