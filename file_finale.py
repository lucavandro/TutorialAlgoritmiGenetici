oggetti = [
  {
    "nome": "Computer",
    "volume": 3,
    "peso": 2.2
  },
  {
    "nome": "Scarpe",
    "volume": 7,
    "peso": 0.5
  },
  {
    "nome": "Libro",
    "volume": 2,
    "peso": 0.33
  },
  {
    "nome": "Acqua",
    "volume": 1,
    "peso": 1
  },
  {
    "nome": "Tablet",
    "volume": 1.2,
    "peso": 0.7
  },
  {
    "nome": "Felpa",
    "volume": 7,
    "peso": 0.2
  },
  {
    "nome": "Cuffie",
    "volume": 2,
    "peso": 0.2
  },
  {
    "nome": "Cubo di rubik",
    "volume": 0.2,
    "peso": 0.13
  },
]
"""
Encoding: Array di booleani es. [True, False, True, True]
True: oggetto scelto
False: oggetto non scelto
"""
def inizializza(dimensione):
  from random import choices
  popolazione = []
  for i in range(dimensione):
    membro = {
      'genoma': choices([True, False], k=len(oggetti)),
      'voto': 0
    }
    popolazione.append(membro)
  return popolazione
  
def fitness(popolazione):
  from itertools import compress
  for membro in popolazione:
    oggetti_scelti = list(compress(oggetti, membro['genoma']))
    somma_pesi = 0
    somma_volumi = 0
    for oggetto in oggetti_scelti:
      somma_pesi += oggetto["peso"] 
      somma_volumi += oggetto["volume"] 

    if somma_pesi <= 3 and somma_volumi <= 18:
      membro['voto']=len(oggetti_scelti)* ( somma_volumi + somma_pesi)

  return popolazione
  
def selezione(popolazione):
  from operator import itemgetter
  popolazione_ordinata = sorted(popolazione, key=itemgetter('voto'), reverse=True)
  return popolazione_ordinata[:4]

def crossover(popolazione):
  from itertools import combinations
  nuova_generazione = []
  for papa, mamma in combinations(popolazione, 2):
    centro = len(oggetti) // 2
    figlio1 = {
      'genoma': papa['genoma'][:centro] + mamma['genoma'][centro:],
      'voto': 0
    }
    figlio2 = {
      'genoma': mamma['genoma'][:centro] + papa['genoma'][centro:],
      'voto': 0
    }
    nuova_generazione.append(figlio1)
    nuova_generazione.append(figlio2)
  return nuova_generazione

def mutazione(popolazione):
  from random import randrange
  for membro in popolazione:
    gene_casuale = randrange(len(oggetti))
    membro['genoma'][gene_casuale] = not membro['genoma'][gene_casuale]
  return popolazione

def evoluzione():
  popolazione = inizializza(4)
  migliore = popolazione[0]
  for i in range(100):
    popolazione = fitness(popolazione)
    popolazione = selezione(popolazione)
    if popolazione[0]['voto'] > migliore['voto']:
      migliore = popolazione[0]
    popolazione = crossover(popolazione)
    popolazione = mutazione(popolazione)
    print(f"Generazione {i:2d} - Voto migliore {migliore['voto']:.2f}")


evoluzione()