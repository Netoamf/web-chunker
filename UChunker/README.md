# UChunker

## (EN)
## Authorship and Affiliation

- **Authors:** Antonio Morais de Freitas Neto and Prof. João Paulo Lazzarini Cyrino
- **Affiliation:** Universidade Federal da Bahia

## Description

This project implements a Minimum Description Length (MDL) algorithm for morphological segmentation based on the algorithm proposed by Carl De Marcken. The goal is to segment a corpus into morphemes efficiently by minimizing the combined cost of encoding the lexicon and the corpus itself.

## Modules

The project is divided into several modules for better organization and maintainability:

1. **`process_descriptive_grammar.py`**: Contains the `ProcessDescriptiveGrammar` class which is responsible for extracting words and morphemes from a descriptive grammar file.
2. **`uchunker.py`**: Contains the `UChunker` class which handles the chunking and segmentation process using the MDL principle.
3. **`comparison.py`**: Provides functions to compare morphemes and segmentations against a lexicon and write the results to output files.
4. **`menu.py`**: Implements a menu-driven interface for users to interact with the different functionalities of the project.
5. **`main.py`**: The entry point of the application that runs the menu interface.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Netoamf/PIBIC-2023-24/tree/main/UChunker.git
   ```

## Usage

1. Run the main script:
    ```bash
    python main.py
    ```

** Follow the menu prompts to: 
- Process descriptive grammar.
- Start the chunker.
- Compare Morphemes.
- Compare Segmentations.

## Step-by-Step Instructions

1. Select **option 1** from the menu.
2. Enter the name of the file containing the descriptive grammar.
3. The program will generate files with morphemes and segmented words.
4. Start the chunker selecting **option 2**
5. Enter the name of the file containing the descriptive grammar.
6. Specify the number of new segments and the number of iterations.
7. The chunker will process the data and output the analysis results.
8. To Compare Morphemes Select **option 3** (Ensure the chunker has been started and the descriptive grammar has been processed.)
9. To Compare Segmentations Select **option 4** (Ensure the chunker has been started and the descriptive grammar has been processed.)
10. Select **option 5** to exit the program.

## (PB)

## Autoria e Afiliação

- **Autores:** Antonio Morais de Freitas Neto e Prof. João Paulo Lazzarini Cyrino
- **Afiliação:** Universidade Federal da Bahia

## Descrição

Este projeto implementa um algoritmo de Comprimento Mínimo de Descrição (MDL) para segmentação morfológica baseado no algoritmo proposto por Carl De Marcken. O objetivo é segmentar um corpus em morfemas de forma eficiente, minimizando o custo combinado de codificação do léxico e do próprio corpus.

## Módulos

O projeto está dividido em vários módulos para melhor organização e manutenção:

1. **`process_descriptive_grammar.py`**: Contém a classe `ProcessDescriptiveGrammar`, responsável por extrair palavras e morfemas de um arquivo de gramática descritiva.
2. **`uchunker.py`**: Contém a classe `UChunker`, que lida com o processo de chunking e segmentação usando o princípio MDL.
3. **`comparison.py`**: Fornece funções para comparar morfemas e segmentações com um léxico e gravar os resultados em arquivos de saída.
4. **`menu.py`**: Implementa uma interface de menu para usuários interagirem com as diferentes funcionalidades do projeto.
5. **`main.py`**: O ponto de entrada da aplicação que executa a interface do menu.

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/Netoamf/PIBIC-2023-24/tree/main/UChunker.git
   ```

## Utilização

1. Execute o script principal:
   ```bash
   python main.py
   ```

**Siga as instruções do menu para:**
- Processar a gramática descritiva.
- Iniciar o chunker.
- Comparar Morfemas.
- Comparar Segmentações.

## Instruções Detalhadas

1. Selecione a **opção 1** no menu.
2. Digite o nome do arquivo que contém a gramática descritiva.
3. O programa irá gerar arquivos com morfemas e palavras segmentadas.
4. Inicie o chunker selecionando a **opção 2**.
5. Digite o nome do arquivo que contém a gramática descritiva.
6. Especifique o número de novos segmentos e o número de iterações.
7. O chunker irá processar os dados e exibir os resultados da análise.
8. Para comparar morfemas, selecione a **opção 3** (certifique-se de que o chunker foi iniciado e a gramática descritiva foi processada).
9. Para comparar segmentações, selecione a **opção 4** (certifique-se de que o chunker foi iniciado e a gramática descritiva foi processada).
10. Selecione a **opção 5** para sair do programa. 