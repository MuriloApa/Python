x, y = map(float, input().split())


if (x == 0 and y == 0):
    print('Origem')
else:
    if (x == 0):
        print('Eixo Y')
    else:
        if (y == 0):
            print('Eixo X')
        else:
            if (x > 0 and y > 0):
                print('Q1')
            if (x > 0 and y < 0):
                print('Q4')
            if (x < 0 and y > 0):
                print('Q2')
            if (x < 0 and y < 0):
                print('Q3')