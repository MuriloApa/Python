def maiusculas(mensagem):
    letras =""
    for i in range(len(mensagem)):
        if ord(mensagem[i]) >= 65 and ord(mensagem[i]) <= 90:
            letras += mensagem[i]

    return letras
