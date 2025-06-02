
---
# Identificador de Gramática (com classificação segundo a Hierarquia de Chomsky)

Este projeto em Python tem como objetivo **validar e classificar gramáticas formais** a partir de regras fornecidas em um arquivo de texto. A classificação é feita segundo a hierarquia de Chomsky, identificando o tipo da gramática (Tipo 0, 1, 2 ou 3).

O programa verifica se as regras da gramática estão conformes com a estrutura formal, extrai os símbolos terminais e não terminais, e apresenta a gramática no formato padrão:

> G = (N, T, P, S)  
> onde N = conjunto de não terminais,  
> T = conjunto de terminais,  
> P = conjunto de regras de produção,  
> S = símbolo inicial (raiz).

---

## 📚 Sobre o Projeto

O programa realiza as seguintes etapas:

- Lê regras gramaticais do arquivo `gramatica.txt`.
- Valida os símbolos utilizados nas regras.
- Classifica a gramática conforme a hierarquia de Chomsky:
  - **Tipo 0**: Gramática Irrestrita  
  - **Tipo 1**: Gramática Sensível ao Contexto  
  - **Tipo 2**: Gramática Livre de Contexto  
  - **Tipo 3**: Gramática Regular (direita, esquerda ou terminal)
- Exibe:
  - Os símbolos terminais e não terminais usados.
  - As regras de produção formatadas.
  - A raiz da gramática.

---

## 🧠 Como Funciona

### Formato de entrada

As regras devem ser escritas no arquivo `gramatica.txt` seguindo este formato:

- Cada regra deve conter pelo menos um **não terminal** no lado esquerdo.
- O lado esquerdo e direito da regra são separados pelo símbolo `>`.
- Diferentes regras são separadas pelo caractere `-`.
- O arquivo deve terminar com o símbolo `$`, que indica o fim da gramática.
- O símbolo `$` também pode representar a cadeia vazia e será convertido para `ε` automaticamente quando aparecer no final da entrada.

### Símbolos permitidos
- Não terminais -> (`A-Z`)
- Terminais -> (`a-z` e `ε`)

### Exemplo de gramática válida
Ao executar o arquivo um exemplo de gramatica é gerado juntamente com a criação do arquivo `gramatica.txt`. O exemplo segue abaixo:
`S > aS - S>aaa - S>$`


