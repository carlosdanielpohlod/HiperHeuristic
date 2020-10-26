from utils import Utils
fluxo = [   [0,1,2,3,1,2,3,4,2,3,4,5],
            [1,0,1,2,2,1,2,3,3,2,3,4],
            [2,1,0,1,3,2,1,2,4,3,2,3],
            [3,2,1,0,4,3,2,1,5,4,3,2],
            [1,2,3,4,0,1,2,3,1,2,3,4],
            [2,1,2,3,1,0,1,2,2,1,2,3],
            [3,2,1,2,2,1,0,1,3,2,1,2],
            [4,3,2,1,3,2,1,0,4,3,2,1],
            [2,3,4,5,1,2,3,4,0,1,2,3],
            [3,2,3,4,2,1,2,3,1,0,1,2],
            [4,3,2,3,3,2,1,2,2,1,0,1],
            [5,4,3,2,4,3,2,1,3,2,1,0]
        ]
distancias = [
            [0,5,2,4,1,0,0,6,2,1,1,1],
            [5,0,3,0,2,2,2,0,4,5,0,0],
            [2,3,0,0,0,0,0,5,5,2,2,2],
            [4,0,0,0,5,2,2,10,0,0,5,5],
            [1,2,0,5,0,10,0,0,0,5,1,1],
            [0,2,0,2,10,0,5,1,1,5,4,0],
            [0,2,0,2,0,5,0,10,5,2,3,3],
            [6,0,5,10,0,1,10,0,0,0,5,0],
            [2,4,5,0,0,1,5,0,0,0,10,10],
            [1,5,2,0,5,5,2,0,0,0,5,0],
            [1,0,2,5,1,4,3,5,10,5,0,2],
            [1,0,2,5,1,0,3,0,10,0,2,0]
        ]

def construirHeuristica(reproducao, buscaLocal, funcaoObjetivo, selecaoPais, fluxo, distancias, parametros, codHeuristicas):
    utils = Utils(parametros)
    numeroGeracoes = 15
    populacao = utils.declararMatriz(linhas = parametros.TAMPOPULACAO, colunas = parametros.TAMCROMOSSOMO)
    funcaoObjetivo.gerarPopulacao(populacao)
    funcaoObjetivo.avaliarPopulacao(populacao, fluxo, distancias)
    # print(populacao)
    for i in range(numeroGeracoes):    
        pai01, pai02 = selecaoPais.selecionar(populacao, codHeuristicas.codSelecaoPais)  
        # print(populacao[pai01], populacao[pai02])
        reproducao.reproduzir(populacao, fluxo, distancias, pai01, pai02, codHeuristicas.codReproducao)
        melhor = utils.buscarMelhorIndividuo(populacao)
        # print(populacao[melhor])
        buscaLocal.busca(populacao[melhor], fluxo, distancias, codHeuristicas.codBuscaLocal)
        # print(populacao[melhor])
    return populacao[melhor][parametros.TAMCROMOSSOMO - 1]