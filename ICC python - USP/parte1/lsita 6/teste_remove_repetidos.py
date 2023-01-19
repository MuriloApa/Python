
def remove_repetidos(vet):
	vet2=[]
	for i in range(len(vet)):
		ver=0
		for j in range(i-1, -1, -1):
			if j>=0 and vet[j]==vet[i]:
				ver=1
		if ver==0:
			vet2.append(vet[i])
	vet2.sort()
	return vet2