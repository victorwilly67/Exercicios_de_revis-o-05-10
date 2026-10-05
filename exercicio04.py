qtd_pares = 0 
qtd_impares = 0
soma_pares = 0
soma_impares = 0 

for i in range(1, 11):
    num = float(input(f"Digite o {i}° número: "))
    
    if num % 2 == 0:
        qtd_pares += 1
        soma_pares += num
    else:
        qtd_impares += 1
        soma_impares += num 

print(f"Quantidade de números pares: {qtd_pares}")
print(f"Quantidade de números ímpares: {qtd_impares}")
print(f"Soma dos números pares: {soma_pares}")
print(f"Soma dos números ímpares: {soma_impares}")