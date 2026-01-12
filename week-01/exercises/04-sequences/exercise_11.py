import random


def make_random_state_town_list():
    result = []
    for _ in range(random.randint(50, 150)):
        match random.randint(0, 7):
            case 0:
                result.append("AL")
            case 1:
                result.append("AK")
            case 2:
                result.append("AR")
            case 3:
                result.append("AZ")
            case 4:
                result.append("Boring")
            case 5:
                result.append("Loafers Glory")
            case 6:
                result.append("Handsome Eddy")
            case 7:
                result.append("Lonelyville")

    return result


if __name__ == "__main__":
    states_or_towns = make_random_state_town_list()
    towns = []
    for i in range(len(states_or_towns)):
        if len(states_or_towns[i]) != 2:
            towns.append(states_or_towns[i])
    print(towns)

    # The states_or_towns list contains either state abbreviations or town names.
    # You can distinguish state abbreviations by their length. They're always two characters.
    # 1. Create a list[str] to hold the towns.
    # 2. Loop through states_or_towns and append towns to the list.
    # 3. Print the town array.
