from Class.puzzle import MyPuzzle
from Class.Word import MyWord

def main():
    # Create a puzzle with an answer
    daily_puzzle = MyPuzzle(MyWord())
    
    # Output the answer letters to the puzzle
    print(f"Answer today: {daily_puzzle.answer.word}")
    
    # Attempt a word
    attempt1 = daily_puzzle.playWord("Blaek")
    print(f"Attempt 1: {attempt1}")

if __name__ == "__main__":
    main()