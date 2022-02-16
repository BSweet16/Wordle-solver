from Class.puzzle import MyPuzzle
from Class.Word import MyWord

def main():
    # Create a puzzle with an answer
    daily_puzzle = MyPuzzle(MyWord("Blake"))
    
    # Output the answer letters to the puzzle
    print(f"Answer today: {daily_puzzle.answer.word}")

if __name__ == "__main__":
    main()