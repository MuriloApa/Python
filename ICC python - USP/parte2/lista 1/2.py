def soma_matrizes(m1, m2):
    if (len(m1) == len(m2) and len(m1[0]) == len(m2[0])):
        r =[]
        for i in range(len(m1)):
            r_linha = []
            for j in range(len(m1[i])):
                r_linha.append(m1[i][j] + m2[i][j])
            r.append(r_linha)
        return r
    else:
        return False

