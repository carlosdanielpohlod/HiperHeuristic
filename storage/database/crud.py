from storage.database.estrutura_database import Resultados,db,ScoreHeuristica,Execucao,HeuristicaUsada
import peewee
db = peewee.SqliteDatabase('conhecimento.db')




def salvarResultado(codReproducao, codBuscaLocal, codSelecaoPais, fitness):

    resultados = Resultados(codReproducao =  codReproducao,codBuscaLocal=  codBuscaLocal, codSelecaoPais=  codSelecaoPais, fitness= fitness)
    resultados.save()
    db.close()
    print("Melhor resultado salvo")
   
def salvarHiperHeuristica(idExecucao, tipoHeuristica, codHeuristica ):
    h = HeuristicaUsada()
    id = db.execute_sql("select heuristicaUsada_id from heuristicausada limit(1)")
#   ARRUMAR AQUI
    for v in id:     
        if(v != None):
            HeuristicaUsada.insert(tipoHeuristica_id = tipoHeuristica, execucao_id = idExecucao, codHeuristica = codHeuristica).execute()
            
    return id   
    
    db.close()
def salvarScore(heuristicaUsada_id, codHeuristica, score):
    novaHeuristica = ScoreHeuristica(heuristica_id = heuristicaUsada_id, codHeuristica = codHeuristica, score = score)
    novaHeuristica.save()
    db.close()
def novaExecucao():
    idExecucao = Execucao.insert().execute()
    # print("criado", idExecucao)
    db.close()
    
    return idExecucao
def melhorHeuristica():
    
    try:
        db.connect()
        resultados = Resultados()
        resultados = resultados.select().order_by("fitness").limit(1).execute()
        
        for resultado in resultados:
            return [resultado.codReproducao, resultado.codBuscaLocal, resultado.codSelecaoPais, resultado.fitness]
        
        db.close()
    except peewee.OperationalError:
        print("erro", peewee.OperationalError)
    class Meta:
        database = db