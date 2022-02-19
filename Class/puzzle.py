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

        # Determine how the answer compared to the real answer
        print(f"Attempt {self.usedAttempts + 1}: {guess}")
        if len(self.answer.word) > 0:
            return self.compareKnownAnswer(guess)
        else:
            return self.compareUnknownAnswer(guess)

    # =============================================
    # Used to attempt to solve the puzzle with a word when the answer is known
    # =============================================
    def compareKnownAnswer(self, guess):
        # Create a parallel array of results (parallel to the characters in the string)
        matching_characters = []
        index = 0
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

    # =============================================
    # Used to attempt to solve the puzzle with a word
    # =============================================
    def compareUnknownAnswer(self, guess):
        # Display legend
        print("Enter the following values for each letter:")
        print(f"{AttemptResult.EXACT.value} (Green): Letter was correct")
        print(f"{AttemptResult.WRONG_POSITION.value} (Yellow): Letter is in another position of the word")
        print(f"{AttemptResult.WRONG.value} (Red/Grey): Letter does not exist in the word")

        # Enter number result of each value
        attempt_results = []
        for character in guess:
            attempt_results.append(input(f"\t{character}: "))

        # Complete a usage
        self.usedAttempts += 1

        # Return number result array
        return attempt_results