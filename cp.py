def max_clique_cp(matriz_adjacencia):
  """
  Implementa o algoritmo de Carraghan & Pardalos para encontrar o clique máximo
  em um grafo representado por uma matriz de adjacência.

  Argumentos:
    matriz_adjacencia: Uma lista de listas representando a matriz de adjacência do grafo.

  Retorna:
    Um conjunto representando o clique máximo encontrado.
  """

  def clique(c, p):
    nonlocal c_max  # Permite modificar a variável c_max no escopo externo

    if len(c) > len(c_max):
      c_max = c

    if len(c) + len(p) > len(c_max):
      for u in list(p):  # Itera sobre uma cópia para permitir a modificação
        p.remove(u)
        c_novo = c | {u}
        p_novo = set()
        for v in range(len(matriz_adjacencia)):
          if matriz_adjacencia[u][v] and v in p:
            p_novo.add(v)
        clique(c_novo, p_novo)

  n = len(matriz_adjacencia)
  c_max = set()  # Inicializa o clique máximo como um conjunto vazio
  todos_vertices = set(range(n))
  clique(set(), todos_vertices)
  return c_max

def main():
    # Exemplo:
    matriz_adjacencia = [
        [0, 1, 1, 0, 0],  # V0
        [1, 0, 1, 0, 0],  # V1
        [1, 1, 0, 1, 0],  # V2
        [0, 0, 1, 0, 0],  # V3
        [0, 0, 0, 0, 0],  # V4
    ]

    clique_maximo = max_clique_cp(matriz_adjacencia)
    clique_maximo_indices = {f"V{v}" for v in clique_maximo}
    print("Clique máximo:", clique_maximo_indices)

if __name__ == "__main__":
  main()