import os


class ReadFile:
    def __init__(self, input_file_path):
        self.input_file_path = input_file_path

    def read_from_file(self):
        """[Read rows from input file]
        
        Returns:
            [list] -- [List of all the rows]
        """
        if not os.path.exists(self.input_file_path):
            print('File Does Not Exist')
        else:
            with open(self.input_file_path, 'r') as f:
                rows = f.readlines()
                rows = [row.strip() for row in rows]
            return rows