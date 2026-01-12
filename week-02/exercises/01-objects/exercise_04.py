from musician import Musician


def main():
    # 1. Add two default values to the __init__ method in Musician.
    # 2. Uncomment the code below and make sure it runs.

    m = Musician()
    m.name = input("Musician name: ")
    m.rating = int(input("Musician rating: "))
    print(f"{m.name}: {m.rating}")

    # 3. Add a loop. The exercise should ask the user for musicians and print
    # them out until the user types "end".

    print("Type 'end' to end loop./n")

    while True:
        m.name = input("Musician name: ")

        if m.name.lower() == "end":
            print("Exiting loop...")
            break
        
        m.rating = int(input("Musician rating: "))
        print(f"{m.name}: {m.rating}")


    pass


if __name__ == "__main__":
    main()
