class Arco:
    def __init__(self, destino, peso):
        self.destino = destino
        self.peso = peso


class No:
    def __init__(self, nome_no):
        self.nome_no = nome_no
        # Em Python, uma lista nativa substitui o LinkedList do Java
        self.adjacencias = []


class Grafo:
    def __init__(self, tamanho):
        self.max_nos = tamanho
        # Cria uma lista de "Nós" inicializados com string vazia
        self.nos = [No("") for _ in range(self.max_nos)]

    def buscar_no(self, nome):
        for no in self.nos:
            if no is not None and no.nome_no == nome:
                return no
        return None

    def seta_informacao(self, nome_antigo, nome_novo):
        n = self.buscar_no(nome_antigo)
        # Adicionado verificação 'n is not None' para evitar erros caso o nó não exista
        if n is not None and n.nome_no != "":
            n.nome_no = nome_novo
        else:
            # Achar primeiro lugar que esteja vazio
            for no in self.nos:
                if no.nome_no == "":
                    no.nome_no = nome_novo
                    break

    def cria_adjacencia(self, origem, destino, peso):
        no_origem = self.buscar_no(origem)
        no_destino = self.buscar_no(destino)

        if no_origem is not None and no_destino is not None:
            no_origem.adjacencias.append(Arco(no_destino, peso))

    def remove_adjacencia(self, origem, destino):
        no_origem = self.buscar_no(origem)
        no_destino = self.buscar_no(destino)

        if no_origem is not None and no_destino is not None:
            for i in range(len(no_origem.adjacencias)):
                if no_origem.adjacencias[i].destino == no_destino:
                    no_origem.adjacencias.pop(i)  # pop remove o item pelo índice
                    break

    def adjacentes(self, nome, adj):
        n = self.buscar_no(nome)
        if n is not None:
            for i in range(len(n.adjacencias)):
                adj[i] = n.adjacencias[i].destino.nome_no
            return len(n.adjacencias)
        return 0

    def imprime_adjacencias(self):
        for no in self.nos:
            print(f"{no.nome_no} aponta para: ", end="")
            for arco in no.adjacencias:
                print(f"{arco.destino.nome_no}({arco.peso})  ", end="")
            print()  # Quebra de linha


# Bloco principal de execução (equivalente ao public static void main)
if __name__ == "__main__":
    meu_grafo = Grafo(4)

    meu_grafo.seta_informacao("", "A")
    meu_grafo.seta_informacao("", "B")
    meu_grafo.seta_informacao("", "C")
    meu_grafo.seta_informacao("", "D")

    meu_grafo.cria_adjacencia("A", "B", 10)
    meu_grafo.cria_adjacencia("A", "C", 25)
    meu_grafo.cria_adjacencia("B", "D", 40)
    meu_grafo.cria_adjacencia("C", "D", 15)

    print("--- GRAFO INICIAL ---")
    meu_grafo.imprime_adjacencias()

    print("\n--- TESTANDO VIZINHOS DO NÓ 'A' ---")
    # Criamos uma lista de tamanho 4 preenchida com strings vazias para simular o vetor de strings do Java
    vetor_vizinhos = [""] * 4
    quantidade = meu_grafo.adjacentes("A", vetor_vizinhos)

    print(f"O nó 'A' tem {quantidade} vizinhos.")
    for i in range(quantidade):
        print(f"Vizinho {i + 1}: {vetor_vizinhos[i]}")

    print("\n--- REMOVENDO LIGAÇÃO A -> B ---")
    meu_grafo.remove_adjacencia("A", "B")
    meu_grafo.imprime_adjacencias()