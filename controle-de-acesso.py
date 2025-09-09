def ler_pessoa():
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    return nome, idade


def verificar_idade(idade):
    return idade >= 18

def acumular_resultados(nome, maior_idade, lista_resultados):
    lista_resultados.append((nome, maior_idade))


def mostrar_resumo(resultados):
    aprovados = sum(1 for _, maior in resultados if maior)
    recusados = sum(1 for _, maior in resultados if not maior)
    
    print("\nResumo:")
    for nome, maior in resultados:
        status = "Maior de idade" if maior else "Menor de idade"
        print(f"{nome}: {status}")
    
    print(f"\nTotal de maiores de idade: {aprovados}")
    print(f"Total de menores de idade: {recusados}")


def main():
    resultados = []
    
    for i in range(5):
        print(f"\nPessoa {i+1}:")
        nome, idade = ler_pessoa()
        maior = verificar_idade(idade)
        acumular_resultados(nome, maior, resultados)
    
    mostrar_resumo(resultados)


main()