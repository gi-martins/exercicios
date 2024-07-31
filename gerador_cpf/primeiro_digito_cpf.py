cpf = input("Digite seu cpf: ")

numbers_cpf = cpf.replace(".", "").replace("-", "").replace(" ", "")[:-2] 

first_digit_calc = (10, 9, 8, 7, 6, 5, 4, 3, 2) # first_digit_calc = tuple(range(10, 1, -1)) dessa forma pode colocar qualquer valor na lista, ...
#                                               ... sem precisar digitar todos os números.
numbers_sum = 0

for index, number in enumerate(numbers_cpf):
    numbers_sum += int(number) * first_digit_calc[index]

first_digit = (numbers_sum * 10) % 11

if first_digit > 9:
    first_digit = 0 

print("O primeiro dígito é:", first_digit)
