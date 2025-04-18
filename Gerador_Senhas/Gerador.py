import random
import string

def gerar_senha(tamanho=12, usar_simbolos=True):
    """
    Gera uma senha aleatória.
    """
    caracteres = string.ascii_letters + string.digits
    if usar_simbolos:
        caracteres += string.punctuation

    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha
