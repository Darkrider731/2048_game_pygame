class Error():
    def __init__(self, number):
        self.number = number

    def handle_error(self):
        error_code = str(self)
        string = ('   '+ error_code)
        print(f'\033[91m{string}\033[0m')
        error_code = str(self.number)
        string = ('error 0000' + error_code)
        print(f'\033[91m{string}\033[0m')