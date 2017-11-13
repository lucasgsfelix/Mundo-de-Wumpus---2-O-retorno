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

def arrumaCaminhoVisitado(caminho_visitado):
	xy = []
	i=0
	while(i<len(caminho_visitado)):
		lista = []
		x = caminho_visitado[i][0]
		y = caminho_visitado[i][1]
		lista.append(int(x))
		lista.append(int(y))
		xy.append(lista)
		i=i+1
	return xy

def inducao(mapa_descoberto,posicao,angulo,caminho_visitado):
	"""Resolve o problema de indecisão"""
	# 2 brisa,
	i=0

	caminho_visitado=arrumaCaminhoVisitado(caminho_visitado)

	estados=[2,1,3,4,5,6]

	acrescimo=0.25
	#dicionario com as probabilidades
	probabilidade=preenche_dicio()
	#exibe_mapa(mapa_descoberto)
	for linha in range(0,len(mapa_descoberto)):
		for coluna in range(0, len(mapa_descoberto[linha])):
			if (mapa_descoberto[linha][coluna] in estados):
				if((coluna+1)<4):
					probabilidade[linha,coluna+1]+=acrescimo
				if((coluna-1)>=0):
					probabilidade[linha,coluna-1]+=acrescimo
				if((linha+1)<4):
					probabilidade[linha+1,coluna]+=acrescimo
				if((linha-1)>=0):
					probabilidade[linha-1,coluna]+=acrescimo
		# 	print posicao
		# print "--------------"
	#exibe_probabilidade(probabilidade)
	#print "Posicao",posicao,"Angulo",angulo
	#print "Já visitado",caminho_visitado
	#mapa_descoberto[posicao[0]][posicao[1]]="P "+str(90)
	#exibe_mapa(mapa_descoberto)
	#print "Zerada"
	probabilidade = marca_visitado(probabilidade, caminho_visitado)
	#exibe_probabilidade(probabilidade)
	escolhas=processa_estado(probabilidade, posicao,angulo)
	return escolhas[0][1],probabilidade
	
#caminho_visitado= []#[[0,0],[0,1],[0,2],[2,3],[0,3],[3,3],[1,2]]
#print inducao(mapa_descoberto,[0,0],0,caminho_visitado)
