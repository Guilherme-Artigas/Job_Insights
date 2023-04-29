# print("-1000".isnumeric())
# print(str("10"))
# print(int("10"))

# string_numerica = "1"  # True
# string_numerica_negativo = "-1"  # False
# string_numerica_flutuante_negativo = "-1.5"  # False
# string_numerica_positivo = "2.3"  # False
# valor_ausente = ""  # False
# numero_inteiro_positivo = 50  # True
# numero_negativo = -50  # False
# numero_positivo_flutuante = 100.1  # False
# numero_negativo_flutuante = -200.5  # False
# letter = "a"  # False

# print(string_numerica.isnumeric())
# print(string_numerica_negativo.isnumeric())
# print(string_numerica_flutuante_negativo.isnumeric())
# print(string_numerica_positivo.isnumeric())
# print(valor_ausente.isnumeric())
# print(str(numero_inteiro_positivo).isnumeric())
# print(str(numero_negativo).isnumeric())
# print(str(numero_positivo_flutuante).isnumeric())
# print(str(numero_negativo_flutuante).isnumeric())
# print(letter.isnumeric())

# print(str("oi").isnumeric())

info_job = {"min_salary": 0, "max_salary": 2000, "Teste": 5000}

# min_salary = info_job.get("min_salary")
# max_salary = info_job.get("max_salary")
min_salary, *resto = info_job.values()
print(resto)