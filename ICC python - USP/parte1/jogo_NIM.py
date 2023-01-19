# n é o número de peças
# m é o número máximo de peças que podem ser retiradas numa rodada

def main():
	print("Bem-vindo ao jogo do NIM! Escolha:\n")
	jogo=int(input("1 - para jogar uma partida isolada\n2 - para jogar um campeonato "))
	if jogo==1:
		print("\nVoce escolheu uma partida isolada!\n")
		partida()
	if jogo==2:
		print("\nVoce escolheu um campeonato!\n")
		voce=0
		computador=0
		ganhador=0
		for i in range (0,3):
			print(f"**** Rodada {i+1} ****\n")
			ganhador=partida()
			if ganhador=="computador":
				computador+=1
			else:
				voce+=1
		print("**** Final do campeonato! ****\n")
		print(f"Placar: Você {voce} X {computador} Computador")

def partida():
	n=int(input("Quantas peças? "))
	m=int(input("Limite de peças por jogada? "))
	while m<=0 or m>=n:
		m=int(input("Limite de peças por jogada? "))
	if n%(m+1)==0:
		print("\nVocê começa!\n")
		ganhador="ninguem"
		while (n>0 and ganhador=="ninguem"):
			jogada=usuario_escolhe_jogada(n, m)
			if jogada==1:
				print("\nVocê tirou uma peça.")
			else:
				print(f"Voce tirou {jogada} peças.")
			n=n-jogada
			if n==1:
				print("Agora resta apenas uma peça no tabuleiro.\n")
			if n>0 and n!=1:
				print(f"Agora restam {n} peças no tabuleiro.\n")
			if n>0:
				jogada=computador_escolhe_jogada(n, m)
				if jogada==1:
					print("O computador tirou uma peça.")
				else:
					print(f"O computador tirou {jogada} peças.")
				n=n-jogada
				if n==0:
					print("Fim do jogo! O computador ganhou!\n")
					ganhador="computador"
				if n==1:
					print("Agora resta apenas uma peça no tabuleiro.\n")
				if n>0 and n!=1:
					print(f"Agora restam {n} peças no tabuleiro.\n")
	else:
		print("\nComputador começa!\n")
		ganhador="ninguem"
		while (n>0 and ganhador=="ninguem"):
			jogada=computador_escolhe_jogada(n, m)
			if jogada==1:
				print("O computador tirou uma peça.")
			else:
				print(f"O computador tirou {jogada} peças.")
			n=n-jogada
			if n==0:
				print("Fim do jogo! O computador ganhou!\n")
				ganhador="computador"
			if n==1:
				print("Agora resta apenas uma peça no tabuleiro.\n")
			if n>0 and n!=1:
				print(f"Agora restam {n} peças no tabuleiro.\n")
			if n>0:
				jogada=usuario_escolhe_jogada(n, m)
				if jogada==1:
					print("\nVocê tirou uma peça.")
				else:
					print(f"Voce tirou {jogada} peças.")
				n=n-jogada
				if n==1:
					print("Agora resta apenas uma peça no tabuleiro.\n")
				if n>0 and n!=1:
					print(f"Agora restam {n} peças no tabuleiro.\n")
	return ganhador
	
def computador_escolhe_jogada(n, m):
	i=0
	ver=0
	while (i<m and ver==0 and i!=n):
		i+=1
		if (n-i)%(m+1)==0:
			ver=1	
	return i

def usuario_escolhe_jogada(n, m):
	jogada=int(input("Quantas peças você vai tirar? "))
	while jogada>m or jogada<=0:
		print("\nOops! Jogada inválida! Tente de novo.")
		jogada=int(input("\nQuantas peças você vai tirar? "))
	return jogada


main()

# Arrumar as mensagens de quem ganhou, elas devem estar na função partida
# Tem que da um jeito de contar quantas partidas cada um vence