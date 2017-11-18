# -*- coding: utf-8 -*-

"""
 Example program to show using an array to back a grid on-screen.
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/mdTeqiWyFnc
"""
import pygame
from playsound import playsound
 

class Gui():

    def __init__(self):
         
       
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)
        self.GRAY = (224,224,224)
        self.BLUE = (0,191,255)
        self.GOLD = (255,215,0)

        self.reservado =["ouro","#","@"]
        self.nivel_sayajin = 0
        self.posicoes=[]
        #posicoes de evolução proximas do wumpus.
        self.evolucoes =[]

        # This sets the WIDTH and HEIGHT of each grid location
        self.WIDTH = 95
        self.HEIGHT = 118

        # This sets the margin between each cell
        self.MARGIN = 5

        # Create a 2 dimensional array. A two dimensional
        # array is simply a list of lists.
        self.grid = []
        for row in range(4):
            # Add an empty array that will hold each cell
            # in this row
            self.grid.append([])
            for column in range(4):
                self.grid[row].append(0)  # Append a cell

        # Initialize pygame
        pygame.init()

        #Iniatializa font
        pygame.init()

        # Set the WIDTH and HEIGHT of the screen
        WINDOW_SIZE = [400, 500]
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
         
        # Set title of screen
        pygame.display.set_caption("Mundo do Wumpus")
         
        # Loop until the user clicks the close button.
        self.done = False
         
        # Used to manage how fast the screen updates
        self.clock = pygame.time.Clock()

    def backlog(self):
        print "-----------"
        print "Pontuação: -",len(self.posicoes)
        print "Caminho",self.posicoes
        print "-----------"

    def win(self):
        self.screen.fill(self.BLACK)
        perso = self.carrega_imagem("shenron")
        self.screen.blit(perso,(0,50))
        pygame.display.flip()
        pygame.time.delay(100)


    def carrega_gui(self,caminho,mapa):
        print "-----------------------"
        self.posicoes = caminho
        for i in range(0,len(mapa)):
            for j in range(0,len(mapa)):
                if mapa[i][j] == "@":
                    self.grid[i][j]= "@"
                elif mapa[i][j] == "#":
                    self.grid[i][j]= "#"
                elif mapa[i][j] == "ouro":
                    self.grid[i][j] ="ouro"
                elif mapa[i][j] == 1 or mapa[i][j] == 3:
                    self.evolucoes.append([i,j])
        self.main()

    
    def carrega_imagem(self,personagem):
         personagem=pygame.image.load("imagens/"+personagem+".png")
         return personagem


    def marca_evolucao(self,posicao,mapa):
        """marca as posições para evolução"""
        for i in posicao:
            mapa[i[0]][i[1]] = 2

        return mapa

    def evolucao(self,tela,personagem,column,row):
        """Carrega imagem da evolução"""

        tela.blit(personagem,[(self.MARGIN + self.WIDTH) * column + self.MARGIN,
                          (self.MARGIN + self.HEIGHT) * row + self.MARGIN,
                          self.WIDTH,
                          self.HEIGHT])

        pygame.display.flip()
        playsound("audio/evolucao.mp3")
        playsound("audio/wumpus.mp3")
        if self.nivel_sayajin is 0:
            perso=self.carrega_imagem("new_person")
            self.nivel_sayajin+=1
        else:
            perso=self.carrega_imagem("personagem")
        return tela,perso

    def preenche_quadrado(self,personagem,cor,linha,coluna):
        """Preenche uma posicao especifica da matriz"""
        self.desenha_quadrado(cor, linha, coluna)
        self.carrega_personagem(personagem,linha,coluna)

    def carrega_personagem(self,personagem,row,column):
        """Carrega um elemento"""
        personagem = self.carrega_imagem(personagem)
        self.screen.blit(personagem,[(self.MARGIN + self.WIDTH) * column + self.MARGIN,
                          (self.MARGIN + self.HEIGHT) * row + self.MARGIN,
                          self.WIDTH,
                          self.HEIGHT])

        pygame.display.flip()

    def desenha_quadrado(self, cor, linha, coluna):
        """Desenha um quadrado"""
        pygame.draw.rect(self.screen,
                                     cor,
                                     [(self.MARGIN + self.WIDTH) * coluna + self.MARGIN,
                                      (self.MARGIN + self.HEIGHT) * linha + self.MARGIN,
                                      self.WIDTH,
                                      self.HEIGHT])

    def main(self):
        """Função principal"""
        self.grid= self.marca_evolucao(self.evolucoes,self.grid)
        cont_pos_max = len(self.posicoes)
        cont_pos_min = 0
        personagem = self.carrega_imagem("perso")
        # -------- Main Program Loop -----------
        while not self.done:
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    self.done = True  # Flag that we are done so we exit this loop
         
            # Set the screen background
            self.screen.fill(self.BLACK)
            # Draw the grid
            #Desenha o mapa
            for linha in range(4):
                for coluna in range(4):
                    cor = self.GRAY
                    if self.grid[linha][coluna] == "#":
                        #cor = self.RED
                        self.preenche_quadrado("wumpus", cor, linha, coluna)
                        # self.desenha_quadrado(color, linha, coluna)
                        # self.carrega_personagem("wumpus",linha,coluna)
                    if self.grid[linha][coluna] == "ouro":
                        #cor = self.GOLD
                        self.preenche_quadrado("esferas", cor, linha, coluna)
                        # self.desenha_quadrado(color, linha, coluna)
                        # self.carrega_personagem("esferas", linha, coluna)
                    elif self.grid[linha][coluna] == "@":
                        self.preenche_quadrado("lake", cor, linha, coluna)
                    if self.grid[linha][coluna] not in self.reservado:
                        self.desenha_quadrado(cor,linha,coluna)

            #pygame.time.wait(30)
            # Limit to 60 frames per second
            self.clock.tick(60)
            #Atualiza a exibição da tela
            pygame.display.flip()

            # Atualiza os deslocamentos
          
            for pos in self.posicoes:
                
                row=pos[0]
                column= pos[1]

               
                if(self.grid[row][column] == 2):
                    personagem= self.carrega_imagem("guerreiro_evoluindo")
                    self.screen,personagem = self.evolucao(self.screen, personagem,column, row)

                self.screen.blit(personagem,[(self.MARGIN + self.WIDTH) * column + self.MARGIN,
                                  (self.MARGIN + self.HEIGHT) * row + self.MARGIN,
                                  self.WIDTH,
                                  self.HEIGHT])
                #pygame.time.wait(1000)
                pygame.display.flip()
                color= self.GRAY
                pygame.draw.rect(self.screen,
                             color,
                             [(self.MARGIN + self.WIDTH) * column + self.MARGIN,
                              (self.MARGIN + self.HEIGHT) * row + self.MARGIN,
                              self.WIDTH,
                              self.HEIGHT])
                if(self.grid[row][column] == 'ouro'):
                    self.backlog()
                    self.win()
                    pygame.quit()
                    return 1
                pygame.time.delay(500)
                self.clock.tick(60)
                pygame.display.flip()

            # Be IDLE friendly. If you forget this line, the program will 'hang'
            # on exit.
            pygame.quit()
