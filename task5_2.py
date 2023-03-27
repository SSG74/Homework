n = int(input('Введите число: '))

def recursive_counter(number, even = 0, odd = 0):
    if number <= 0:
        return even, odd
    reduced_number, last_digit = divmod(number, 10)
    if last_digit % 2 == 0:
        return recursive_counter(reduced_number, even + 1, odd)
    else:
        return recursive_counter(reduced_number, even, odd + 1)
even, odd = recursive_counter(n)
print(f'в числе {n} есть {even} четных цифр и {odd} нечетных')