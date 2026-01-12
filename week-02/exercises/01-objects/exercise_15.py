from hero import Hero, Power

# 1. Create a new method in the Hero class.
# Name: to_line
# Inputs: none (self)
# Output: String
# Description: returns the Hero's name and powers as a single line of text.


def main():
    # 2. Instantiate your three favorite super heroes with appropriate powers.
    levitation = Power("Levitation")
    flight = Power("Flight")
    blastPower = Power("Blast Power")

    h1 = Hero("Black Panther", [levitation, flight])
    h2 = Hero("Superman", [flight, blastPower])
    h3 = Hero("Static Shock", [blastPower])

    # 3. Use the `to_line` method to print each hero's details to the console.
    print(h1.to_line())
    print(h2.to_line())
    print(h3.to_line())

    pass


if __name__ == "__main__":
    main()
