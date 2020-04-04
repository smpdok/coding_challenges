from string import ascii_uppercase, ascii_lowercase
from data import parameters


class Message:
    def __init__(self, msg, emblem):
        self.msg = msg
        self.emblem = emblem
        if self.msg.isupper():
            self.case = ascii_uppercase
        else:
            self.case = ascii_lowercase
        self.encrypted_direction = parameters.encrypted_direction
        if self.encrypted_direction == 'clockwise':
            self.key = len(self.emblem)
        else:
            self.key = -len(self.emblem)

    def decrypt_message_with_key(self):
        decrypted_msg = ''
        l = len(self.case)
        for char in self.msg:
            if char in self.case:
                decrypted_msg = decrypted_msg + self.case[
                    (self.case.index(char) - self.key) % l]
            else:
                decrypted_msg += char
        return decrypted_msg

    def verify_message(self, decrypted_msg):
        """[Check whether the decrypted msg has allies's emblem in it]
        
        Returns:
            [bool] -- [True if emblem is present else False]
        """
        self.decrypted_msg = sorted(decrypted_msg)
        self.emblem = sorted(self.emblem)
        it = iter(self.decrypted_msg)
        return all(item in it for item in self.emblem)