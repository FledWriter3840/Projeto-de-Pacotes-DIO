import string

def avaliar_forca(senha):
    """
    Avalia a força da senha.
    Retorna: "Fraca", "Média" ou "Forte"
    """
    tem_maiuscula = any(c.isupper() for c in senha)
    tem_minuscula = any(c.islower() for c in senha)
    tem_digito = any(c.isdigit() for c in senha)
    tem_simbolo = any(c in string.punctuation for c in senha)
    
    pontuacao = sum([tem_maiuscula, tem_minuscula, tem_digito, tem_simbolo])

    if len(senha) >= 12 and pontuacao == 4:
        return "Forte"
    elif len(senha) >= 8 and pontuacao >= 2:
        return "Média"
    else:
        return "Fraca"
