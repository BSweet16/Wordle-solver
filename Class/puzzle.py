from .Word import MyWord
from .AttemptResult import AttemptResult

class MyPuzzle(object):
    MAX_ATTEMPTS = 6

    # =============================================
    # Constructor
    # =============================================
    def __init__(self, my_answer):
        self.answer = my_answer if my_answer else MyWord()      # The answer to the puzzle
        self.usedAttempts = 0                                   # The number of attempts used

    # =============================================
    # Used to attempt to solve the puzzle with a word
    # =============================================
    def playWord(self, guess):
        # Check if an attempt is able to be used
        if self.usedAttempts >= self.MAX_ATTEMPTS:
            print("Unable to attempt answer. Maximum number of guesses reached.")
            return []
        
        matching_characters = []
        index = 0

        # Create a parallel array of results (parallel to the characters in the string)
        for character in guess:
            if character.upper() == self.answer.word[index].upper():        # Character exists in this position
                matching_characters.append(AttemptResult.EXACT.value)
            elif guess.find(character.upper()) > -1:                        # Character exists somewhere else in the answer
                matching_characters.append(AttemptResult.WRONG_POSITION.value)
            else:
                matching_characters.append(AttemptResult.WRONG.value)             # Character does not exist at all
            index += 1

        self.usedAttempts += 1
        
        return matching_characters