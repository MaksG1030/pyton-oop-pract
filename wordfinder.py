"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    ...
    def __init__(self, file):
        """Initiates new class of word finder, which takes STRING of the path of TXT file"""
        word_file = open(file, "r")
        self.words = self.read_file(word_file)
        print(f"{len(self.words)} words read")
    def read_file(self, word_file):
        """Opens the file, returns a list with each single word in word_file
        """
        return [word.strip() for word in word_file]
    def random(self):
        """get random choice of our words list"""
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    def read_file(self, word_file):
        """will check to see if word is a valid word (no blanks or starts with #)"""
        return [word.strip() for word in word_file if word.strip() and not word.startswith("#")]