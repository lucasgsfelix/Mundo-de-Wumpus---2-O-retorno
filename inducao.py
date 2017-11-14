# -*- coding: utf-8 -*-



import random
import numpy as np




def regra_deslocamento(linha,coluna):
	pass

def preenche_dicio():
	probabilidade={}
	for i in range(0,4):
		for j in range(0,4):
			probabilidade[i,j]= 0
	return probabilidade

def exibe_probabilidade(probabilidade):
	"""Exibe a probabilidade"""
	for i in list(probabilidade):
		print i,probabilidade[i]

def exibe_mapa(mapa_descoberto):
	print "Matriz Completa"
	for i in mapa_descoberto:
		print i
	print"-----------------"

def marca_visitado(probabilidade,caminho_visitado):
	"""Marca o caminho como visitado"""
	for i in caminho_visitado:
		probabilidade[i[0],i[1]] = 0
	return probabilidade
def ordena(caminhos,chave):
	lista=[]
	listaf=[]
	for i in caminhos:
		listaf.append(i[chave])
	listaf= np.argsort(listaf)
	#print listaf
	for i in listaf:
		lista.append(caminhos[i])
	return lista
def processa_estado(probabilidade,posicao,angulo):
	"""Processa o estado de acordo com os dados de entrada"""
	"""Posicao[[linha],[coluna]]"""
	#print "--- Processando estados ----"
	linha = posicao[0]
	coluna = posicao[1]
	caminhos= []
	#print "Posicao",posicao
	if((coluna+1)<4):
		#print "Prob",probabilidade[linha,coluna+1]
		#print "Deslocamento",[linha,coluna+1]
		caminhos.append([probabilidade[linha,coluna+1],[linha,coluna+1],0])
	if((coluna-1)>=0):
		#print probabilidade[linha,coluna-1]
		#print "Deslocamento",[linha,coluna-1]
		caminhos.append([probabilidade[linha,coluna-1],[linha,coluna-1],180])
	if((linha+1)<4):
		#print probabilidade[linha+1,coluna]
		#print "Deslocamento",[linha+1,coluna]
		caminhos.append([probabilidade[linha+1,coluna],[linha+1,coluna],270])
	if((linha-1)>=0):
		#print probabilidade[linha-1,coluna]
		#print "Deslocamento",[linha-1,coluna]
		caminhos.append([probabilidade[linha-1,coluna],[linha-1,coluna],90])
	#print caminhos
	#print "---------------" 
	lista=ordena(caminhos,2)
	lista =ordena(caminhos,0)
	
	return lista

def verifica_visitado(posicao,caminho):
	if(posicao in caminho):
		return True
	else:
		return False

def inducao(mapa_descoberto,posicao,angulo,caminho_visitado):
	"""Resolve o problema de indecisão"""
	# 2 brisa,
	estados=[2,1,3,4,5,6]

	acrescimo=0.25
	estado_especial = False
	#dicionario com as probabilidades
	probabilidade=preenche_dicio()
	#exibe_mapa(mapa_descoberto)
	for linha in range(0,len(mapa_descoberto)):
		for coluna in range(0, len(mapa_descoberto[linha])):
			if (mapa_descoberto[linha][coluna] in estados):

				if((linha is 0) and (coluna is 3)):
					if(verifica_visitado([linha,coluna-1],caminho_visitado)):
						probabilidade[linha+1,coluna]=1
						estado_especial= True
				elif((linha is 1) and (coluna is 0)):
					if(verifica_visitado([linha,coluna+1],caminho_visitado)):
						probabilidade[linha+1,coluna-1]=1
						estado_especial= True
				elif((linha is 2) and (coluna is 0)):
					if(verifica_visitado([linha,coluna+1],caminho_visitado)):
						probabilidade[linha+1,coluna+1]=1
						estado_especial= True
				else:
					if((coluna+1)<4):
						probabilidade[linha,coluna+1]+=acrescimo
					if((coluna-1)>=0):
						probabilidade[linha,coluna-1]+=acrescimo
					if((linha+1)<4):
						probabilidade[linha+1,coluna]+=acrescimo
					if((linha-1)>=0):
						probabilidade[linha-1,coluna]+=acrescimo
	probabilidade = marca_visitado(probabilidade, caminho_visitado)
	#exibe_probabilidade(probabilidade)
	escolhas=processa_estado(probabilidade, posicao,angulo)
	print type(probabilidade)
	mapaProbabilidade = geraMapaProbabilidades(probabilidade)
	mapaProbabilidade = zeraProb(mapaProbabilidade, caminho_visitado)
	if estado_especial is True:
		return posicao,mapaProbabilidade
	return escolhas[0][1], mapaProbabilidade

def zeraProb(mapaProbabilidade, caminhosVisitados):

	i=0
	while(i<len(mapaProbabilidade)):
		j=0
		while(j<len(mapaProbabilidade[i])):
			
			if any (mapaProbabilidade[i][j] == k for k in caminhosVisitados):

				mapaProbabilidade[i][j] = 0
				
			j=j+1

		i=i+1

	return mapaProbabilidade

def geraMapaProbabilidades(tabelaProbabilidade): 
	#print "TIPO",type(tabelaProbabilidade)
	i=0
	mapa = [[0,0,0,0],
			[0,0,0,0],
			[0,0,0,0],
			[0,0,0,0]]
	#value é a probabilidade
	while(i<len(tabelaProbabilidade.values())):
		posicao = tabelaProbabilidade.keys()[i]
		if(type(posicao[0])==str) and (type(posicao[1])==str):
			mapa[int(posicao[0])][int(posicao[1])] = tabelaProbabilidade.values()[i]
		else:
			mapa[posicao[0]][posicao[1]] = tabelaProbabilidade.values()[i]
		i=i+1


	return mapa
	