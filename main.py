import os
import base64
import random
import string

def armazenar_senha(servico, senha):
    if not os.path.exists("senhas.txt"):
        with open("senhas.txt", "w") as f:
            pass
    senha_codificada = base64.b64encode(senha.encode("utf-8")).decode("utf-8")
    with open("senhas.txt", "a") as f:
        f.write(f"{servico}:{senha_codificada}\n")

def gerar_senha(segura=True, tamanho=12):
    caracteres = string.ascii_letters + string.digits
    if segura:
        caracteres += string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(tamanho))

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
