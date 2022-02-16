from .puzzle import MyPuzzle
from .Word import MyWord
from english_words import english_words_set

# =============================================
# This class utilizes a python dictionary library.
# enlish-words-py: https://pypi.org/project/english-words/
# =============================================
class PuzzleSolver(object):
    def SolvePuzzle(self):
        dictionary = self.buildWordList()
        print(dictionary)
        
    # =============================================
    # Build a list of words to use as a dictionary. 
    # This list only includes the words that are the length of the target word size for the puzzle
    # =============================================
    def buildWordList(self):
        foundWords = []
        for word in english_words_set:
            if len(word) == MyWord.MAX_WORD_LENGTH: # Build a list of words that can apply to the max word length
                foundWords.append(word.upper())
        return foundWords
