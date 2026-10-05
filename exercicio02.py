nome = input("Digite o seu nome: ")
anoNascimento = float(input("Digite o seu ano de nascimento: "))
anoAtual = float(input("Digite o ano atual: "))

idade = anoAtual - anoNascimento

if idade >= 18:
    print("Você já pode fazer a sua carteira de motorista!!")

elif idade >= 16:
    print("Você já pode votar!!")

else:
    print("Idade inválida!")
