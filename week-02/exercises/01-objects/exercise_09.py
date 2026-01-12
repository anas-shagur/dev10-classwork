from balloon import Balloon

# 1. Create a new method in the Balloon class.
# Name: is_exploded
# Inputs: none (self)
# Output: boolean
# Description: if the self._psi field is greater than 16.0, returns True.
# Otherwise, returns False.

# 2. Edit the psi @property.
# If the self._psi field is greater than 16.0, return the float positive "inf".
# Otherwise, return self._psi.


def main():
    # 3. Uncomment the code below.
    # 4. Fix any errors by editing the Balloon class.
    # 5. Confirm the output is similar to Sample Output

    b = Balloon("orange")
    for _ in range(10):
        b.inflate()
        print(f"psi:{b.psi}, exploded?:{"yes" if b.is_exploded() else "no"}")

    # Sample Output
    # psi:3.168552425925846, exploded?:no
    # psi:6.449317768787848, exploded?:no
    # psi:9.672181651750737, exploded?:no
    # psi:13.352370783778934, exploded?:no
    # psi:inf, exploded?:yes
    # psi:inf, exploded?:yes
    # psi:inf, exploded?:yes
    # psi:inf, exploded?:yes
    # psi:inf, exploded?:yes
    # psi:inf, exploded?:yes

    pass


if __name__ == "__main__":
    main()
