media = 0
qtd_pares = 0
for i in range(1, 6):
    num = float(input(f"Digite o {i}° número: "))
    
    if num % 2 == 0:
        media += num
        qtd_pares += 1

if qtd_pares > 0:
    media /= qtd_pares
    print(f"A média dos números pares é: {media}")
else:
    print("Nenhum número par foi digitado.")