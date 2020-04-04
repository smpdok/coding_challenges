import argparse
from data import parameters
from scripts.message import Message
from scripts.read_file import ReadFile


class Southeros:
    def __init__(self, king, msgs, allies_required):
        self.king = king
        self.msgs = msgs
        self.allies_required = allies_required
        self.allies = parameters.allies[self.king]
        self.ruler = ''

    def get_allies(self):
        if len(self.allies) > self.allies_required:
            self.allies = " ".join(self.allies)
        else:
            self.allies = None
        return self.allies

    def set_ruler(self, king):
        self.ruler = king

    def get_ruler(self):
        return self.ruler

    def send_the_ravens(self):
        """[Send the messages and find the allies]
        """
        for msg in self.msgs:
            kingdom, space, secret_msg = msg.partition(' ')
            emblem = parameters.kingdom_emblem_dict[kingdom]
            msg_obj = Message(secret_msg, emblem)
            decrypted_msg = msg_obj.decrypt_message_with_key()
            if msg_obj.verify_message(
                    decrypted_msg) and kingdom not in self.allies:
                self.allies.append(kingdom)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Available Arguments')
    parser.add_argument('--file', dest="file", action="store")
    parser.add_argument('--king',
                        dest="king",
                        action="store",
                        default=parameters.default_king,
                        choices=parameters.kings_in_southeros)
    args, unknown_args = parser.parse_known_args()
    # If --file argument isn't passed input_file_path will be selected from unknown_args
    try:
        input_file_path = args.file.strip()
    except AttributeError:
        input_file_path = unknown_args[0]
    king = args.king.strip()
    if input_file_path != '':
        file_obj = ReadFile(input_file_path)
        msgs = file_obj.read_from_file_as_rows()
    if msgs:
        allies_required = parameters.allies_required
        southeros_obj = Southeros(king, msgs, allies_required)
        southeros_obj.send_the_ravens()
        allies = southeros_obj.get_allies()
        print(allies)
        if allies:
            southeros_obj.set_ruler(king)
