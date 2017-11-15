# -*- coding: utf-8 -*-



def inducaoLogica(mapaJogador, i, j, conhecidos):
    # ---- lógica pra quando eu tenho 2 ou 1 
	## apartir de uma posição i, j, onde foi identificado um 2, verifico todos os locais 
	## ao redor dele que podem ser @
	## e apartir da posição desse posso, vejo se a suas adjacências são 2, caso seja
	## garanto o local onde esta o poço
	posicoesBuraco = []
	if(i>0):
		posicoesBuraco.append(str(i-1)+str(j)+'\t') #vou dar um split nesse \t
	if(i<3):
		posicoesBuraco.append(str(i+1)+str(j)+'\t')
	if(j>0):
		posicoesBuraco.append(str(i)+str(j-1)+'\t')
	if(j<3):
		posicoesBuraco.append(str(i)+str(j+1)+'\t')

	return verificaPossiblidade(posicoesBuraco, conhecidos, mapaJogador)


def verificaPossiblidade(posicoesBuraco, conhecidos, mapaJogador):


	item = 1 # vai definir se tenho que comparar com buraco ou wumpus
	posicoesBuraco = ''.join(posicoesBuraco).split('\t')
	posicoesBuraco.remove('')
	i=0
	### retira posições já conhecidas da lista de possiveis posicoes de buraco
	while(i<len(posicoesBuraco)):
		if any (int(posicoesBuraco[i])== k for k in conhecidos):
			posicoesBuraco.pop(i)
		i=i+1
	# agora vou testar as possibilidades para cada um dos buracos

	k=0
	certezaBuraco = []
	while(k<len(posicoesBuraco)):

		p = posicoesBuraco[k]

		i = int(p[0])
		j = int(p[1])

		##agora verifico as adjascências do buraco
		cont = 0

		if(i>0):
			if(mapaJogador[i-1][j] == item):
				cont=cont+1
		if(i<3):
			if(mapaJogador[i+1][j] == item):
				cont=cont+1
		if(j>0):
			if(mapaJogador[i][j-1] == item):
				cont=cont+1
		if(j<3):
			if(mapaJogador[i][j+1] == item):
				cont=cont+1

		if(cont>1):
			certezaBuraco.append(str(i)+str(j))

		k=k+1
	return certezaBuraco



