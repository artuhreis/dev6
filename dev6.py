anoAtual = 2022
# Função de Calculo da Idade.
def calculoIdade(anoAtual,anoNacimento):
    idade = anoAtual - anoNacimento
    return idade

print("Bem Vindo ao Sistema de Calculo de Idade :) \n")

# Coletando o Nome do Usuário.
print("Digite seu Nome Completo: ")
nome = str (input())

# Solicitar e validar o Ano de Nascimento.
anoNascimento = False
while not anoNascimento:
    try:
        print("Digite o ano que você nasceu: ")
        anoNascimento = int(input())
    
        if anoNascimento < 1922 or anoNascimento > 2021 and anoNascimento :
            print("Ano de Nascimento Invalido! Por favor Digite um ano entre 1922 a 2022!")
            anoNascimento = False
        else:
            anoNascimento = anoNascimento

    except ValueError:
        print("Ano de Nascimento Invalido! Por favor Digite um ano entre 1922 a 2022!")

# Teste e devolução para o usuario. 
idade = calculoIdade(anoAtual,anoNascimento)
print(nome, " você tem ", idade , "anos")


    