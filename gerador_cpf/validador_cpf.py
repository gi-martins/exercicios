import re
import sys


FIRST_DIGIT_CALC = tuple(range(10, 1, -1))
SECOND_DIGIT_CALC = tuple(range(11, 1, -1))

cpf = input("Digite o CPF: ")
numbers_cpf = re.sub(r'[^0-9]', "", cpf)

if len(numbers_cpf) != 11 or numbers_cpf[0] * len(numbers_cpf) == numbers_cpf:
    print("CPF inválido")
    sys.exit()

total = 0
for index, number in enumerate(numbers_cpf[:-2]):
    total += int(number) * FIRST_DIGIT_CALC[index]

first_digit = (total * 10) % 11
if first_digit > 9:
    first_digit = 0

total = 0 
for index, number in enumerate(numbers_cpf[:-1]):
    total += int(number) * SECOND_DIGIT_CALC[index]

second_digit = (total * 10) % 11 
if second_digit > 9:
    second_digit = 0

if numbers_cpf[-2:] == f"{first_digit}{second_digit}":
    print("O CPF é válido")
else:
    print("CPF inválido")
