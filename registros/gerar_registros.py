import random

# Função para gerar um número de CEP aleatório
def gerar_cep():
    cep = ''.join(random.choices('0123456789', k=8))
    cep_formatado = f"{cep[:5]}-{cep[5:]}"
    return cep_formatado

# Função para gerar um número de peso aleatório
def gerar_peso():
    peso = random.uniform(0.1, 10.0)
    peso_formatado = "{:.4f}".format(peso)
    return peso_formatado

# Função para gerar um prazo aleatório
def gerar_prazo():
    prazo = random.randint(1, 10)
    return str(prazo)

# Função para gerar um valor de frete aleatório
def gerar_frete():
    frete = random.randint(10, 50)
    return str(frete)

# Função para gerar uma modalidade aleatória
def gerar_modalidade():
    modalidades = ['PAC', 'SEDEX', 'Transportadora']
    modalidade = random.choice(modalidades)
    return modalidade

# Função para gerar um valor de cubagem aleatório
def gerar_cubagem():
    cubagem = random.uniform(0.1, 10.0)
    cubagem_formatada = "{:.3f}".format(cubagem)
    return cubagem_formatada

# Função para gerar registros
def gerar_registros(numero_registros):
    registros = []
    for _ in range(numero_registros):
        cep_inicial = gerar_cep()
        cep_final = gerar_cep()
        peso_inicial = gerar_peso()
        peso_final = gerar_peso()
        prazo = gerar_prazo()
        frete = gerar_frete()
        modalidade = gerar_modalidade()
        cubagem_inicial = gerar_cubagem()
        cubagem_final = gerar_cubagem()
        registro = f"{cep_inicial}\t{cep_final}\t{peso_inicial}\t{peso_final}\t{prazo}\t{frete}\t{modalidade}\t{cubagem_inicial}\t{cubagem_final}"
        registros.append(registro)
    
    return registros

# Teste da função gerar_registros
if __name__ == '__main__':
    numero_registros = 10000
    registros = gerar_registros(numero_registros)
    
    for registro in registros:
        print(registro)
