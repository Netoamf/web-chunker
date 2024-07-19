# Segmentação Morfológica com Algoritmos BPE e MDL

## Descrição

Este repositório contém os resultados do projeto de pesquisa desenvolvido por mim, Antonio Morais de Freitas Neto, sob orientação do Prof. João Paulo Lazzarini Cyrino no âmbito do PIBIC e do Trabalho de Conclusão de Curso (TCC) na Universidade Federal da Bahia. O projeto visa explorar e comparar diferentes abordagens para a segmentação morfológica.

## Algoritmos Implementados

O repositório apresenta a implementação de dois algoritmos distintos para a segmentação morfológica:

1. **Byte Pair Encoding (BPE):** Um algoritmo de compressão de dados que é frequentemente utilizado para segmentação de subpalavras. Neste projeto, o BPE é adaptado para identificar morfemas em textos.

2. **Minimum Description Length (MDL):** Um algoritmo, também de compressão de dados, que busca encontrar a descrição mais compacta para os dados. Neste contexto, o MDL é utilizado para determinar a segmentação morfológica que minimiza o comprimento da representação do léxico e do corpus.

## Conteúdo do Repositório

- **Código-fonte:** Implementações em Python dos algoritmos BPE e MDL para segmentação morfológica.
- **Gramáticas Descritivas:** Arquivos contendo as gramáticas descritivas utilizadas para testar e avaliar os algoritmos.
- **Documentação:** Este arquivo README.md e outros nos branchs referentes aos algoritmos. Os arquivos README.md dos algoritmos foram escritos em PB e EN para facilitar o acesso a todos que desejarem usar o programa.

## Referências Bibliográficas

**MDL:**

- DE MARCKEN, C. (1995). The unsupervised acquisition of a lexicon from continuous speech. arXiv preprint cmplg/9512002.
- RISSANEN, J. (1978). "Modeling by shortest data description". Automatica. 14 (5): 465–471.

**BPE:**

-  FEB94 A New Algorithm for Data Compression. Disponível em: <http://www.pennelynn.com/Documents/CUJ/HTML/94HTML/19940045.HTM>.
- SENNRICH, R.; HADDOW, B.; BIRCH, A. Neural Machine Translation of Rare Words with Subword Units. 31 ago. 2015. https://arxiv.org/abs/1508.07909v5
