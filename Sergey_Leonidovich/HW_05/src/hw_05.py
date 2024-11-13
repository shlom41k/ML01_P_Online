"""
HW_05. Исходные данные и задание.
"""

"""
Класс Alphabet
1. Создайте класс Alphabet.
2. Создайте метод __init__(), внутри которого будут определены два динамических свойства:
    1) lang - язык;
    2) letters - список букв.
Начальные значения свойств берутся из входных параметров метода.
3. Создайте метод print(), который выведет в консоль буквы алфавита.
4. Создайте метод letters_num(), который вернет количество букв в алфавите.
"""

"""
Класс EngAlphabet
1. Создайте класс EngAlphabet путем наследования от класса Alphabet
2. Создайте метод __init__(), внутри которого будет вызываться родительский метод __init__(). 
В качестве параметров ему будут передаваться обозначение языка(например, 'En') и строка, 
состоящая из всех букв алфавита(можно воспользоваться свойством ascii_uppercase из модуля string).
3. Добавьте приватное статическое свойство __letters_num, которое будет хранить количество букв в алфавите.
4. Создайте метод is_en_letter(), который будет принимать букву в качестве параметра и определять, 
относится ли эта буква к английскому алфавиту.
5. Переопределите метод letters_num() - пусть в текущем классе классе он будет возвращать значение свойства __letters_num.
6. Создайте статический метод example(), который будет возвращать пример текста на английском языке.
"""


import string


class Alphabet:

    # Total objects in class
    __alphabets = []

    def __init__(self, language: str, letters: list):
        """
        Constructor: create object of class Alphabet.
        :param language: language (str);
        :param letters: list of letters for current language (list).
        """
        # Add properties
        self.__language = language
        self.__letters = letters

        # Add item to list of all class objects
        self.__class__.__alphabets.append(self)

    def __del__(self):
        """ Destructor """
        # Remove item from list of all class objects
        self.__class__.__alphabets.remove(self)

    def __str__(self) -> str:
        """ View for object, when use str() method """
        return f"{self.__language}"

    def __repr__(self) -> str:
        return self.__str__()

    @classmethod
    def get_all_alphabet(cls) -> list:
        """ Get lisf of all class objects """
        return cls.__alphabets

    @property
    def language(self) -> str:
        return self.__language

    @property
    def letters(self) -> list:
        return self.__letters

    def print_letters(self) -> None:
        """ Display all letters in alphabet """
        print(f"Буквы: {''.join(self.__letters)}.")

    def letters_num(self) -> int:
        """ Get number of letters in alphabet """
        return len(self.__letters)


class EngAlphabet(Alphabet):
    def __init__(self, language: str, letters: str):
        """
        Constructor: create object of class EngAlphabet.
        :param language: language (str);
        :param letters: letters for current language (str).
        """
        # Call parent class __init__() method
        super().__init__(language=language, letters=[letter for letter in letters])
        # Add new property for this class
        self.__letters_num = len(self.letters)

    def __del__(self):
        """ Destructor """
        super().__del__()

    def is_en_letter(self, letter: str) -> bool:
        """
        Checks whether a character belongs to the given alphabet
        :param letter: character (str);
        :return: True or False (boolean).
        """
        return True if letter.lower() in self.letters else False

    # Override parent method
    def letters_num(self) -> int:
        """ Get number of letters in alphabet """
        return self.__letters_num

    @staticmethod
    def example() -> str:
        """ Return text example """
        return "Example of simple english language tex"


if __name__ == "__main__":
    """
    Тесты:
    1. Создайте объект класса EngAlphabet
    2. Напечатайте буквы алфавита для этого объекта
    3. Выведите количество букв в алфавите
    4. Проверьте, относится ли буква F к английскому алфавиту
    5. Проверьте, относится ли буква Щ к английскому алфавиту
    6. Выведите пример текста на английском языке
    """

    # 1) Создаем объект класса EngAlphabet
    en = EngAlphabet(language="EN", letters=string.ascii_lowercase)
    print(f"Алфавит: '{en}'.")

    # 2) Выведем буквы алфавита
    en.print_letters()

    # 3) Выведем количество букв в алфавите
    print(f"Чисто букв в алфавите: {en.letters_num()}.")

    # 4) Проверим, относится ли символ 'F' к английскому алфавиту
    test_letter = "F"
    print("Буква '{0}' {1} к английскому алфавиту.".format(test_letter,
                                                        ("относится" if en.is_en_letter(test_letter) else
                                                         "не относится")))

    # 5) Проверим, относится ли символ 'Щ' к английскому алфавиту
    test_letter = "Щ"
    print("Буква '{0}' {1} к английскому алфавиту.".format(test_letter,
                                                        ("относится" if en.is_en_letter(test_letter) else
                                                         "не относится")))

    # 6) Выведем пример текста на английском языке:
    print(f"Пример текста: '{EngAlphabet.example()}'.")

