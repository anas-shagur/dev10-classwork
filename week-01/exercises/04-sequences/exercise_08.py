import random


def make_bug_list():
    bugs = ["beetle"] * 200
    for _ in range(random.randint(0, 150)):
        bugs[random.randint(0, 199)] = "mosquito"
    return bugs


if __name__ == "__main__":
    bugs = make_bug_list()
    beetles = 0
    mosquitoes = 0
    for i in range(len(bugs)):
        if bugs[i] == "beetle":
            beetles += 1
        else:
            mosquitoes += 1
    print(f"Beetles: {beetles}")
    print(f"Mosquitoes: {mosquitoes}")


    # The bugs list elements are either the value "beetle" or "mosquito".
    # 1. Count the number of beetles and mosquitoes.
    # 2. Print the result.
    # Results will vary because of randomness.
