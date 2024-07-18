import re

def words_from_file(filename):
    words = []
    with open(filename, "r", encoding="UTF-8") as file:
        lines = file.readlines()
        for i in range(0, len(lines), 3):
            phrase = lines[i].strip().replace('-', '').split()
            words.extend(phrase)
    with open("corpus.txt", "w", encoding="UTF-8") as output_file:
        for word in words:
            output_file.write(word + "\n")
    return words

def extract_morphemes_from_file(filename):
    with open(filename, "r", encoding="UTF-8") as file:
        lines = file.readlines()
        with open("words.txt", "w", encoding="UTF-8") as output_file:
            for i in range(0, len(lines), 3):
                phrase = lines[i].strip()
                words = re.sub(r"-", " ", phrase).split()
                for word in words:
                    output_file.write(f"{word}\n")
