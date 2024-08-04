# EN Version
# BPE Pipeline 

This project implements a Byte Pair Encoding (BPE) processing pipeline for text tokenization and word segmentation.

## Authorship

- **Authors:** Antonio Morais de Freitas Neto and Fernando Yamaguchi


## Modules

- `corpus.py`: Functions for reading and processing the corpus.
- `bpe.py`: Functions for BPE operations.
- `analysis.py`: Functions for analyzing results.
- `plotting.py`: Functions for plotting results.
- `corpus_creation.py`: Functions for creating corpus and morphemes files from an input file.
- `main.py`: Main execution script.


## Usage

1. Modify the configuration in `config.json`.
2. Create your corpus and morphemes files by running:
    ```bash
    python -c "from corpus_creation import words_from_file, extract_morphemes_from_file; words_from_file('input_file.txt'); extract_morphemes_from_file('input_file.txt')"
    ```
3. Run the main script:
    ```bash
    python main.py
    ```

# PB Version

# Pipeline BPE 
Este projeto implementa um pipeline de Byte Pair Encoding (BPE) para tokenização de texto e segmentação de palavras.

## Autoria

- **Autores:** Antonio Morais de Freitas Neto e Fernando Yamaguchi

## Módulos

- `corpus.py`: Funções para leitura e processamento do corpus.
- `bpe.py`: Funções para operações BPE.
- `analysis.py`: Funções para análise de resultados.
- `plotting.py`: Funções para plotagem de resultados.
- `corpus_creation.py`: Funções para criar arquivos de corpus e morfemas a partir de um arquivo de entrada.
- `main.py`: Script principal de execução.


## Uso

1. Modifique a configuração no `config.json`.

2. Crie seus arquivos de corpus e morfemas executando:
    ```bash
    python -c "from corpus_creation import words_from_file, extract_morphemes_from_file, words_from_file_regex; words_from_file('input_file.txt'); extract_morphemes_from_file('input_file.txt'); words_from_file_regex('input_file.txt')"
    ```
3. Execute o script principal:
    ```bash
    python main.py
    ```
