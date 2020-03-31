import sys
from data import parameters
from scripts.decrypt_message import DecryptMessage
from scripts.read_file import ReadFile
from scripts.allies import Ally


def parse_message(rows, ally_list):
    """[Parse message and find the allies]
    
    Arguments:
        rows {[list]} -- [rows extracted from input file]
    
    Returns:
        [list] -- [List containing all the allies of ruler]
    """
    for row in rows:
        kingdom, space, msg = row.partition(' ')
        animal = parameters.kingdom_animal_dict[kingdom]
        decrypt_obj = DecryptMessage(msg, animal)
        decrypt_obj.alphabet_to_number()
        decrypt_obj.decrypt()
        decrypt_obj.negative_cases()
        decrypted_message = decrypt_obj.number_to_alphabet()
        ally_obj = Ally(decrypted_message, animal)
        if ally_obj.ally_check() and kingdom not in ally_list:
            ally_list.append(kingdom)
    return ally_list


if __name__ == "__main__":
    input_file_path = sys.argv[1]
    if input_file_path != '':
        file_obj = ReadFile(input_file_path)
        rows = file_obj.read_from_file()
    if rows:
        ally_list = parameters.ally_list
        allies = parse_message(rows, ally_list)
    if len(allies) > 3:
        print(*allies)
    else:
        print(None)
