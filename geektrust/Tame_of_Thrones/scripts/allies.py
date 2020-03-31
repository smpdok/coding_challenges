class Ally:
    def __init__(self, msg, animal):
        self.msg = msg
        self.animal = animal

    def ally_check(self):
        """[Check whether the decrypted msg has allies's animal in it]
        
        Returns:
            [bool] -- [True if animal is present else False]
        """
        # print(f'msg: {self.msg} and animal:{self.animal}')
        count = 0
        for item in self.animal:
            if item in self.msg:
                count += 1
                self.msg.remove(item)
        if count == len(self.animal):
            return True
        return False