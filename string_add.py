def add(numbers, delimiter=','):
    separated_numbers = numbers.split(delimiter)
    numbers_sum = 0
    for number in separated_numbers:
        try:
            number_value = int(number)
            if number_value >= 0:
                numbers_sum += number_value
        except ValueError:
            return -1
    return numbers_sum
