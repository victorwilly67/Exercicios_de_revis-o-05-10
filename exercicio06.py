nome_mais_velho = ""
idade_mais_velho = 0    

for i in range(1, 6):
    nome = input(f"Digite o nome da {i}° pessoa: ")
    idade = int(input(f"Digite a idade de {nome}: "))

    if idade > idade_mais_velho:
        idade_mais_velho = idade
        nome_mais_velho = nome

print(f"A pessoa mais velha é {nome_mais_velho} com {idade_mais_velho} anos.")