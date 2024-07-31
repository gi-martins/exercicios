cpf = input("Digite seu cpf: ")

numbers_cpf = cpf.replace(".", "").replace("-", "").replace(" ", "")[:-1] 

second_digit_calc = (11, 10, 9, 8, 7, 6, 5, 4, 3, 2) # second_digit_calc = tuple(range(11, 1, -1)) dessa forma pode colocar qualquer valor na lista, ...
#                                                   ... sem precisar digitar todos os números.
numbers_sum = 0

for index, number in enumerate(numbers_cpf):
    numbers_sum += int(number) * second_digit_calc[index]

second_digit = (numbers_sum * 10) % 11

if second_digit > 9:
    second_digit = 0 

print("O segundo dígito é:", second_digit)
