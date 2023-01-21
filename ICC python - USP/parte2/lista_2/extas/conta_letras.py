def conta_letras(frase, contar="vogais"):
    cont = 0
    frase = frase.casefold()
    for i in range(len(frase)):
        if contar == "vogais" and (frase[i] == 'a' or frase[i] == 'e' or frase[i] == 'i' or frase[i] == 'o' or frase[i] == 'u'):
            cont += 1
        if contar == "consoantes" and (frase[i] != 'a' and frase[i] != 'e' and frase[i] != 'i' and frase[i] != 'o' and frase[i] != 'u' and frase[i] != " "):
            cont += 1
    return cont
