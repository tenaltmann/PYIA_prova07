import random

def lancar_dados ():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    soma_dos_dados = dado1 + dado2

    return f'Seus dados foram lançados e os valores foram {dado1} e {dado2}, totalizando {soma_dos_dados}'


inicio = print('SERÃO LANÇADOS DOIS DADOS .....')
print(lancar_dados())