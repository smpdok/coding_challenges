import sys
from string import ascii_uppercase


def read_from_file(input_file_path):
    with open(input_file_path, 'r') as f:
        rows = f.readlines()
        rows = [row.strip() for row in rows]
    return rows


def decrypt_message(rows, num_alph_dict, alph_num_dict, kingdom_animal_dict):
    ally_list = ['SPACE']
    for row in rows:
        kingdom, space, msg = row.partition(' ')
        animal = kingdom_animal_dict[kingdom.upper()]
        key = len(animal)
        # convert each alphabet to respective number
        msg = [alph_num_dict[alph] for alph in msg if alph.isalpha()]
        # Decrypt
        msg = [num - key for num in msg]
        # Eliminate -ve cases
        msg = [26 + num if num < 1 else num for num in msg]
        # Convert back to alphabets
        msg = [num_alph_dict[num].upper() for num in msg]

        result = check_animal(msg, animal)
        if result and kingdom not in ally_list:
            ally_list.append(kingdom)
    return ally_list


def check_animal(msg, animal):
    count = 0
    for item in animal:
        if item in msg:
            count += 1
            msg.remove(item)
    if count == len(animal):
        return True
    return False


if __name__ == "__main__":
    input_file_path = sys.argv[1]
    rows = read_from_file(input_file_path)
    # Dict with Key: Number Value: Alphabet
    num_alph_dict = {
        idx + 1: alph
        for (idx, alph) in enumerate(ascii_uppercase)
    }
    # Dict with Key: Alphabet Value: Number
    alph_num_dict = {
        alph: idx + 1
        for (idx, alph) in enumerate(ascii_uppercase)
    }
    kingdom_animal_dict = {
        'SPACE': 'GORILLA',
        'LAND': 'PANDA',
        'WATER': 'OCTOPUS',
        'ICE': 'MAMMOTH',
        'AIR': 'OWL',
        'FIRE': 'DRAGON'
    }
    ally_list = decrypt_message(rows, num_alph_dict, alph_num_dict,
                                kingdom_animal_dict)
    if len(ally_list) > 3:
        print(*ally_list)
    else:
        print(None)
