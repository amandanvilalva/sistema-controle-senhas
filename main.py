import os
import base64
import random
import string

# Dicionário para armazenar as senhas
senhas = {}

# Funções principais
def armazenar_senha():
    servico = input("Digite o nome do serviço: ")
    senha = input("Digite a senha: ")
    
    # Criptografa a senha
    senha_criptografada = base64.b64encode(senha.encode()).decode()
    senhas[servico] = senha_criptografada
    print(f"Senha para '{servico}' armazenada com sucesso!")

def recuperar_senha():
    servico = input("Digite o nome do serviço para recuperar a senha: ")
    if servico in senhas:
        senha_criptografada = senhas[servico]
        senha_decifrada = base64.b64decode(senha_criptografada).decode()
        print(f"A senha para '{servico}' é: {senha_decifrada}")
    else:
        print(f"Nenhuma senha encontrada para o serviço '{servico}'.")

def gerar_senha():
    tamanho = int(input("Digite o tamanho da senha a ser gerada (padrão: 12): ") or 12)
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha_gerada = ''.join(random.choice(caracteres) for _ in range(tamanho))
    print(f"Senha gerada: {senha_gerada}")

def exportar_backup():
    caminho = input("Digite o nome do arquivo para exportar (ex.: backup.txt): ")
    try:
        with open(caminho, "w") as arquivo:
            for servico, senha_criptografada in senhas.items():
                arquivo.write(f"{servico}:{senha_criptografada}\n")
        print(f"Backup exportado com sucesso para '{caminho}'!")
    except Exception as e:
        print(f"Erro ao exportar backup: {e}")

# Menu principal
def menu():
    while True:
        print("\n--- Sistema de Controle de Senhas ---")
        print("1. Armazenar senha")
        print("2. Recuperar senha")
        print("3. Gerar senha segura")
        print("4. Exportar backup")
        print("5. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            armazenar_senha()
        elif escolha == "2":
            recuperar_senha()
        elif escolha == "3":
            gerar_senha()
        elif escolha == "4":
            exportar_backup()
        elif escolha == "5":
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o menu
if __name__ == "__main__":
    menu()


def recuperar_senha(servico):
    if not os.path.exists("senhas.txt"):
        print("Nenhuma senha armazenada!")
        return
    with open("senhas.txt", "r") as f:
        for linha in f:
            serv, senha_codificada = linha.strip().split(":")
            if serv == servico:
                senha = base64.b64decode(senha_codificada.encode("utf-8")).decode("utf-8")
                print(f"Senha para {servico}: {senha}")
                return
    print("Serviço não encontrado!")

def exportar_backup():
    if not os.path.exists("senhas.txt"):
        print("Nenhuma senha para exportar!")
        return
    with open("senhas.txt", "r") as f:
        dados = f.read()
    with open("backup_senhas.txt", "w") as f:
        f.write(dados)
    print("Backup exportado com sucesso!")
