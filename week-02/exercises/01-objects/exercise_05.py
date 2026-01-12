from musician import Musician


def main():
    musicians = []
    musicians.append(Musician("Frank Ocean", 10))
    musicians.remove

    m = Musician()
    print("Enter your top 5 favorite Musicians.")

    for _ in range(5):
        m.name = input("Musician name: ")
        m.rating = int(input("Musician rating: "))
        musicians.append(m)

    # 1. Use a loop to populate the `musicians` array with your top 5 favorite musicians.
    # (Replace Frank Ocean.)
    # Create musicians from user input. (See exercise_04.py.)

    # 2. Use a second loop to print details about each musician.

    for i in range(5):
        print(f"{i+1}: {m.name}: {m.rating}")


if __name__ == "__main__":
    main()
