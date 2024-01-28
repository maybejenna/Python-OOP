import random

class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, file_path):
        """Initialize the WordFinder with a file path."""
        self.file_path = file_path
        self.words = []
        self._read_words()

    def _read_words(self):
        """Read words from a file and store them in a list."""
        with open(self.file_path, 'r') as file:
            for line in file:
                word = line.strip()
                if word:  # This checks if the line is not empty
                    self.words.append(word)
        print(f"{len(self.words)} words read")

    def random(self):
        """Return a random word from the list of words."""
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    """Special Word Finder: finds random words, excluding comments and blank lines."""

    def _read_words(self):
        """Read words from a file, ignoring comments and blank lines."""
        with open(self.file_path, 'r') as file:
            for line in file:
                word = line.strip()
                if word and not word.startswith('#'):
                    self.words.append(word)
        print(f"{len(self.words)} words read")

wf = WordFinder("python-oo-practice/words.txt")