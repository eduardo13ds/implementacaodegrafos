# Implementação de Grafo em Python

Este projeto contém uma implementação em Python de um grafo direcionado com pesos, utilizando a estrutura de listas de adjacência. O código foi adaptado a partir de uma estrutura originalmente desenvolvida na linguagem Java.

---

## Estrutura das Classes

O funcionamento do grafo é modelado através de três classes principais:

* **Arco**: Representa a aresta (ligação) do grafo. Armazena a referência para o nó de destino e o peso associado à ligação.

* **No (Nó)**: Representa um vértice. Contém um identificador em formato de texto (nome) e uma lista responsável por armazenar todos os arcos que partem deste nó.

* **Grafo**: A estrutura central que gere os vértices. É inicializada com um tamanho máximo predefinido e fornece a interface para a manipulação dos dados.

---

## Funcionalidades Disponíveis

A classe `Grafo` oferece os seguintes métodos principais para manipulação:

* **buscar_no(nome)**: Procura e devolve a referência de um nó específico com base no seu nome.

* **seta_informacao(nome_antigo, nome_novo)**: Renomeia um nó existente. Caso o nó antigo não seja encontrado, atribui o novo nome à primeira posição vazia disponível no grafo.

* **cria_adjacencia(origem, destino, peso)**: Estabelece uma nova aresta direcionada de um nó de origem para um nó de destino, registando o peso da ligação.

* **remove_adjacencia(origem, destino)**: Elimina a ligação direta existente entre o nó de origem e o nó de destino.

* **adjacentes(nome, adj)**: Identifica os nós vizinhos de um vértice específico, preenche uma lista fornecida com os nomes desses vizinhos e devolve a quantidade total encontrada.

* **imprime_adjacencias()**: Imprime na consola a configuração atual do grafo, listando cada nó, os seus respetivos destinos e os pesos dos arcos.

---

## Como Executar

O código utiliza apenas recursos nativos do Python, dispensando a instalação de bibliotecas externas ou gestores de pacotes.

1. Guardar o código num ficheiro local, nomeando-o como `grafo.py`, por exemplo.
2. Abrir o terminal de comando ou a linha de comandos do sistema operativo.
3. Navegar até ao diretório onde o ficheiro foi guardado e executar o seguinte comando:

```bash
python grafo.py
```

---

## Saída Esperada

A execução do ficheiro acionará a rotina principal, que cria um grafo de 4 nós (`A`, `B`, `C` e `D`), estabelece ligações entre eles, imprime o estado inicial, lista os vizinhos do nó **"A"** e demonstra o comportamento de remoção de uma aresta.

O resultado na consola deverá ser semelhante a este:

```
--- GRAFO INICIAL ---

A aponta para: B(10)  C(25)

B aponta para: D(40)

C aponta para: D(15)

D aponta para:


--- TESTANDO VIZINHOS DO NÓ 'A' ---

O nó 'A' tem 2 vizinhos.

Vizinho 1: B
Vizinho 2: C


--- REMOVENDO LIGAÇÃO A -> B ---

A aponta para: C(25)

B aponta para: D(40)

C aponta para: D(15)

D aponta para:
```
