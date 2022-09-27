from ai_replica.common import get_answer, load_global_model, reconstruct_mind

"""A simple console interface for the replica. Just run it with Python, and it should work."""


def main():
    print("Reconstructing the mind...")
    reconstruct_mind()
    print(
        "Done. Now, just enter something and press Enter. If you want to exit, press CTRL+C"
    )
    print("Loading model")
    load_global_model()

    print(f"Enter something and press Enter. If you want to exit, press CTRL+C")

    while True:
        user_input = input("Enter something:\n")
        answer = get_answer(user_input)
        print(f"\n*Bot*: {answer}\n")


if __name__ == "__main__":
    main()
