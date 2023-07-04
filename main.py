from registros.gerar_registros import gerar_registros

# Definir o número desejado de registros
numero_registros = 10000

# Chamar a função para gerar os registros
registros = gerar_registros(numero_registros)

# Exibir os registros gerados
for registro in registros:
    print(registro)