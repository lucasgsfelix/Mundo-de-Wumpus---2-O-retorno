#!/usr/bin/env python2.7.12
#-*- coding: utf-8 -*-
from random import randint


def definePocoWumpus(mapa):
    # arroba(@) é poço ---- hashtag(#) é wumpus
    cont = 0
    posicoes = []
    while(cont < 4):
        linha = randint(0, 3)
        coluna = randint(0, 3)
        if (linha != 0) and (coluna != 0):
            if(cont == 3):  # define poço
                if(mapa[linha][coluna] != '@'):
                    posicoes.append(linha)
                    posicoes.append(coluna)
                    mapa[linha][coluna] = '#'
                    break
            else:  # define wumpus
                if(mapa[linha][coluna] != '@'):
                    posicoes.append(linha)
                    posicoes.append(coluna)
                    mapa[linha][coluna] = '@'
                    cont = cont + 1
    # agora eu preciso colocar a brisa
    i = 0
    j = 0
    while(True):

        linha = posicoes[j]
        coluna = posicoes[j + 1]
        j = j + 2
        # quando alocar eu ando

        # posições possíveis de eu colocar o fedo
        mapa = alocaPercepcoes(2, mapa, linha, coluna)

        i = i + 1
        # colocando a brisa
        if (i == 3):
            linha = posicoes[j]
            coluna = posicoes[j + 1]
            return alocaPercepcoes(1, mapa, linha, coluna)


def defineOuro(mapa):
    while(True):
        linha = randint(0, 3)
        coluna = randint(0, 3)

        if(mapa[linha][coluna] != '@'):
            if(mapa[linha][coluna] == '#'):
                mapa[linha][coluna] = '#ouro'
            else:
                mapa[linha][coluna] = 'ouro'
            return mapa


def printMapa(mapa):
    i = 0
    while(i < len(mapa)):
        print mapa[i]
        i = i + 1


def alocaPercepcoes(p, mapa, linha, coluna):
    if linha > 0 and mapa[linha - 1][coluna] != '@' and mapa[linha - 1][coluna] != '#':
        mapa[linha - 1][coluna] = mapa[linha - 1][coluna] + p
    if linha < 3 and mapa[linha + 1][coluna] != '@' and mapa[linha + 1][coluna] != '#':
        mapa[linha + 1][coluna] = mapa[linha + 1][coluna] + p
    if coluna > 0 and mapa[linha][coluna - 1] != '@' and mapa[linha][coluna - 1] != '#':
        mapa[linha][coluna - 1] = mapa[linha][coluna - 1] + p
    if coluna < 3 and mapa[linha][coluna + 1] != '@' and mapa[linha][coluna + 1] != '#':
        mapa[linha][coluna + 1] = mapa[linha][coluna + 1] + p

    return mapa
