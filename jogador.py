#!/usr/bin/env python2.7.12
#-*- coding: utf-8 -*-
from random import randint
from mapa import *
from inducao import *
import time

angulo = 0
pontuacao = 0
listaPontuacao = []

def calculaNovoAngulo(linha_antiga, coluna_antiga, i, j):

	if(linha_antiga<i): #quer dizer que fui pra trás
		angulo = 270
	elif(linha_antiga>i):
		angulo = 90
	elif(coluna_antiga<j):
		angulo = 0
	elif(coluna_antiga>j):
		angulo = 180

def caminhoDeVoltaPoco(mapa, i, j):

	###descobre o caminho pelo o qual o herói veio
	linha_antiga = i
	coluna_antiga = j
	if (i>0) and (mapa[i-1][j]!='@'): #diferente de poço --- tenho que olhar o angulo
		medidaDesempenho(-1, "CAMINHOU DA SALA "+ str(i)+ str(j)+ " PARA A SALA "+str(i-1)+ str(j))
		i = i -1
	elif (i<3) and (mapa[i+1][j]!='@'):
		medidaDesempenho(-1, "CAMINHOU DA SALA "+ str(i)+ str(j)+ " PARA A SALA "+str(i+1)+ str(j))
		i = i +1
	elif (j>0) and (mapa[i][j-1]!='@'):
		medidaDesempenho(-1, "CAMINHOU DA SALA "+ str(i)+ str(j)+ " PARA A SALA "+str(i)+ str(j-1))
		j=j-1
	elif (j<3) and (mapa[i][j+1]!='@'):
		medidaDesempenho(-1, "CAMINHOU DA SALA "+ str(i)+ str(j)+ " PARA A SALA "+str(i)+ str(j+1))
		j=j-1

	calculaNovoAngulo(linha_antiga, coluna_antiga, i, j)
	

	return i, j

def caminhoDeVoltaWumpus(mapa, i, j):

	###descobre o caminho pelo o qual o herói veio
	linha_antiga = i
	coluna_antiga = j

	if (i>0) and (mapa[i-1][j]!='#'): #diferente de poço --- tenho que olhar o angulo
		medidaDesempenho(-1, "CAMINHOU DA SALA "+ str(i)+ str(j)+ " PARA A SALA "+str(i-1)+ str(j))
		i = i -1
	elif (i<3) and (mapa[i+1][j]!='#'):
		medidaDesempenho(-1, "CAMINHOU DA SALA "+ str(i)+ str(j)+ " PARA A SALA "+str(i+1)+ str(j))
		i = i +1
	elif (j>0) and (mapa[i][j-1]!='#'):
		medidaDesempenho(-1, "CAMINHOU DA SALA "+ str(i)+ str(j)+ " PARA A SALA "+str(i)+ str(j-1))
		j=j-1
	elif (j<3) and (mapa[i][j+1]!='#'):
		medidaDesempenho(-1, "CAMINHOU DA SALA "+ str(i)+ str(j)+ " PARA A SALA "+str(i)+ str(j+1))
		j=j-1

	calculaNovoAngulo(linha_antiga, coluna_antiga, i, j)

	return i, j

def caminhoDeVolta(mapa, i, j):

	linha_antiga = i
	coluna_antiga = j


	if (i>0) and (mapa[i-1][j]!='@') and (mapa[i-1][j]!='#'): #diferente de poço --- tenho que olhar o angulo
		medidaDesempenho(-1, "CAMINHOU DA SALA "+ str(i)+ str(j)+ " PARA A SALA "+str(i-1)+ str(j))
		i = i -1
	elif (i<3) and (mapa[i+1][j]!='@') and (mapa[i+1][j]!='#'):
		medidaDesempenho(-1, "CAMINHOU DA SALA "+ str(i)+ str(j)+ " PARA A SALA "+str(i+1)+ str(j))
		i = i +1
	elif (j>0) and (mapa[i][j-1]!='@') and (mapa[i+1][j]!='#'):
		medidaDesempenho(-1, "CAMINHOU DA SALA "+ str(i)+ str(j)+ " PARA A SALA "+str(i)+ str(j-1))
		j=j-1
	elif (j<3) and (mapa[i][j+1]!='@') and (mapa[i+1][j]!='#'):
		medidaDesempenho(-1, "CAMINHOU DA SALA "+ str(i)+ str(j)+ " PARA A SALA "+str(i)+ str(j+1))
		j=j-1

	calculaNovoAngulo(linha_antiga, coluna_antiga, i, j)

	return i, j

def caminhaNoMapa(mapa, mapaJogador, mapaVisitado):
	i=0
	j=0
	flag=0
	global angulo
	ultimosVisitados = []
	quantIteracoes = 0
	mapaAux  = []
	verticesSemBuraco = []
	while(True):
		#time.sleep(4)

		if(mapa[i][j]=='ouro'):
			print 'PARABÉNS, VOCÊ CONSEGUIU ALCANÇAR O OURO !!!'
			print 'SUA PONTUAÇÃO FOI DE \n', pontuacao
			print 'SUA LISTA DE AÇÕES FOI \n', ''.join(listaPontuacao)
			print 'SEU MAPA DESCOBERTO FOI \n', printMapa(mapaJogador)
			print 'O MAPA TOTAL ERA \n', printMapa(mapa)
			break

		elif((mapa[i][j]=='@')or(mapa[i][j]=='#')or(mapa[i][j]=='#ouro')):
			print 'GAME OVER!'
			if(mapa[i][j]=='@'): print "VOCÊ CAIU NUM BURACO !"
			else: print "VOCẼ FOI MORTO PELO WUMPUS !" 
			
			break

		elif(mapa[i][j]==6): #tenho poço por perto

			mapaJogador[i][j] = 6
			abreMapa('@', mapaJogador, i, j)
			## tenho que definir para onde irei andar
			###volto cuidadosamente no caminho que eu fui
			i,j = caminhoDeVoltaPoco(mapa, i, j)
			mapaJogador[i][j] = 0

		elif(mapa[i][j]==5): #tenho poço e wumpus por perto  --- tenho que fazer ele lançar a flecha
			
			mapaJogador[i][j] = 5
			
			# posso inferir onde estão os poços e wumpus

			abreMapa('#@', mapaJogador, i, j) 
			caminhoDeVolta(mapa, i, j)
			

			mapaJogador[i][j] = 0 #posicao safe
		
			## tenho que definir para onde irei andar

		elif(mapa[i][j]==4): #tenho poço 
			
			mapaJogador[i][j]=4

			abreMapa('@', mapaJogador, i, j)
			i, j = caminhoDeVoltaPoco(mapa, i, j)

			mapaJogador[i][j] = 0
		

			## tenho que definir para onde irei andar
		elif(mapa[i][j]==3): #tenho poço e wumpus por perto  
			
			mapaJogador[i][j]=3
			abreMapa('#@', mapaJogador, i, j)
			i, j = caminhoDeVolta(mapa, i, j)

			mapaJogador[i][j] = 0

			## tenho que definir para onde irei andar

		elif(mapa[i][j]==2): #tenho poço e wumpus por perto  
			
			mapaJogador[i][j] = 2
			abreMapa('@', mapaJogador, i, j)
			i, j = caminhoDeVoltaPoco(mapa, i, j)

			mapaJogador[i][j] = 0

		elif(mapa[i][j]==1): #tenho wumpus por perto
			
			mapaJogador[i][j] = 1
			abreMapa('#', mapaJogador, i, j)
			i, j = caminhoDeVoltaWumpus(mapa, i, j)

			mapaJogador[i][j] = 0

			### marco nas 


			## tenho que definir para onde irei andar
		elif(mapa[i][j]==0):

			mapaJogador[i][j]=0
			abreMapa(0, mapaJogador, i, j)
			#atualizo no mapa do jogador que não há perigo a vista
			## tenho que definir para onde irei andar
			if(i==None or j==None):
				i=0
				j=0
			i, j = avaliaAngulos(i, j, ultimosVisitados, mapaVisitado)

		
		if(mapa[i][j]!=0):
			mapaVisitado[i][j] = 1 

		if(flag==0):
			flag=1
			ultimosVisitados.append(str(i)+str(j))

		if all ((str(i)+str(j)) != k for k in  ultimosVisitados):
			ultimosVisitados.append(str(i)+str(j))

		if(quantIteracoes==0):
			mapaAux = mapaJogador

		if(contNone(mapaJogador)==contNone(mapaAux)):
			quantIteracoes = quantIteracoes + 1
			if(quantIteracoes==50):
				posicoes = []
				tabelaProbabilidade = {}
				quantIteracoes=0
				posicoes, tabelaProbabilidade = inducao(mapaJogador,[i,j],angulo,ultimosVisitados)
				mapaProbrabilidade = geraMapaProbabilidades(tabelaProbabilidade)
				quantIteracoes = 0
				i = posicoes[0]
				j = posicoes[1]
				if(type(mapaJogador[i][j])==int) and (mapaJogador[i][j]%2!=0):#quer dizer que eu to no wumpus
					mapa, mapaJogador = tacarFlecha(tabelaProbabilidade, mapa, mapaProbrabilidade)
				elif (type(mapaJogador[i][j])==int) and (mapaJogador[i][j]%2==0): #quer dizer que estou tratando buracos
					menorP = menorProbabilidade(mapaProbrabilidade)
					mapaJogador[i][j] = 0
					if(mapaProbrabilidade[i][j]==0 or mapaProbrabilidade[i][j]==menorP) and type(mapa[i][j])!=str:
						i, j = avaliaAngulos(i, j, ultimosVisitados, mapaVisitado)

				mapaAux = mapaJogador
		else:
			mapaAux = mapaJogador
			quantIteracoes = 0

def contNone(mapa):
	cont=0
	i=0
	while(i<len(mapa)):
		j=0
		while(j<len(mapa[i])):
			if(mapa[i][j]==None):
				cont=cont+1
			j=j+1
		i=i+1

	return cont

def menorProbabilidade(mapaProbrabilidade):
	aux = 1
	i=0
	x = 1
	while(i<len(mapaProbrabilidade)):
		j=0
		while(j<len(mapaProbrabilidade[i])):
			if(mapaProbrabilidade[i][j]<aux) and (mapaProbrabilidade[i][j]!=0):
				aux = mapaProbrabilidade[i][j]
			j=j+1
		i=i+1
	return aux
def tacarFlecha(tabelaProbabilidade, mapa, mapaJogador):
	posicaoCorreta = maiorValorDic(tabelaProbabilidade)
	#é hora de atirar flecha
	if((mapa[posicaoCorreta[0]][posicaoCorreta[1]]=='#')or(mapa[posicaoCorreta[0]][posicaoCorreta[1]]=='#ouro')):
		print 'PARABÉNS, VOCÊ MATOU O WUMPUS !'
		mapa=retiraWumpusFedo(mapa)
		mapaJogador=retiraWumpusFedo(mapaJogador)
	else:
		print 'ERROU A FLECHADA ! :/'
	return mapa, mapaJogador

def geraMapaProbabilidades(tabelaProbabilidade):
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
				
def retiraFalsosBuracos(tabelaProbabilidade, mapa):

	i=0
	aux = 0
	while(i<len(tabelaProbabilidade.values())):
		if(aux<tabelaProbabilidade.values()[i]):
			aux = tabelaProbabilidade.values()[i]
			p = i
		i=i+1

	del tabelaProbabilidade[tabelaProbabilidade.keys()[p]] #retiro o com maior probabilidade

	i=0
	novaProbabilidade = []
	while(i<len(tabelaProbabilidade.values())):
		if(tabelaProbabilidade.values()[i]!=0):
			novaProbabilidade.append(tabelaProbabilidade.keys()[i])
		i=i+1
	

def maiorValorDic(tabelaProbabilidade):
	i=0
	aux = 0
	while(i<len(tabelaProbabilidade.values())):
		if(aux<tabelaProbabilidade.values()[i]):
			aux = tabelaProbabilidade.values()[i]
			p = i
		i=i+1

	return tabelaProbabilidade.keys()[p]

def retiraWumpusFedo(mapa):
	i=0
	j=0
	while(i<len(mapa)):
		j=0
		while(j<len(mapa[i])):
			if(mapa[i][j]=='#'):
				mapa[i][j]=0
			elif(type(mapa[i][j])==int) and (mapa[i][j]%2!=0):
				mapa[i][j]=mapa[i][j]-1
			elif(mapa[i][j]=='#ouro'):
				mapa[i][j]='ouro'
			else:
				mapa[i][j]=mapa[i][j]
			j=j+1
		i=i+1
	return mapa


def avaliaAngulos(linha, coluna, ultimosVisitados, mapaVisitado):
	global angulo
	if (angulo==0) and (coluna<3):
		if all (str(linha)+str(coluna+1) != k for k in ultimosVisitados): # quer dizer que eu não visitei
			return linha, coluna+1
		else:
			if(linha<3):
				angulo = 270
				return linha+1, coluna
			elif(linha==3):
				angulo = 90
				return linha-1, coluna
			elif(coluna==3):
				angulo = 180
				return linha, coluna-1

	elif(angulo==0) and (coluna==3):
		if(linha==0):
			angulo = 270
			return linha+1, coluna
		elif(linha==3):
			angulo = 90
			return linha-1, coluna
		else:
			if all (str(linha-1)+str(coluna) != k for k in ultimosVisitados): # quer dizer que eu não visitei
				angulo = 90
				return linha-1, coluna

			elif all (str(linha+1)+str(coluna) != k for k in ultimosVisitados): 
				angulo = 270
				return linha+1, coluna

			elif all (str(linha)+str(coluna-1) != k for k in ultimosVisitados): 
				angulo = 180
				return linha, coluna-1

	if (angulo==90) and (linha>0):
		
		if all (str(linha-1)+str(coluna) != k for k in ultimosVisitados): # quer dizer que eu não visitei
			return linha-1, coluna
		else:
			if(coluna>0):
				angulo = 180
				return linha, coluna-1
			elif(coluna==0):
				angulo = 0
				return linha, coluna+1
			elif(linha==0):
				angulo = 270
				return linha+1, coluna

	elif(angulo==90) and (linha==0):

		if(coluna==3):
			angulo = 270
			return linha+1, coluna
		elif(coluna==0):
			angulo = 0
			return linha, coluna+1
		else:
			if all (str(linha)+str(coluna+1) != k for k in ultimosVisitados): # quer dizer que eu não visitei
				angulo = 0
				return linha, coluna+1

			elif all (str(linha+1)+str(coluna) != k for k in ultimosVisitados): 
				angulo = 270
				return linha+1, coluna

			elif all (str(linha)+str(coluna-1) != k for k in ultimosVisitados): 
				angulo = 180
				return linha, coluna-1

	if (angulo==180) and (coluna>0):

		if all (str(linha)+str(coluna-1) != k for k in ultimosVisitados): # quer dizer que eu não visitei
			return linha, coluna-1
		else:
			if(linha>0):
				angulo = 90
				return linha-1, coluna
			elif(linha==0):
				angulo = 270
				return linha+1, coluna
			elif(coluna==0):
				angulo = 0
				return linha, coluna+1
		
	
	elif(angulo==180) and (coluna==0):
		
		if(linha==0):
			angulo = 270
			return linha+1, coluna

		elif(linha==3):
			angulo = 0 
			return linha, coluna+1

		else:

			if all (str(linha)+str(coluna+1) != k for k in ultimosVisitados): # quer dizer que eu não visitei
				angulo = 0
				return linha, coluna+1

			elif all (str(linha+1)+str(coluna) != k for k in ultimosVisitados): 
				angulo = 270
				return linha+1, coluna

			elif all (str(linha-1)+str(coluna) != k for k in ultimosVisitados): 
				angulo = 90
				return linha-1, coluna



	if (angulo==270) and (linha<3):

		if all (str(linha+1)+str(coluna) != k for k in ultimosVisitados): # quer dizer que eu não visitei
			return linha+1, coluna
		else:
			if(coluna>0):
				angulo = 180
				return linha, coluna-1
			elif(coluna==0):
				angulo = 0
				return linha, coluna+1
			elif(linha==3):
				angulo = 90
				return linha-1, coluna

	elif(angulo==270) and (linha==3):

		if(coluna==0):
			angulo = 0
			return linha, coluna+1

		elif(coluna==3):
			angulo = 90
			return linha-1, coluna

		else:
			if all (str(linha)+str(coluna+1) != k for k in ultimosVisitados): # quer dizer que eu não visitei
				angulo = 0
				return linha, coluna+1

			elif all (str(linha)+str(coluna-1) != k for k in ultimosVisitados): 
				angulo = 180
				return linha, coluna-1

			elif all (str(linha-1)+str(coluna) != k for k in ultimosVisitados): 
				angulo = 90
				return linha-1, coluna

			




	'''else: # tenho que fazer avaliações otimizadas aqui
		return avaliaAngulosEspeciais(linha, coluna)'''


def calculo(x, y):

	medidaDesempenho(-1, "MUDOU O ÂNGULO DE "+str(x)+" PARA "+str(y))
	angulo=y

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
	global pontuacao
	listaPontuacao.append(acao)
	listaPontuacao.append('\n')
	pontuacao = pontuacao + x


def abreMapa(p, mapa, linha, coluna):
	
	if(type(p)!=int):

		if linha>0 and (mapa[linha-1][coluna] == None or mapa[linha-1][coluna] == 0): mapa[linha-1][coluna] = p
		if linha<3 and (mapa[linha+1][coluna] == None or mapa[linha+1][coluna] == 0): mapa[linha+1][coluna] = p
		if coluna>0 and (mapa[linha][coluna-1] == None or mapa[linha][coluna-1] == 0):mapa[linha][coluna-1] = p
		if coluna<3 and (mapa[linha][coluna+1] == None or mapa[linha][coluna+1] == 0) :mapa[linha][coluna+1] = p

	else:
		if linha>0 :
			if(mapa[linha-1][coluna]==None or type(mapa[linha-1][coluna])==str) : mapa[linha-1][coluna] = p
			else: mapa[linha-1][coluna] = mapa[linha-1][coluna] + p

		if linha<3 :
			if(mapa[linha+1][coluna]==None or type(mapa[linha+1][coluna])==str): mapa[linha+1][coluna] = p
			else: mapa[linha+1][coluna] = mapa[linha+1][coluna] + p

		if coluna>0 :
			if(mapa[linha][coluna-1]==None or type(mapa[linha][coluna-1])==str): mapa[linha][coluna-1] = p
			else: mapa[linha][coluna-1] = mapa[linha][coluna-1] + p
			
		if coluna<3 :
			if(mapa[linha][coluna+1]==None or type(mapa[linha][coluna+1])==str): mapa[linha][coluna+1] = p
			else: mapa[linha][coluna+1] = mapa[linha][coluna+1] + p
			
	return mapa



