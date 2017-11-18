#!/usr/bin/env python2.7.12
#-*- coding: utf-8 -*-
from random import randint
from mapa import *
from jogador import *
from gui import *


if __name__ == "__main__":

    mapa = [[0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]
    # mapa = [[0, 0, 2, 'ouro'],
    #       [0, 2, '@', 2],
    #       [0, 1, 4, 2],
    #       [1, '#', '@', '@']]

    mapaJogador = [[None, None, None, None],
                   [None, None, None, None],
                   [None, None, None, None],
                   [None, None, None, None]]

    mapa_aux = mapa

    mapa = definePocoWumpus(mapa)  # ao fim mapa está pronto
    mapa = defineOuro(mapa)
    caminho, mapa, sucesso = caminhaNoMapa(mapa, mapaJogador)
    gui = Gui()
    if(sucesso is True):
        gui.carrega_gui(caminho, mapa)
    else:
        print "GAME OVER, Execute novamente"
