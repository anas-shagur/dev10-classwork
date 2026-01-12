from balloon import Balloon


def main():
    # BALLOON GAME

    # 1. Instantiate three balloons of different colors.

    b1 = Balloon("Blue")
    b2 = Balloon("Green")
    b3 = Balloon("Yellow")

    while True:
        if input("Inflate? [y/n]: ").strip().lower() == "y":
            # 2. If the user confirms an inflate, inflate each balloon.
            b1.inflate()
            b2.inflate()
            b3.inflate()
            if b1.is_exploded() or b2.is_exploded() or b3.is_exploded():
                break
            pass

        # 3. When one or more balloons explode, stop the loop.

    # 4. Print the color of the winners (balloons that exploded).
    if b1.is_exploded():
        print(b1.color)
    if b2.is_exploded():
        print(b2.color)
    if b3.is_exploded():
        print(b3.color)


if __name__ == "__main__":
    main()
