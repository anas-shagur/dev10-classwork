from musician import Musician


def main():
    # 1. Add setters for both the name and rating fields in Musician.

    one = Musician("Frank Ocean", 10)
    print(one.name)

    # 2. Use the appropriate setter to change Musician one's name to your favorite musician.
    # (If Frank Ocean is your favorite musician, choose your second favorite.)

    one.name = "Lupe Fiasco"
    print(one.name)

    # Expected Output
    # Frank Ocean
    # [Your Favorite Musician]


if __name__ == "__main__":
    main()
