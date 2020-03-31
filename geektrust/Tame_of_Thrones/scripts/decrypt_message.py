from string import ascii_uppercase


class DecryptMessage:
    def __init__(self, msg, animal):
        self.msg = msg
        self.num_to_alph = {
            idx + 1: alph
            for (idx, alph) in enumerate(ascii_uppercase)
        }
        self.alph_to_num = {
            alph: idx + 1
            for (idx, alph) in enumerate(ascii_uppercase)
        }
        self.animal = animal
        self.key = len(self.animal)

    def alphabet_to_number(self):
        """[Changes alphabets to respective number]
        
        Returns:
            [list] -- [list with alphabets replaced as numbers]
        """
        self.msg = [
            self.alph_to_num[alph] for alph in self.msg if alph.isalpha()
        ]
        return self.msg

    def decrypt(self):
        """[Decrpyt number by subtracting key from each number]
        
        Returns:
            [list] -- [list with decrypted numbers]
        """
        self.msg = [num - self.key for num in self.msg]
        return self.msg

    def negative_cases(self):
        """[Replaces negative numbers after decrpytion by adding 26]
        
        Returns:
            [list] -- [list with negative numbers changed to 26 + num]
        """
        self.msg = [26 + num if num < 1 else num for num in self.msg]
        return self.msg

    def number_to_alphabet(self):
        """[Changes number  back to respective alphabet]
        
        Returns:
            [list] -- [list with numbers replaced as respective alphabets]
        """
        self.msg = [self.num_to_alph[num].upper() for num in self.msg]
        return self.msg