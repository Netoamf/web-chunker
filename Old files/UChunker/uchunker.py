from math import log2, inf
from collections import Counter
from process_descriptive_grammar import ProcessDescriptiveGrammar

class UChunker:
    def __init__(self, filename, analysis_output_path="outputs/analysis.txt", segment_frequency_output="outputs/segment_frequency.txt"):
        """
        Initializes the UChunker with the provided filename and output files.
        """
        self.process_grammar = ProcessDescriptiveGrammar(filename)
        self.corpus = self.process_grammar.words_from_descriptive_grammar()
        self.char_set = set()
        self.lexicon = Counter()
        self.analysis_output = analysis_output_path
        self.segment_frequency_output = segment_frequency_output
        for line in self.corpus:
            chars = ''.join(line)
            for c in chars:
                self.lexicon[c] += 1
            self.char_set |= set(chars)
        self.char_cost = -1 * log2(1 / len(self.char_set))

    def start(self, n_new_segments, n_iterations):
        """
        Starts the chunker process with specified segments and iterations.
        """
        for i in range(n_iterations):
            first_parse = self.new_segments_from_parse()
            print(f"Iteração {i}")
            print(f"Custo atual do léxico: {self.lexicon_cost()}")
            print(f"Custo atual da análise: {first_parse[1]}")
            print(f"Custo da hipótese: {self.lexicon_cost() + first_parse[1]}")
            self.new_lexicon(first_parse[0], n_new_segments)

    def new_segments_from_parse(self):
        """
        Parses the corpus to find new segments.
        :return: New segments and their parse cost.
        """
        new_segments = Counter()
        parse_cost = 0
        for line in self.corpus:
            analysis_cost, parse = self.analyse(line)
            parse_cost += analysis_cost
            for i in range(0, len(parse), 2):
                if i == len(parse) - 1:
                    new_segments[parse[i]] += 1
                else:
                    new_segments[parse[i] + parse[i + 1]] += 1
        return new_segments, parse_cost

    def new_lexicon(self, new_segments, n_new_segments):
        """
        Updates the lexicon with new segments.
        """
        new_segments_count = {}
        for segment, freq in new_segments.most_common(n_new_segments):
            new_segments_count[segment] = freq
        for segment, freq in new_segments_count.items():
            self.lexicon[segment] += freq
        with open(self.segment_frequency_output, "w", encoding="UTF-8") as segment_frequency_file:
            for segment, freq in self.lexicon.items():
                segment_frequency_file.write(f"{segment}: {freq}\n")
        new_lexicon = Counter()
        for line in self.corpus:
            for segment in self.analyse(line)[1]:
                new_lexicon[segment] += 1
        self.lexicon = new_lexicon

    def item_cost(self, item):
        """
        Computes the cost of an item based on its probability in the lexicon.
        :param item: Item to compute the cost for.
        :return: Cost of the item.
        """
        prob = self.lexicon[item] / self.lexicon.total()
        if prob == 0:
            return inf
        return -1 * log2(prob)

    def analyse(self, char_sequence):
        """
        This method employs a forward-backward algorithm.
        The forward step computes the optimal segmentation and associated costs for each prefix of the sequence.
        The backward step traces back from the end of the sequence to find the actual segmentation that yields the minimum cost.

        :param char_sequence: Character sequence to analyze.
        :type char_sequence: str
        :return: Tuple containing the cost of the analysis and the list of segments.
        :rtype: Tuple[float, List[str]]
        """
        # Initialize the costs array with zero cost for the empty prefix
        costs = [0]
        # Initialize the segments list to store the best segmentation for each prefix
        segments = []

        # forward step: Compute the minimum cost for each prefix of the sequence
        for final_position in range(1, len(char_sequence) + 1):
            # Dictionary to store the cost of each candidate segment ending at final_position
            candidates = dict()

            # Consider all possible segments ending at final_position
            for initial_position in range(0, final_position):
                current_sequence = char_sequence[initial_position:final_position]
                # Compute the cost of the current segment plus the cost of the preceding prefix
                candidates[current_sequence] = self.item_cost(current_sequence) + costs[initial_position]
            # Choose the segment with the minimum cost
            chosen = min(candidates, key=candidates.get)

            if candidates[chosen] == inf:
                chosen = char_sequence[final_position - 1]

            segments.append(chosen)
            costs.append(candidates[chosen])

        # backward step: Trace back to determine the final segmentation
        reversed_segments = list(reversed(segments))
        final_segments = []
        i = 0
        while i < len(reversed_segments):
            final_segments.append(reversed_segments[i])
            segment_length = len(reversed_segments[i])
            i += segment_length
        # Compute the total cost of the analysis by summing the costs of the final segments
        cost_of_analysis = sum(map(self.item_cost, final_segments))

        with open(self.analysis_output, "a", encoding="UTF-8") as analysis_file:
            analysis_file.write(f"Análise: {' '.join(final_segments)}\n")

        # Return the total cost of the analysis and the final segmentation in the correct order
        return cost_of_analysis, list(reversed(final_segments))

    def analysis_cost(self):
        """
        Computes the total cost of analysis.
        :return: Total analysis cost.
        """
        return sum(map(lambda x: self.analyse(x)[0], self.corpus))

    def lexicon_cost(self):
        """
        Computes the total cost of the lexicon.
        :return: Total lexicon cost.
        """
        return sum(map(lambda x: len(x) * self.char_cost, self.lexicon.keys()))

    def hypothesis_cost(self):
        """
        Computes the total hypothesis cost.
        :return: Total hypothesis cost.
        """
        return self.lexicon_cost() + self.analysis_cost()
