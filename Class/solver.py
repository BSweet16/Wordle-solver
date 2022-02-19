from .puzzle import MyPuzzle
from .Word import MyWord
from .AttemptResult import AttemptResult
from english_words import english_words_set

# =============================================
# This class utilizes a python dictionary library.
# enlish-words-py: https://pypi.org/project/english-words/
# =============================================
class PuzzleSolver(object):
    puzzle = MyPuzzle("")

    # =============================================
    # This function is responsible for the organization of calling all 
    # methods needed to solve the puzzle. 
    # =============================================
    def SolvePuzzle(self):
        self.dictionary = self.buildWordList()
        print()

        # Attempt to solve the puzzle 
        puzzle_solved = False
        while((self.puzzle.usedAttempts < self.puzzle.MAX_ATTEMPTS) and puzzle_solved == False): # Continue until out of guesses or the puzzle is solved
            attempt_results = self.playBasicAttempt() # Attempt a guess and filter the results accordingly

            # Determine if the correct answer has been found
            correct_answer = True
            for attempt_result in attempt_results:
                if attempt_result != AttemptResult.EXACT.value:
                    correct_answer = False

            # Output success message!
            if correct_answer == True:
                puzzle_solved = correct_answer
                print(f"Puzzle solved in {self.puzzle.usedAttempts} attempts")
                return

        # Output failure message
        print("Unable to solve puzzle... ")
        print(f"Remaining options: {self.dictionary}")
        return
        
        
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

    # =============================================
    # Attempts to solve the puzzle with a word
    # This is the most basic method to attempt to solve the puzzle
    # =============================================
    def playBasicAttempt(self):
        # Make an attempt of a word
        attempted_word = self.dictionary[0]
        matching_characters = self.puzzle.playWord(attempted_word) # Uses first word in the known dictionary

        # Filter the dictonary according to the results
        index = 0 # The index of the current letter in the guessed word being evaluated
        for attempted_letter in attempted_word:
            if matching_characters[index] == AttemptResult.EXACT.value: # Keep words with this letter in this position
                for word in self.dictionary:
                    if word[index] != attempted_letter: # If the letters DON'T match, remove the word. They should match, according to the attempt result
                        self.dictionary.remove(word)
            elif matching_characters[index] == AttemptResult.WRONG_POSITION.value: # Remove words with letter in this position
                for word in self.dictionary:
                    if word[index] == attempted_letter: # If the letters DO match, remove the word. They should not match, according to the attempt result
                        self.dictionary.remove(word)
            elif matching_characters[index] == AttemptResult.WRONG.value: # Remove words with this letter
                for word in self.dictionary:
                    if attempted_letter in word: # If the letter exists in the word, remove the word. It shoudl not exist in the word at all, according to the attempt result
                        self.dictionary.remove(word)
            else: 
                print("Error: Discovered unrecognized attempt result value while filtering")

            index += 1
        print(f"Remaining options: {self.dictionary}")
        return matching_characters
        
