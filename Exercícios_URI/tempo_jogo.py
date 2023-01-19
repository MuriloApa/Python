start, end = map(int, input().split())
if (end == start):
    print(f"O JOGO DUROU 24 HORA(S)")
else:
    if (end > start):
        print(f"O JOGO DUROU {end - start} HORA(S)")
    else:
        print(f"O JOGO DUROU {end - start + 24} HORA(S)")
