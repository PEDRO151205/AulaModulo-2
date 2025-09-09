def expansao1():
    print("Bem-vindo à Expansão 1!")
    
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    
    print(f"Olá, {nome}! Você tem {idade} anos.")
    
    if idade >= 18:
        print("Você é maior de idade.")
    else:
        print("Você é menor de idade.")

expansao1()        
        

def somar_lista_com_while():
    numeros = []
    while True:
        entrada = input("Digite um número (ou 'sair' para terminar): ")
        if entrada.lower() == "sair":
            break
        try:
            numeros.append(float(entrada))  
        except ValueError:
            print("Por favor, digite um número válido.")
    
    return sum(numeros)

print(f"A soma é: {somar_lista_com_while()}")