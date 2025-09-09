def ler_dados():
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    return nome, idade

def verificar_idade(idade):
    return "Maior de idade" if idade >= 18 else "Menor de idade"

def exibir_resultado(nome, resultado):
    print(f"{nome} é {resultado}")

def main():
    nome, idade = ler_dados()
    resultado = verificar_idade(idade)
    exibir_resultado(nome, resultado)

main()

def ler_dados():
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    return nome, idade

def verificar_idade(idade):
    return "Maior de idade" if idade >= 18 else "Menor de idade"

def exibir_resultado(nome, resultado):
    print(f"{nome} é {resultado}")

def main():
    resultados = []
    
    for i in range(5):
        print(f"\nPessoa {i+1}:")
        nome, idade = ler_dados()
        resultado = verificar_idade(idade)
        exibir_resultado(nome, resultado)
        resultados.append((nome, resultado))
    
    print("\nResumo dos resultados:")
    for nome, resultado in resultados:
        print(f"{nome} -> {resultado}")

main()