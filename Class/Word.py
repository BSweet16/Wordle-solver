class MyWord(object):
    MAX_WORD_LENGTH = 5

    # =============================================
    # Constructor
    # =============================================
    def __init__(self, characters = ""):
        if len(characters) <= self.MAX_WORD_LENGTH:
            self.word = characters # Set the characters in passed to the letters
        else:
            print(f"Error: {characters} exceeds maximum character limit of {self.MAX_WORD_LENGTH} by {len(characters) - self.MAX_WORD_LENGTH} character(s).")

    # =============================================
    # Determine if a word matches the current word
    # =============================================
    @classmethod
    def checkMatch(self, compareWord):
        my_length = self.word.len()
        compare_length = compareWord.len()

        # Search for non-matching letters
        if my_length == compare_length:
            index = 0
            for letter in compareWord:
                if letter != self.word[index]: # Compare each own letter to given word
                    return False
                index += 1
            return True

        return False