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
         
        print "GUIII"
       # print "Caminho",caminho
        #print "Mapa",mapa
        # Define some colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)
        self.YELLOWGREEN = (154,205,50)
        self.BLUE = (0,191,255)
        self.GOLD = (255,215,0)


        # #caminho do guerreiro
        # self.posicoes=[[0,0],[0,1],[1,1],[2,1],[2,2],[2,3],[3,3]]
        # self.evolucoes=[[2,3]]

        self.reservado =["ouro","#"]
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
         
        # # Set row 1, cell 5 to one. (Remember rows and
        # # column numbers start at zero.)
        # grid[0][0] = 1
         
        # Initialize pygame
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
                elif mapa[i][j] == 1:
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

    def carrega_personagem(self,personagem,row,column):
        """Carrega o wumpus"""
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
            for row in range(4):
                for column in range(4):
                    color = self.YELLOWGREEN
                    if self.grid[row][column] == "#":
                        color = self.RED
                        self.desenha_quadrado(color, row, column)
                        self.carrega_personagem("wumpus",row,column)
                    if self.grid[row][column] == "ouro":
                        color = self.GOLD
                        self.desenha_quadrado(color, row, column)
                        self.carrega_personagem("esferas", row, column)
                    elif self.grid[row][column] == "@":
                        color = self.BLUE
                    if self.grid[row][column] not in self.reservado:
                        self.desenha_quadrado(color,row,column)

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
                color= self.YELLOWGREEN
                pygame.draw.rect(self.screen,
                             color,
                             [(self.MARGIN + self.WIDTH) * column + self.MARGIN,
                              (self.MARGIN + self.HEIGHT) * row + self.MARGIN,
                              self.WIDTH,
                              self.HEIGHT])
                pygame.time.delay(2000)
                pygame.display.flip()

            # Be IDLE friendly. If you forget this line, the program will 'hang'
            # on exit.
            pygame.quit()

#if __name__ == '__main__':
    # gui = Gui()
    # gui.main()
