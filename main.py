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
