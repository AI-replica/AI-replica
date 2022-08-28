from ai_replica.common import get_answer
from ai_replica.engine.reconstruct_mind import reconstruct

"""A simple console interface for the replica. Just run it with Python, and it should work."""

if __name__ == "__main__":
    print("Reconstructing the mind...")
    reconstruct()
    print(
        "Done. Now, just enter something and press Enter. If you want to exit, press CTRL+C"
    )
    while True:
        user_input = input("Enter something:\n")
        answer = get_answer(user_input)
        print("\n" + answer + "\n")
