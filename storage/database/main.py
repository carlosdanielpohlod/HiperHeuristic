from funcoesEstatisticas_file import *
from grafico_file import *

grafico = Grafico()
funcoes = FuncoesEstatisticas()
def bestXmediaPop(id):
    best, pop = funcoes.mediaPopulacaoEFitnessPorExecucao(id)
    grafico.evolucaoPopulacaoXBest(best, pop, i)
def areaSimples(id):
    grafico.graficoSimples(funcoes.codesPorExecucao(id))

for i in range(3, 3+ 10):  
    bestXmediaPop(i)

