def solicitar_login():
    return input("Digite a senha: ")

def verificar_login(senha, tentativa):
    return senha == tentativa

def main_login():
    senha = "1234"
    tentativas = 0

    while tentativas < 3:
        tentativa = solicitar_login()
        if verificar_login(senha, tentativa):
            print("Login bem-sucedido!")
            return
        else:
            print("Senha incorreta.")
            tentativas += 1
    
    print("Número máximo de tentativas atingido. Acesso bloqueado.")

main_login()

def main_login():
    senha = "1234"
    tentativas = 0

    while tentativas < 3:
        tentativa = solicitar_login()
        tentativas += 1  
        if verificar_login(senha, tentativa):
            print("Login bem-sucedido!")
            print(f"Você fez {tentativas} tentativa(s).")
            return
        else:
            print("Senha incorreta.")
    
    print("Número máximo de tentativas atingido. Acesso bloqueado.")
    print(f"Total de tentativas: {tentativas}")

main_login()