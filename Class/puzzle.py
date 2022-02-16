from .Word import MyWord

class MyPuzzle(object):

    # =============================================
    # Constructor
    # =============================================
    def __init__(self, my_answer):
        self.answer = my_answer if my_answer else MyWord() # Set the answer to the puzzle
