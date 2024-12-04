import os
import base64

def armazenar_senha(servico, senha):
    if not os.path.exists("senhas.txt"):
        with open("senhas.txt", "w") as f:
            pass
    senha_codificada = base64.b64encode(senha.encode("utf-8")).decode("utf-8")
    with open("senhas.txt", "a") as f:
        f.write(f"{servico}:{senha_codificada}\n")
