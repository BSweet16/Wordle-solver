from .puzzle import MyPuzzle
from .Word import MyWord
from .AttemptResult import AttemptResult
from english_words import english_words_set

# =============================================
# This class utilizes a python dictionary library.
# enlish-words-py: https://pypi.org/project/english-words/
# =============================================
class PuzzleSolver(object):
    puzzle = MyPuzzle("") # To use the solver functions, set the puzzle to empty string here

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
            for attempt_result in attempt_results: # There was at least 1 letter that wasn't correct
                if attempt_result != AttemptResult.EXACT.value:
                    correct_answer = False
            if len(attempt_results) == 0: # The dictionary ran out of words
                correct_answer = False
                break

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
        if len(self.dictionary) > 0:
            attempted_word = self.dictionary[0]
            attempt_results = self.puzzle.playWord(attempted_word) # Uses first word in the known dictionary
        else:
            print("No words match these requirements")
            return []

        # Filter the dictonary according to the results
        attempt_letter_index = 0 # The index of the current letter in the guessed word being evaluated
        valid_words = [] # Build a list of words to remove
        for attempted_letter in attempted_word:

            # Check if the word was valid
            if attempted_letter.upper() == AttemptResult.SKIP or attempted_letter.upper() == AttemptResult.SKIP_WORD:
                self.dictionary = self.dictionary.remove(attempted_word) # Remove the selected word from the list
                break

            for word in self.dictionary:
                if word == attempted_word: # Evaluating attempted word
                    if word not in valid_words:
                        if (AttemptResult.WRONG_POSITION.value not in attempt_results) and (AttemptResult.WRONG_POSITION.value not in attempt_results) and (AttemptResult.WRONG.value not in attempt_results): # Attempted word was the answer
                            self.dictionary = [word]
                            return attempt_results
                else: # Not evaluating attempted word
                    if (attempt_results[attempt_letter_index] == AttemptResult.EXACT.value) and (word not in valid_words): # Keep words with this letter in this position
                        if word[attempt_letter_index] == attempted_letter: # If the letters DO match, keep the word. They should match, according to the attempt result
                            valid_words.append(word)
                    elif attempt_results[attempt_letter_index] == AttemptResult.WRONG_POSITION.value and word not in valid_words: # Remove words with letter in this position
                        if word[attempt_letter_index] != attempted_letter and attempted_letter in word: # If the letters DON'T match AND the rest of the word has that letter, keep the word. They should not match, according to the attempt result
                            valid_words.append(word)
                    elif attempt_results[attempt_letter_index] == AttemptResult.WRONG.value and word not in valid_words: # Remove words with this letter
                        if attempted_letter not in word: # If the letter exists in the word, remove the word. It shoudl not exist in the word at all, according to the attempt result
                            valid_words.append(word)
                    elif word in valid_words:
                        continue # Just ignore it if the word is already in the list
                    else: 
                        print("Error: Discovered unrecognized attempt result value while filtering")

            attempt_letter_index += 1
        self.dictionary = valid_words # Update the dictionary with the filtered values
        print(f"Remaining options: {self.dictionary}")
        return attempt_results
        
