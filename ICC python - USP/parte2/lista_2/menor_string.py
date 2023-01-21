def menor_nome(string_list):
    menor = string_list[0].strip().casefold().capitalize()
    for i in string_list:
        if len(i.strip()) < len(menor.strip()):
            menor = i.strip().casefold().capitalize()
    return menor
