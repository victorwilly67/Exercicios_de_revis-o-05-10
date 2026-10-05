contador = 1
soma = 0

for i in range(1, 11):
    num = float(input(f"Digite o {i}° número: "))
    soma += num
    contador += 1

print(f"A soma dos números é {soma}")