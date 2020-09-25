from random import randint
from utils import *

class funcaoObjetivo:
    def __init__(self, parametros):
        self.parametros = parametros
        self.utils = Utils(parametros)
    def setParametros(self, parametros):
        self.parametros = parametros
      
    def gerarPopulacao(self, populacao):
        N = len(populacao[0]) + 1

        novoIndividuo = [0] * N  
        existe = False
        num = 0
        individuo = 0  
        locus = 0

        for individuo in range(self.parametros.TAMPOPULACAO):
            self.utils.zerar(novoIndividuo)
            # novoIndividuo =  [self.parametros.TAMCROMOSSOMO + 3] *len(novoIndividuo) *
            while(locus < N):
                

                num = randint(0,N)
                existe = False

                for i in range(self.parametros.TAMCROMOSSOMO - 1):
                    
                    if(novoIndividuo[i] == num):
                        
                        existe = True
                        break
                    
                    
                
                if(existe == False):              
                    novoIndividuo[locus] = num   
                    locus = locus + 1  
            
            locus = 0
            print(self.parametros.TAMCROMOSSOMO, self.parametros.TAMPOPULACAO, len(populacao[0]))
            for j in range(self.parametros.TAMCROMOSSOMO - 1):
                populacao[individuo][j] = novoIndividuo[j]
            
            populacao[individuo][self.parametros.TAMCROMOSSOMO - 1] = 0
        
    def avaliarIndividuo(self,individuo, fluxo, distancias):
    
        fitness = 0
        N = len(individuo) - 1
        for i in range(N):
            for j in range(N):
                    fitness = distancias[i][j] * fluxo[ individuo[i] ] [individuo[j] ]
        individuo[self.parametros.TAMINDIVIDUO - 1] = fitness
    
    def avaliarPopulacao(self, populacao, fluxo, distancias):
        for individuo in range(self.parametro):
            avaliarIndividuo(populacao[individuo], fluxo, distancias)
    