import string as str

class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters
        
    def print_letters(self):
        print(f"Буквы : {self.letters}")
    def letters_num(self):
        return len(self.letters)

class EngAlphabet(Alphabet):
    __letters_num = len(str.ascii_uppercase)

    def __init__(self):
        super().__init__('en', str.ascii_uppercase)

    def is_en_letter(self, letter: str) -> bool:
        return letter.upper() in self.letters

    def letters_num(self):
        return self.__letters_num

    @staticmethod
    def example() -> str:
        return "Hello, world!"
