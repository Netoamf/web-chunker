# Segmentação Morfológica com Algoritmos BPE e MDL

## (PB)
## Descrição

Esse repositório contém a implementação da versão web dos chunkers elaborado durante o PIBIC 2023-24. Implementaremos em uma página web uma maneira de segmentar morfológicamente palavras de línguas sub-representadas de maneira gratuita.

## Algoritmos Implementados

O repositório apresenta a implementação de dois algoritmos distintos para a segmentação morfológica:

1. **Byte Pair Encoding (BPE):** Um algoritmo de compressão de dados que é frequentemente utilizado para segmentação de subpalavras. Neste projeto, o BPE é adaptado para identificar morfemas em textos.

2. **Minimum Description Length (MDL):** Um algoritmo, também de compressão de dados, que busca encontrar a descrição mais compacta para os dados. Neste contexto, o MDL é utilizado para determinar a segmentação morfológica que minimiza o comprimento da representação do léxico e do corpus.

## Conteúdo do Repositório

- **Código-fonte:** Implementações em Python dos algoritmos BPE e MDL para segmentação morfológica.
- **Gramáticas Descritivas:** Arquivos contendo as gramáticas descritivas utilizadas para testar e avaliar os algoritmos.
- **Documentação:** Este arquivo README.md e outros nos diretórios referentes aos algoritmos. Os arquivos README.md dos algoritmos foram escritos em PB e EN para facilitar o acesso a todos que desejarem usar o programa.

## Autoria

- **Autores:** Antonio Morais de Freitas Neto e Fernando Yamaguchi

## Referências Bibliográficas

**MDL:**

- DE MARCKEN, C. (1995). The unsupervised acquisition of a lexicon from continuous speech. arXiv preprint cmplg/9512002.
- RISSANEN, J. (1978). "Modeling by shortest data description". Automatica. 14 (5): 465–471.

**BPE:**

-  FEB94 A New Algorithm for Data Compression. Disponível em: <http://www.pennelynn.com/Documents/CUJ/HTML/94HTML/19940045.HTM>.
- SENNRICH, R.; HADDOW, B.; BIRCH, A. Neural Machine Translation of Rare Words with Subword Units. 31 ago. 2015. https://arxiv.org/abs/1508.07909v5




## (EN)
## Description

This repository contains the implementation of the web version of chunkers developed during PIBIC 2023-24. We will implement on a web page a way to morphologically segment words from underrepresented languages ​​for free.

## Implemented Algorithms

This repository features the implementation of two distinct algorithms for morphological segmentation:

1. **Byte Pair Encoding (BPE):** A data compression algorithm commonly employed for subword segmentation. In this project, BPE is adapted to identify morphemes within texts. 

2. **Minimum Description Length (MDL):** A data compression algorithm that strives to find the most concise description for the data. In this context, MDL is used to determine the morphological segmentation that minimizes the length of representation for both the lexicon and the corpus.

## Repository Contents

- **Source Code:** Python implementations of the BPE and MDL algorithms for morphological segmentation.
- **Descriptive Grammars:** Files containing the descriptive grammars utilized to test and evaluate the algorithms.
- **Documentation:** This README.md file and others within the directories of each algorithm. The README.md files for the algorithms were written in both Portuguese (PT-BR) and English (EN) to facilitate access for all those who wish to use the program.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Netoamf/web-chunker.git
    ````

2. Install the requirements (we advise to create a virtual environment)
   ```python
   python -r requirements.txt
    ```

## Authorship

- **Authors:** Antonio Morais de Freitas Neto and Fernando Yamaguchi

## Bibliographic References

**MDL:**

- DE MARCKEN, C. (1995). The unsupervised acquisition of a lexicon from continuous speech. arXiv preprint cmplg/9512002.
- RISSANEN, J. (1978). "Modeling by shortest data description". Automatica. 14 (5): 465–471.

**BPE:**

- FEB94 A New Algorithm for Data Compression. Available at: <http://www.pennelynn.com/Documents/CUJ/HTML/94HTML/19940045.HTM>.
- SENNRICH, R.; HADDOW, B.; BIRCH, A. Neural Machine Translation of Rare Words with Subword Units. Aug. 31, 2015. https://arxiv.org/abs/1508.07909v5 
