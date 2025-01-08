def bron_kerbosch(matriz_adjacencia):
  """
  Implementa o algoritmo de Bron-Kerbosch para encontrar todos os cliques maximais
  em um grafo representado por uma matriz de adjacência.

  Argumentos:
    matriz_adjacencia: Uma lista de listas representando a matriz de adjacência do grafo.

  Retorna:
    Uma lista de conjuntos, onde cada conjunto representa um clique maximal.
  """

  def bk(r, p, x):
    """
    Função recursiva para o algoritmo de Bron-Kerbosch.

    Argumentos:
      r: O clique atual sendo construído (conjunto).
      p: O conjunto de vértices candidatos (conjunto).
      x: O conjunto de vértices excluídos (conjunto).
    """
    if not p and not x:
      cliques_maximais.append(r)
      return

    for u in list(p):
      p.remove(u)
      r_novo = r | {u}
      p_novo = set()
      x_novo = set()
      for v in range(len(matriz_adjacencia)):
        if matriz_adjacencia[u][v]:
          if v in p:
            p_novo.add(v)
          if v in x:
            x_novo.add(v)

      bk(r_novo, p_novo, x_novo)
      x.add(u)

  n = len(matriz_adjacencia)
  cliques_maximais = []
  todos_vertices = set(range(n))  # Vértices são representados por índices 0, 1, ..., n-1
  bk(set(), todos_vertices, set())
  return cliques_maximais

def main():
    # Exemplo:
    matriz_adjacencia = [
        [0, 1, 1, 0, 1],  # V1 (0)
        [1, 0, 1, 1, 1],  # V2 (1)
        [1, 1, 0, 1, 1],  # V3 (2)
        [0, 1, 1, 0, 1],  # V4 (3)
        [1, 1, 1, 1, 0],  # V5 (4)
    ]

    cliques = bron_kerbosch(matriz_adjacencia)
    print("Cliques maximais:")
    for clique in cliques:
        clique_indices = {f"V{v}" for v in clique}
    print(clique_indices)

if __name__ == "__main__":
    main()
