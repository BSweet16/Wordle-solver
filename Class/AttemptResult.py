from enum import Enum

class AttemptResult(Enum):
    EXACT = "0"               # The character is the correct letter in the correct place
    WRONG_POSITION = "1"      # The character exists in the word, but not in this position
    WRONG = "2"               # The character does not exist in the word at all
    SKIP = "S"                # Skip the word choice
    SKIP_WORD = "SKIP"        # The word version option to skip the current word choice