# chunker/uchunker.py
def run_uchunker(grammar):
    # Função simplificada do UChunker
    segments = grammar.sentence.split()
    analysis_result = {
        'segments': segments,
        'hypothesis': 'hypothetical analysis',
        'lexicon': 'sample lexicon'
    }
    return analysis_result
