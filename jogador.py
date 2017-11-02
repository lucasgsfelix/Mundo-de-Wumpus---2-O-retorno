#!/usr/bin/env python2.7.12
#-*- coding: utf-8 -*-
from random import randint

angulo = 0
pontuacao = 0
listaPontuacao = []

def caminhaNoMapa(mapa, mapaJogador):
	i=0
	j=0
	while(True):

		if(mapa[i][j]=='ouro'):
			print 'PARABÉNS, VOCÊ CONSEGUIU ALCANÇAR O OURO !!!'
			print 'SUA PONTUAÇÃO FOI DE \n', pontuacao
			print 'SUA LISTA DE AÇÕES FOI \n', ''.join(listaPontuacao)
			print 'SEU MAPA DESCOBERTO FOI \n', printMapa(mapaJogador)
			break


		elif(mapa[i][j]==0):
			#atualizo no mapa do jogador que não há perigo a vista
			abreMapa(0, mapaJogador, i, j) # onde é 1, quer dizer que não há perigo à vista

			## tenho que definir para onde irei andar

			avaliaAngulos(linha, coluna)

		elif(mapa[i][j]%2==0): #tenho poço por perto

			abreMapa(2, mapaJogador, i, j)

			## tenho que definir para onde irei andar


		elif(mapa[i][j]==1): #tenho wumpus por perto

			abreMapa(1, mapaJogador, i, j) #quer dizer que eu tenho wumpus perto

			## tenho que definir para onde irei andar

		elif(mapa[i][j]%2!=0): #tenho poço e wumpus por perto  

			abreMapa(3, mapaJogador, i, j)

			## tenho que definir para onde irei andar


def avaliaAngulos(linha, coluna):

	if (angulo==0) and (coluna<3):

		return linha, coluna+1

	elif (angulo==90) and (linha>0):

		return linha+1, coluna

	elif (angulo==180) and (coluna>0):

		return linha, coluna-1

	elif (angulo==270) and (linha<3):

		return linha-1, coluna

	else: # tenho que fazer avaliações otimizadas aqui

		return avaliaAngulosEspeciais(linha, coluna)


def calculo(x, y):
	medidaDesempenho(-1, "MUDOU O ÂNGULO DE "+str(x)+" PARA "+str(y))
	angulo=y
	#medidaDesempenho(-1, "CAMINHOU DA SALA ", str(linha), str(coluna), "PARA A SALA", str(linha+v1), str(coluna+v2))

def avaliaAngulosEspeciais(linha, coluna):
	
	if (angulo==0):
		avaliacaoAngulos(coluna, linha, 3, 3, 0, 0, 90, 270)
	elif (angulo==90): #verifico a linha	
		avaliacaoAngulos(linha, coluna, 0, 0, 3, 90, 0, 180)
	elif (angulo==180):
		avaliacaoAngulos(coluna, linha, 0, 0, 3, 180, 90, 270)
	elif(angulo==270):
		avaliacaoAngulos(linha, coluna, 3, 3, 0, 270, 0, 180)

	return linha, coluna

def avaliacaoAngulos(linha, coluna, valor1, valor2, valor3, angulo1, angulo2, angulo3):
	if(linha==valor1):
		if(coluna==valor2):
			calculo(angulo1, angulo2)
		elif(coluna==valor3):
			calculo(angulo1, angulo3)
		else:
			aux = randint(0, 1) 
			if(aux==0):
				calculo(angulo1, angulo2)
			else:
				calculo(angulo1, angulo3)


def medidaDesempenho(x, acao):
	listaPontuacao.append(acao)
	listaPontuacao.append('\n')
	pontuacao = pontuacao + x

def abreMapa(p, mapa, linha, coluna):

	if linha>0 and mapa[linha-1][coluna] != '@' and mapa[linha-1][coluna] != '#':
		mapa[linha-1][coluna] = mapa[linha-1][coluna] + p
	if linha<3 and mapa[linha+1][coluna] != '@' and mapa[linha+1][coluna] != '#':
		mapa[linha+1][coluna] = mapa[linha+1][coluna] + p
	if coluna>0 and mapa[linha][coluna-1] != '@' and mapa[linha][coluna-1] != '#':
		mapa[linha][coluna-1] = mapa[linha][coluna-1] + p
	if coluna<3 and mapa[linha][coluna+1] != '@' and mapa[linha][coluna+1] != '#':
		mapa[linha][coluna+1] = mapa[linha][coluna+1] + p

	return mapa