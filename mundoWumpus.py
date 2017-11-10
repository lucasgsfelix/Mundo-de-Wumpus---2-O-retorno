#!/usr/bin/env python2.7.12
#-*- coding: utf-8 -*-
from random import randint
from mapa import *
from jogador import *





if __name__ == "__main__":

	mapa = [[0,0,0,0],
			[0,0,0,0],
			[0,0,0,0],
			[0,0,0,0]]

	mapaJogador =  [[None,None,None,None],
					[None,None,None,None],
					[None,None,None,None],
					[None,None,None,None]]
	
	mapaVisitado = [[0,0,0,0],
					[0,0,0,0],
					[0,0,0,0],
					[0,0,0,0]]


	mapa =  definePocoWumpus(mapa)  #### ao fim mapa está pronto
	mapa = defineOuro(mapa)
	caminhaNoMapa(mapa, mapaJogador, mapaVisitado)


