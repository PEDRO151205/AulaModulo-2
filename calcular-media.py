def calcular_media(lista):
    media = sum(lista) / len(lista)
    print(f"Média: {media:.2f}")
    
    if media >= 7:
        print("Aprovado")
    else:
        print("Reprovado")
    
    return media

# Exemplo de uso:
notas = [8, 7, 6, 9]
calcular_media(notas)