from Class.puzzle import MyPuzzle
from Class.Word import MyWord
from Class.solver import PuzzleSolver

def MainMenu():
    print("Which would you like to do? (Choose a number)")
    print("1: Play Wordle")
    print("2: Solve a Wordle")
    return input(">> ")

def PlayGame():
    # Welcome message
    print("Welcome to Wordle!")

    # Create a puzzle with an answer
    daily_puzzle = MyPuzzle(MyWord("Exams"))

    # Output the answer letters to the puzzle
    # print(f"Answer today: {daily_puzzle.answer.word}")

    # Attempt a word
    # attempt1 = daily_puzzle.playWord("Blaek")
    # print(f"Attempt 1: {attempt1}")

    return


def SolvePuzzle():
    PuzzleSolver().SolvePuzzle()

    return

def main():
    user_input = 0
    while user_input != 1 and user_input != 2:
        user_input = MainMenu()
        if user_input == "1":
            PlayGame()
        elif user_input == "2":
            SolvePuzzle()

        return
    return

if __name__ == "__main__":
    main()