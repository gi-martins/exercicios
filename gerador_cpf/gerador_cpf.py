import random


FIRST_DIGIT_CALC = tuple(range(10, 1, -1))
SECOND_DIGIT_CALC = tuple(range(11, 1, -1))

init_cpf = ""

for number in range(9):
    init_cpf += str(random.randint(0, 9))

total = 0
for index, number in enumerate(init_cpf):
    total += int(number) * FIRST_DIGIT_CALC[index]

first_digit = (total * 10) % 11
if first_digit > 9:
    first_digit = 0

cpf = f"{init_cpf}{first_digit}"

total = 0
for index, number in enumerate(cpf):
    total += int(number) * SECOND_DIGIT_CALC[index]

second_digit = (total * 10) % 11
if second_digit > 9:
    second_digit = 0

print(("{}{}{}.{}{}{}.{}{}{}-{}{}").format(*f"{cpf}{second_digit}"))
