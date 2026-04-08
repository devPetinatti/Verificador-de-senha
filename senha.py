# usei a biblioteca "re" para o código realizar a verificação de itens semelhantes

import re

senha = input("Digite uma senha: ")

forca = 0

# esse código verifica o tamanho da senha
if len(senha) >= 8:
    forca += 1

# esse já verifica se há letras maiúsculas
if re.search(r"[A-Z]", senha):
    forca += 1

# e esse letras minúsculas
if re.search(r"[a-z]", senha):
    forca += 1

# o codigo observa números com esse
if re.search(r"[0-9]", senha):
    forca += 1

# e símbolos nesse
if re.search(r"[!@#$%^&*(),.?\":{}|<>]", senha):
    forca += 1

# aqui o resultado
if forca <= 2:
    print("Senha fraca")
elif forca == 3 or forca == 4:
    print("Senha média")
else:
    print("Senha forte")
